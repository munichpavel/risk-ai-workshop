'''Shared functions for model selection'''
from pathlib import Path

import yaml

MODULE_DIR = Path(__file__).parent


def get_params():
    params = yaml.safe_load(open(MODULE_DIR / "params.yaml"))
    return params
