'''Methods related to simpson paradox example generation'''
from typing import Union
from itertools import product

import xarray as xr
import pandas as pd
import numpy as np


def compute_margin(a_data_array, non_margin_sel: dict) -> float:
    res = a_data_array.sel(**non_margin_sel).sum()
    res = res.values

    return res


def transform_data_array_component(
    a_data_array: xr.DataArray, component_function
) -> Union[int, float]:
    new_component_value = component_function(a_data_array)
    # res = a_data_array.copy()
    # res[component] = new_component_value

    return float(new_component_value)


def get_flat_combinations(coords: dict) -> pd.DataFrame:

    flat_combination_cols = coords.keys()
    flat_combination_values = list(product(*list(coords.values())))
    flat_combinations = pd.DataFrame(
        flat_combination_values, columns=flat_combination_cols
    )
    return flat_combinations


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
        coords=coords
    )
    for row_idx, feature_series in feature_combinations.iterrows():
        feature_dict = feature_series.to_dict()
        score_array[feature_dict] = scores[row_idx]

    return score_array
