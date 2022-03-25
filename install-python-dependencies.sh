python -VV
python -m site
python -m pip install --upgrade pip setuptools wheel
python -m pip install --upgrade coverage[toml] virtualenv tox tox-gh-actions
python -m pip install -r requirements.txt
python -m pip install .