import os
from pathlib import Path
from joblib import dump

import pandas as pd

from sklearn.linear_model import LogisticRegression

from risk_learning.model_selection.utils import get_params


def main(
    stage_name: str, stage_params: dict,
    input_data_stage: str,
    feature_filename: str, target_filename: str
) -> None:
    project_root = Path(os.environ['PROJECT_ROOT'])
    data_dir = project_root / 'notebooks' / 'data'
    input_dir = data_dir / input_data_stage
    out_dir = data_dir / stage_name
    out_dir.mkdir(exist_ok=True)

    X = pd.read_csv(input_dir / feature_filename)
    y = pd.read_csv(input_dir / target_filename)

    clf = LogisticRegression()
    clf_name = 'logistic-regression'

    clf.fit(X, y)

    dump(clf, out_dir / (clf_name + '.joblib'))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Try different models for model selection'
    )
    parser.add_argument(
        '--input_data_stage', type=str, help='stage name for input data'
    )
    parser.add_argument(
        '--feature_filename', type=str, help='filename for features to train'
    )
    parser.add_argument(
        '--target_filename', type=str, help='filename for target to train'
    )
    args = parser.parse_args()

    params = get_params()
    stage_name = 'fit'
    stage_params = params[stage_name]

    main(
        stage_name, stage_params,
        args.input_data_stage,
        args.feature_filename, args.target_filename
    )
