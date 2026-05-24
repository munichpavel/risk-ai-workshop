import os
from pathlib import Path
from joblib import dump

import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from risk_learning.model_selection import utils


def main(stage_name: str, stage_params: dict) -> None:
    project_root = Path(os.environ['PROJECT_ROOT'])
    data_dir = project_root / 'notebooks' / 'data'
    input_dir = data_dir / stage_params['data_in_folder']
    out_dir = data_dir / stage_name
    out_dir.mkdir(exist_ok=True)

    Xs = []
    for feature_filename in stage_params['feature_filenames']:
        Xi = pd.read_csv(
            input_dir / feature_filename,
            **stage_params['file_read_params']
        )
        Xs.append(Xi)

    ys = []
    for target_filenames in stage_params['target_filenames']:
        yi = pd.read_csv(
            input_dir / target_filenames,
            **stage_params['file_read_params']
        )
        ys.append(yi)

    X = utils.vconcat_pandases(Xs)
    y = utils.vconcat_pandases(ys)

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
