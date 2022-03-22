from pathlib import Path
import shutil
import subprocess

import pytest
from pytest import approx

import model_selection
from model_selection import utils, split

PROJECT_ROOT = Path(__file__).parent.parent
MODEL_SELECTION_DIR = Path(model_selection.__file__).parent


def test_pipeline_runs(tmpdir, monkeypatch):
    '''Weak end-to-end test'''

    tmpdir = Path(tmpdir)
    data_dir_test = tmpdir / 'notebooks' / 'data'
    data_dir_test.mkdir(parents=True)

    shutil.copy(
        src=PROJECT_ROOT / 'notebooks' / 'data' / 'default.csv',
        dst=data_dir_test
    )

    monkeypatch.setenv('PROJECT_ROOT', tmpdir.as_posix())

    out = subprocess.run([
        'python', 'split.py',
        '--data_path', (data_dir_test / 'default.csv').as_posix()
    ], cwd=MODEL_SELECTION_DIR, check=True)

    assert out.returncode == 0


# Test model selection utils
def test_get_params():
    '''Weak test for shared function to read model selection parameters'''
    params = utils.get_params()
    assert isinstance(params, dict)


# Test split script
@pytest.mark.parametrize(
    'train_ratio,test_ratio,expected,ExpectedException',
    [
        (0.6, 0.2, 0.2, None),
        (0.9, 0.9, None, ValueError),
        (-0.5, 0.8, None, ValueError),
        (0.5, -0.3, None, ValueError),
    ]
)
def test_get_validation_ratio_split(
    train_ratio, test_ratio, expected, ExpectedException
):

    if ExpectedException is None:
        res = split.get_validation_split_ratio(train_ratio, test_ratio)
        assert res == approx(expected)

    else:
        with pytest.raises(ExpectedException):
            split.get_validation_split_ratio(train_ratio, test_ratio)
