'''Evaluate model based on metric in params and input data'''
import os
from pathlib import Path
import joblib
import json

import pandas as pd
import sklearn.metrics as metrics


def main(stage_name: str, stage_params: dict) -> None:
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
    with open(outdir / 'metrics.json', "w") as fp:
        for model_path in model_paths:
            clf = joblib.load(model_path)
            predictions_by_class = clf.predict_proba(X)
            predictions = predictions_by_class[:, 1]
            avg_prec = metrics.average_precision_score(y, predictions)

            json.dump({"avg_prec": avg_prec}, fp, indent=4)


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

    main(args.stage_name, stage_params)
