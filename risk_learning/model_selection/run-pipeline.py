import os
from pathlib import Path
import subprocess

from risk_learning.model_selection import utils

project_root = Path(os.environ['PROJECT_ROOT'])
model_selection_repo_dir = project_root / 'risk_learning' / 'model_selection'
data_dir = project_root / 'notebooks' / 'data'
params = utils.get_params()

############
# Split data
############
in_path = data_dir / 'default.csv'
split_out = subprocess.run([
    'python', 'split.py',
    '--data_path', in_path.as_posix()
], cwd=model_selection_repo_dir, check=True)

###################
# Fit training data
###################
fit_out = subprocess.run([
    'python', 'fit.py',
    '--stage_name', 'fit_train',  # TODO drop this???

], cwd=model_selection_repo_dir, check=True)

#############################
# Evaluate on validation data
#############################
evaluate_out = subprocess.run([
    'python', 'evaluate.py', '--stage_name', 'evaluate_fit_train'
], cwd=model_selection_repo_dir, check=True)
