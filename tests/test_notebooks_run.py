'''
Test that demo notebook cells execute without errors
Using https://www.thedataincubator.com/blog/2016/06/09/testing-jupyter-notebooks/
'''
import os
from pathlib import Path
import subprocess
import tempfile

import pytest
try:
    import nbformat
except ModuleNotFoundError as err:
    print('Skipping import--will get other error laster if needed')
    print(err)


project_root = Path(os.environ['PROJECT_ROOT'])
notebook_dir = project_root / 'notebooks'


@pytest.mark.notebook
@pytest.mark.parametrize(
    'notebook_path',
    [
        notebook_dir / 'causal-models-exercises.ipynb',
        notebook_dir / 'graphical-models-exercises.ipynb',
        notebook_dir / 'model-selection-exercises.ipynb',
        notebook_dir / 'probability-polytope-exercises.ipynb',
        notebook_dir / 'simpsons-paradox-exercises.ipynb',
    ]
)
def test_ipynb(notebook_path, monkeypatch, tmpdir):

    # Set up mock output directories
    monkeypatch.setenv('DATA_DIR', str(tmpdir))
    monkeypatch.setenv('DG_FIG_DIR', str(tmpdir))
    monkeypatch.setenv('CC_FIG_DIR', str(tmpdir))
    monkeypatch.setenv('EXPERIMENTS_DIR', str(tmpdir))

    nb, errors = _notebook_run(notebook_path)
    assert errors == []


def _notebook_run(path):
    """
    Execute a notebook via nbconvert and collect output.
    """
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = [
            "python", "-m", "nbconvert", "--to", "notebook", "--execute",
            "--ExecutePreprocessor.timeout=60",
            "--output", fout.name, path
        ]
        subprocess.check_call(args)

        fout.seek(0)
        nb = nbformat.read(fout, nbformat.current_nbformat)

    errors = [
        output for cell in nb.cells if "outputs" in cell
        for output in cell["outputs"] if output.output_type == "error"
    ]

    return nb, errors
