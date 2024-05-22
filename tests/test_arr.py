import pytest

import pandas as pd
from pandas.api.types import CategoricalDtype

import numpy as np
import xarray as xr


from risk_learning.arr import (
    convert_to_categorical,
    make_feature_combination_array,
    make_feature_combination_score_array,
    make_trend_reports, make_a_trend_report, make_data_trend_reports
)


def test_convert_to_categorical():
    df = pd.DataFrame(dict(
        gender=[0, 1, 1], occupation=[1, 0, 0], default=[0, 0, 1]
    ))
    categorical_values_dict = dict(
        gender=[0, 1], occupation=[0, 1], default=[0, 1]
    )

    expected = pd.DataFrame(
        dict(gender=[0, 1, 1], occupation=[1, 0, 0], default=[0, 0, 1]),
    ).astype({
        'gender': CategoricalDtype(categories=[0, 1], ordered=True),
        'occupation': CategoricalDtype(categories=[0, 1], ordered=True),
        'default': CategoricalDtype(categories=[0, 1], ordered=True)
    })

    res = convert_to_categorical(df, categorical_values_dict)
    pd.testing.assert_frame_equal(res, expected)


@pytest.mark.parametrize(
    'label_mapping_values,expected',
    [
        (
            {
                "gender": [0, 1],
                "occupation": [0, 1],
            },
            np.array([
                [0, 0],
                [0, 1],
                [1, 0],
                [1, 1]
            ])
        ),
        (
            {
                "gender": [-1, 1],
                "occupation": [-1, 1],
            },
            np.array([
                [-1, -1],
                [-1, 1],
                [1, -1],
                [1, 1]
            ])
        )
    ]
)
def test_make_feature_combination_array(label_mapping_values, expected):
    res = make_feature_combination_array(label_mapping_values)
    np.testing.assert_array_equal(res, expected)


def test_make_feature_combination_scores_array():
    feature_combinations = pd.DataFrame(
        [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ], columns=('first', 'second')
    )
    scores = pd.Series([-0.5, -0.25, 0.25, 0.5])

    expected = xr.DataArray(
        [
            [-0.5, -0.25],
            [0.25, 0.5]
        ],
        dims=('first', 'second'),
        coords=dict(first=[0, 1], second=[0, 1])
    )

    res = make_feature_combination_score_array(feature_combinations, scores)

    xr.testing.assert_equal(res, expected)



@pytest.mark.parametrize(
    'scores,expected',
    [
        (
            xr.DataArray(
                [42, 42], dims=("gender"), coords={"gender": [0, 1]}
            ),

            dict(gender_trend= 0)
        ),
        (
            xr.DataArray(
                [0.4, 0.2], dims=("gender"), coords={"gender": [0, 1]}
            ),
            dict(gender_trend=0.2)
        ),
        (
            xr.DataArray(
                [0.2, 0.4], dims=("gender"), coords={"gender": [0, 1]}
            ),
            dict(gender_trend=-0.2)
        ),
        (
            xr.DataArray(
                [-4, -6], dims=("gender"), coords={"gender": [0, 1]}
            ),
            dict(gender_trend= 2)
        )
    ]
)
def test_make_a_trend_report(scores, expected):
    res = make_a_trend_report(scores)

    assert res == expected


@pytest.mark.parametrize(
    'contingency_probabilities,population_group,expected',
    [
        (
            xr.DataArray(
                np.array([
                    [0.4, 0.1],
                    [0.2, 0.8]]
                ),
                dims=('gender', 'occupation'),
                coords=dict(gender=[0, 1], occupation=[0, 1])
            ),
            'occupation',
            [
                {
                    'population_group': 'occupation',
                    'population_value': 0,
                    'trend': {'gender_trend': pytest.approx(0.2)}
                },
                {
                    'population_group': 'occupation',
                    'population_value': 1,
                    'trend': {'gender_trend': pytest.approx(-0.7)}
                }
            ]
        ),
        (
            xr.DataArray(
                np.array([
                    [4, 1],
                    [2, 8]]
                ),
                dims=('gender', 'occupation'),
                coords=dict(gender=[0, 1], occupation=[0, 1])
            ),
            'occupation',
            [
                {
                    'population_group': 'occupation',
                    'population_value': 0,
                    'trend': {'gender_trend': pytest.approx(2.)}
                },
                {
                    'population_group': 'occupation',
                    'population_value': 1,
                    'trend': {'gender_trend': pytest.approx(-7.)}
                }
            ]
        ),
        (
            xr.DataArray(
                np.array([0.2, 0.1]),
                dims=('gender',),
                coords=dict(gender=[0, 1])
            ),
            '',
            [{'gender_trend': pytest.approx(0.1)}]
        )

    ]
)
def test_make_trend_reports(contingency_probabilities,population_group,expected):
    res = make_trend_reports(
        contingency_probabilities, population_group
    )
    assert res == expected
