'''Evaluate model based on metric in params and input data'''
import os
from pathlib import Path
import joblib
import json

import pandas as pd
import sklearn.metrics as metrics

from risk_learning.simpson import (
    get_flat_combinations, make_feature_combination_score_array
)


def main(
    stage_name: str, stage_params: dict, domain_value_params: dict,
    target_col: str
) -> None:
    project_root = Path(os.environ['PROJECT_ROOT'])
    data_dir = project_root / 'notebooks' / 'data'
    input_dir = data_dir / stage_params['data_in_folder']
    model_dir = data_dir / stage_params['model_in_folder']
    outdir = data_dir / stage_name
    outdir.mkdir(exist_ok=True)

    # Read in feature and target data to fit
    X = pd.read_csv(
        input_dir / stage_params['feature_filename'],
        **stage_params['file_read_params']
    )
    y = pd.read_csv(
        input_dir / stage_params['target_filename'],
        **stage_params['file_read_params']
    )

    # Read in models
    model_path_extension = 'joblib'
    model_paths = list(model_dir.glob(f'*.{model_path_extension}'))
    if not model_paths:
        raise FileNotFoundError(
            f'No {model_path_extension} files found in {model_dir}'
        )

    # Evaluate models
    feature_combination_dict = {}
    for feature_name, domain_values in domain_value_params.items():
        if feature_name == target_col:
            print('Target column, not a feature. Skipping.')
            continue
        feature_combination_dict[feature_name] = domain_values

    feature_combinations = get_flat_combinations(feature_combination_dict)

    for model_path in model_paths:
        model_name = model_path.stem
        with open(outdir / f'metrics_{model_name}.json', "w") as fp:
            clf = joblib.load(model_path)

            # Evaluate on the dataset
            predictions_by_class = clf.predict_proba(X)
            scores = predictions_by_class[:, 1]
            avg_prec = metrics.average_precision_score(y, scores)

            # Evaluate on the feature combinations
            feature_scores = clf.predict_proba(feature_combinations)[:, 1]
            feature_score_array = make_feature_combination_score_array(
                feature_combinations, feature_scores
            )
            mean_female_score = float(
                feature_score_array.sel(gender=0).mean().values
            )
            mean_male_score = float(
                feature_score_array.sel(gender=1).mean().values
            )

            json.dump(
                {
                    'avg_precision': avg_prec,
                    'mean_female_score': mean_female_score,
                    'mean_male_score': mean_male_score
                },
                fp, indent=4
            )


if __name__ == '__main__':
    import argparse
    from risk_learning.model_selection.utils import get_params

    parser = argparse.ArgumentParser(
        description='Evaluate model(s)'
    )
    parser.add_argument(
        '--stage_name', type=str, help='stage name for params'
    )
    args = parser.parse_args()

    params = get_params()
    stage_params = params[args.stage_name]
    domain_value_params = params['data_models']['domain_values']
    split_params = params['split']
    target_col = split_params['target_col']

    main(args.stage_name, stage_params, domain_value_params, target_col)
