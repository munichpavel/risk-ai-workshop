'''Shared functions for model selection'''
import os
from pathlib import Path

import yaml

PROJECT_ROOT = Path(os.environ['PROJECT_ROOT'])


def get_params():
    params = yaml.safe_load(open(
        PROJECT_ROOT / 'risk_learning' / 'model_selection' / 'params.yaml'
    ))
    return params
