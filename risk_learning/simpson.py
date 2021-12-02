'''Methods related to simpson paradox example generation'''
from typing import Union

import xarray as xr


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
