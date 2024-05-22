from typing import Dict
from itertools import product

import pandas as pd
from pandas.api.types import CategoricalDtype

import numpy as np
import xarray as xr

from fake_data_for_learning.contingency_tables import calculate_contingency_table


def convert_to_categorical(
        df: pd.DataFrame, categorical_values_dict: Dict
    ) -> pd.DataFrame:
    data_categories = {}
    for feature_name, feature_values in categorical_values_dict.items():
        data_categories[feature_name] = CategoricalDtype(
            categories=feature_values, ordered=True
        )
    res = df.copy()
    res = res.astype(data_categories)
    return res


def make_feature_combination_array(label_mapping_values: Dict) -> np.ndarray:
    res = np.array(list(product(*list(label_mapping_values.values()))))
    return res


def make_feature_combination_score_array(
    feature_combinations: pd.DataFrame, scores: pd.Series
) -> xr.DataArray:
    '''TODO refactor, maybe break into smaller functions with tests'''
    coord_names = feature_combinations.columns
    coords = {}
    for coord_name in coord_names:
        feature_vals = list(set(feature_combinations[coord_name]))
        coords[coord_name] = feature_vals

    # Get score array shape
    score_shape = []
    for vals in coords.values():
        score_shape.append(len(vals))

    score_array = xr.DataArray(
        np.zeros(score_shape),
        dims=coords.keys(),
        coords=coords
    )
    for row_idx, feature_series in feature_combinations.iterrows():
        feature_dict = feature_series.to_dict()
        score_array[feature_dict] = scores[row_idx]

    return score_array


def make_trend_reports(
    contingency_probabilities: xr.DataArray, population_subgroup: str
) -> dict:

    if population_subgroup:
        trend_reports = []
        for population_value in contingency_probabilities[population_subgroup].values:
            population_report = {}
            population_select_dict = {f'{population_subgroup}': population_value}
            trend_report = make_a_trend_report(
                contingency_probabilities[population_select_dict]
            )
            population_report['population_group'] = population_subgroup
            population_report['population_value'] = int(population_value)  # json-serializability
            population_report['trend'] = trend_report
            trend_reports.append(population_report)
    else:
        trend_reports = [
            make_a_trend_report(contingency_probabilities)
        ]

    return trend_reports


def make_a_trend_report(score_contingencies: xr.DataArray) -> dict:
    """
    Define trend as simple difference between scores, due to

    * more tractable analytical expressions for GLMs
    * essential point is trend + or -; no need to compare absolute values across datasets
    * normalizing would require edge cases (denom == 0) and potentially cause numerical issues
    """
    exposure_name = score_contingencies.dims[0]
    num_select = {f'{exposure_name}': 0}  # FIXME this will cause problems for
    denom_select = {f'{exposure_name}': 1}  # non-{0,1} encoding
    trend = float(
        score_contingencies[num_select]
        - score_contingencies[denom_select]
    )
    res = {f'{exposure_name}_trend': trend}
    return res


def make_data_trend_reports(
        df: pd.DataFrame, target_field_name: str, target_field_value: int,
        non_exposure_field_name
    ) -> dict:
    """Generate useful statistics including trend"""
    data_trend_reports = {}
    # Add number of records as it's convenient to have
    data_trend_reports['n_samples'] = df.shape[0]

    # Calculate contingency table
    contingency_counts = calculate_contingency_table(df)
    data_trend_reports['contingency_table'] = contingency_counts.to_dict()

    # Calculate trend
    project_sub_pop = contingency_counts.sum(dim=non_exposure_field_name)
    project_sub_pop_probs = project_sub_pop / project_sub_pop.sum(dim=target_field_name)

    total_population_trend_report = make_a_trend_report(
        project_sub_pop_probs[{target_field_name: target_field_value}]
    )

    data_trend_reports['total_population'] = total_population_trend_report

    # Subpopulation data trend
    default_counts = contingency_counts[{target_field_name: target_field_value}]
    non_target_population_counts = contingency_counts.sum(target_field_name)
    data_default_contingency_probs = default_counts / non_target_population_counts
    data_subpopulation_trend_reports = make_trend_reports(
        data_default_contingency_probs, population_subgroup=non_exposure_field_name
    )
    data_trend_reports['sub_populations'] = data_subpopulation_trend_reports
    return data_trend_reports
