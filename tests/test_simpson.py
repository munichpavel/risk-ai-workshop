'''Tests for simpson paradox-related functionality'''
import pytest

import xarray as xr
import numpy as np

from risk_learning.simpson import (
    compute_margin, transform_data_array_component
)


@pytest.mark.parametrize(
    'a_data_array,non_margin_sel,expected',
    [
        (
            xr.DataArray(
                [
                    [6, 8],
                    [3, 1]
                ], dims=('recovered', 'treated'),
                coords=dict(recovered=[0, 1], treated=[0, 1])
            ), dict(treated=1),
            np.array(8. + 1.)
        ),
        (
            xr.DataArray(
                [[
                    [6, 8],
                    [3, 1]

                ], [
                    [4, 22],
                    [27, 9]
                ]],
                dims=("recovered", "gender", "treated"),
                coords=dict(recovered=[0, 1], gender=[0, 1], treated=[0, 1])
            ), dict(treated=1),
            np.array(8. + 1. + 22. + 9.)
        ),
        (
            xr.DataArray(
                [[
                    [6, 8],
                    [3, 1]

                ], [
                    [4, 22],
                    [27, 9]
                ]],
                dims=("recovered", "gender", "treated"),
                coords=dict(recovered=[0, 1], gender=[0, 1], treated=[0, 1])
            ), dict(treated=1, gender=1),
            np.array(1. + 9.)
        ),
        (
            xr.DataArray(
                [[
                    [1, 2],
                    [3, 4]

                ], [
                    [5, 6],
                    [7, 8]
                ]],
                dims=("recovered", "gender", "treated"),
                coords=dict(recovered=[0, 1], gender=[0, 1], treated=[0, 1])
            ), dict(),
            np.array(8. * 9. / 2.)
        ),
    ]
)
def test_compute_margin(a_data_array, non_margin_sel, expected):
    res = compute_margin(a_data_array, non_margin_sel)
    assert res == expected


def translate_component_by(a_data_array, component, epsilon):
    return a_data_array[component] + epsilon


def custom_function(a_data_array, nu):
    """A simpson's paradox inspired function"""
    first = (a_data_array[dict(recovered=1, gender=1, treated=1)] + nu)
    second = (
        compute_margin(a_data_array, dict(gender=1, treated=0))
        / compute_margin(a_data_array, dict(gender=1, treated=1))
    )

    return first * second


@pytest.mark.parametrize(
     'a_data_array,component_function,expected',
     [
        (
            xr.DataArray(
                [
                    [6, 8],
                    [3, 1]
                ], dims=('recovered', 'treated'),
                coords=dict(recovered=[0, 1], treated=[0, 1])
            ),
            # Using the above component_pre_function
            lambda a_data_array: translate_component_by(
                    a_data_array, dict(recovered=0, treated=1), 2
                ),
            10
        ),
        (
            xr.DataArray(
                [[
                    [6, 8],
                    [3, 1]
                ], [
                    [4, 22],
                    [27, 9]
                ]],
                dims=("recovered", "gender", "treated"),
                coords=dict(recovered=[0, 1], gender=[0, 1], treated=[0, 1])
            ),
            # Using the above component_pre_function
            lambda a_data_array: custom_function(a_data_array, 1),
            30
        ),

     ]
)
def test_transform_data_array_component(
    a_data_array, component_function, expected
):

    res = transform_data_array_component(a_data_array, component_function)
    assert res == expected
