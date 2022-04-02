'''Shared functions for model selection'''
import os
from pathlib import Path
from typing import Union

import yaml

import pandas as pd


PROJECT_ROOT = Path(os.environ['PROJECT_ROOT'])


def get_params():
    params = yaml.safe_load(open(
        PROJECT_ROOT / 'risk_learning' / 'model_selection' / 'params.yaml'
    ))
    return params


def vconcat_pandases(
    pandases: list[Union[pd.DataFrame, pd.Series]]
) -> Union[pd.DataFrame, pd.Series]:

    res = pd.concat(pandases, axis=0)
    res.reset_index(inplace=True, drop=True)
    return res
