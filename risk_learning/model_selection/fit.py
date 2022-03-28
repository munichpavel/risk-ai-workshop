import os
from pathlib import Path
from joblib import dump

import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def main(stage_name: str, stage_params: dict) -> None:
    project_root = Path(os.environ['PROJECT_ROOT'])
    data_dir = project_root / 'notebooks' / 'data'
    input_dir = data_dir / stage_params['data_in_folder']
    out_dir = data_dir / stage_name
    out_dir.mkdir(exist_ok=True)

    X = pd.read_csv(
        input_dir / stage_params['feature_filename'],
        **stage_params['file_read_params']
    )
    y = pd.read_csv(
        input_dir / stage_params['target_filename'],
        **stage_params['file_read_params']
    )

    model_params = stage_params['model_params']
    for model_name, model_metadata in model_params.items():
        # FIXME alternative to eval???
        clf = eval(model_metadata['name'])(**model_metadata['hyperparams'])
        clf.fit(X, y.values.ravel())

        dump(clf, out_dir / (model_name + '.joblib'))


if __name__ == '__main__':
    import argparse
    from risk_learning.model_selection.utils import get_params

    parser = argparse.ArgumentParser(
        description='Fit model(s)'
    )
    parser.add_argument(
        '--stage_name', type=str, help='stage name'
    )

    args = parser.parse_args()

    params = get_params()
    stage_name = args.stage_name
    stage_params = params[stage_name]

    main(stage_name, stage_params)
