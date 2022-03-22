from pathlib import Path
import shutil
import subprocess

import model_selection

PROJECT_ROOT = Path(__file__).parent.parent
MODEL_SELECTION_DIR = Path(model_selection.__file__).parent


def test_pipeline_runs(tmpdir, monkeypatch):

    tmpdir = Path(tmpdir)
    data_dir_test = tmpdir / 'notebooks' / 'data'
    data_dir_test.mkdir(parents=True)

    shutil.copy(
        src=PROJECT_ROOT / 'notebooks' / 'data' / 'default.csv',
        dst=data_dir_test
    )

    monkeypatch.setenv('PROJECT_ROOT', tmpdir.as_posix())

    out = subprocess.run([
        'python', 'prepare.py',
        (data_dir_test / 'default.csv').as_posix()
    ], cwd=MODEL_SELECTION_DIR, check=True)

    assert out.returncode == 0
