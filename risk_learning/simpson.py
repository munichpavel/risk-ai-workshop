'''Methods related to simpson paradox example generation'''
from typing import Union
from itertools import product

import xarray as xr
import pandas as pd


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
