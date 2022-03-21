import sys
import random
import os
from pathlib import Path


import yaml

from sklearn.model_selection import train_test_split
import pandas as pd

in_path = sys.argv[1]

params = yaml.safe_load(open("params.yaml"))["prepare"]
random.seed(params["seed"])
train_split = params["train_split"]
test_split = params["test_split"]
target_col = params["target_col"]
validation_split = 1 - test_split - train_split

if validation_split >= 1 or validation_split <= 0:
    # As per dvc example https://github.com/iterative/example-get-started/blob/master/src/prepare.py  # noqa: E501
    # TODO why not raise an error instead?
    msg = (
        f"Entered train and test split ratios {train_split}, {test_split}\n"
        f"resulting in invalid validation split of {validation_split}\n"
    )
    sys.stderr.write(msg)
    sys.exit(1)

project_root = Path(os.environ['PROJECT_ROOT'])
data_dir = project_root / 'notebooks' / 'data'

df = pd.read_csv(in_path)
y = df[target_col]
non_target_cols = [c for c in df.columns if c != target_col]

X = df[non_target_cols]

# Split into train + validation  / test sets
X_train_validate, X_test, y_train_validate, y_test = train_test_split(
    X, y, test_size=test_split, random_state=params["seed"]
)

X_train, X_validate, y_train, y_validate = train_test_split(
    X_train_validate, y_train_validate,
    train_size=train_split, random_state=params["seed"]
)

# TODO shouldn't this come from dvc run command???
outdir = data_dir / 'prepared'
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
