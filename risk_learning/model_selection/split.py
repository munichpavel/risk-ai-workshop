from typing import Union
import random
import os
from pathlib import Path

from sklearn.model_selection import train_test_split
import pandas as pd


def validate_split_ratios(train_ratio: float, test_ratio: float) -> None:
    error_msg = ''
    if train_ratio <= 0 or train_ratio >= 1:
        error_msg += "Train split ratio of {train_ratio} is invalid.\n"
    if test_ratio <= 0 or test_ratio >= 1:
        error_msg += "Test split ratio of {test_ratio} is invalid.\n"

    validation_ratio = 1 - train_ratio - test_ratio

    if validation_ratio <= 0 or validation_ratio >= 1:
        error_msg += (
            f"Entered train and test ratios {train_ratio}, {test_ratio}\n"
            f"resulting in invalid validation split of {validation_ratio}\n"
        )

    if len(error_msg) > 0:
        raise ValueError(error_msg)


def main(
    stage_name: str, stage_params: dict, data_path: str
) -> None:
    random.seed(stage_params['seed'])
    train_ratio = stage_params['train_ratio']
    test_ratio = stage_params['test_ratio']

    validate_split_ratios(train_ratio, test_ratio)

    project_root = Path(os.environ['PROJECT_ROOT'])
    data_dir = project_root / 'notebooks' / 'data'

    target_col = stage_params['target_col']
    non_target_cols = stage_params['non_target_cols']
    df = pd.read_csv(
        data_path, usecols=non_target_cols + [target_col],
        **stage_params['file_read_params']
    )

    X = df[non_target_cols]
    y = df[target_col]

    # Split into train + validation  / test sets
    X_train_validate, X_test, y_train_validate, y_test = train_test_split(
        X, y, test_size=test_ratio, random_state=stage_params['seed']
    )

    train_ratio_after_test_split = train_ratio / (1 - test_ratio)
    X_train, X_validate, y_train, y_validate = train_test_split(
        X_train_validate, y_train_validate,
        train_size=train_ratio_after_test_split,
        random_state=stage_params['seed']
    )

    outdir = data_dir / stage_name
    outdir.mkdir(exist_ok=True)

    out_dict = dict(
        X_train=dict(data=X_train, filename='X-train.csv'),
        y_train=dict(data=y_train, filename='y-train.csv'),
        X_validate=dict(data=X_validate, filename='X-validate.csv'),
        y_validate=dict(data=y_validate, filename='y-validate.csv'),
        X_test=dict(data=X_test, filename='X-test.csv'),
        y_test=dict(data=y_test, filename='y-test.csv')
    )

    for data_filename in out_dict.values():
        data_filename['data'].to_csv(
            outdir / data_filename['filename'], index=False
        )


if __name__ == '__main__':
    import argparse
    from risk_learning.model_selection.utils import get_params

    parser = argparse.ArgumentParser(
        description='Split data for model selection'
    )
    parser.add_argument(
        '--data_path', type=str, help='path for input data'
    )
    args = parser.parse_args()

    params = get_params()
    stage_name = 'split'
    stage_params = params[stage_name]

    main(stage_name, stage_params, args.data_path)
