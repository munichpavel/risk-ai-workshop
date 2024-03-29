import os
from pathlib import Path
import shutil
import subprocess
import csv
from itertools import product
import json
from distutils.dir_util import copy_tree

import pytest
import pandas as pd

import yaml

from risk_learning.model_selection import utils, split


# Test model selection utils
def test_utils_get_params():
    '''Weak test for shared function to read model selection parameters'''
    params = utils.get_params()
    assert isinstance(params, dict)


@pytest.mark.parametrize(
    'pandases,expected',
    [
        (
            [
                pd.DataFrame(dict(noshes=['knish', 'matzah'], rating=[0, 3])),
                pd.DataFrame(dict(noshes=['knish', 'bagel'], rating=[1, 2]))
            ],
            pd.DataFrame(
                dict(
                    noshes=['knish', 'matzah', 'knish', 'bagel'],
                    rating=[0, 3, 1, 2]
                )
            )
        ),
        (
            [
                pd.Series(['knish', 'matzah'], name='noshes'),
                pd.Series(['knish', 'bagel'], name='noshes')
            ],
            pd.Series(
                ['knish', 'matzah', 'knish', 'bagel'], name='noshes'
            )
        )
    ]
)
def test_utils_vconcat_pandases(pandases, expected):
    res = utils.vconcat_pandases(pandases)
    if isinstance(pandases[0], pd.DataFrame):
        pd.testing.assert_frame_equal(res, expected)
    elif isinstance(pandases[0], pd.Series):
        pd.testing.assert_series_equal(res, expected)
    else:
        assert False, 'only pandas dataframes or series in scope'


# Test model selection pipeline
def test_pipeline_runs(tmpdir, monkeypatch):
    '''Weak end-to-end test'''
    ############
    # Test setup
    ############
    project_root = Path(os.environ['PROJECT_ROOT'])
    model_selection_repo_dir = (
        project_root / 'risk_learning' / 'model_selection'
    )
    params = utils.get_params()  # Violate Uncle Bob "locate where used" due to env var monkeypatch below  # noqa: E501

    tmpdir = Path(tmpdir)
    data_dir = tmpdir / 'notebooks' / 'data'
    data_dir.mkdir(parents=True)

    shutil.copy(
        src=project_root / 'notebooks' / 'data' / 'default.csv',
        dst=data_dir
    )
    params_dir_test = tmpdir / 'risk_learning' / 'model_selection'
    params_dir_test.mkdir(parents=True)

    shutil.copy(
        src=project_root / 'risk_learning' / 'model_selection' / 'params.yaml',
        dst=params_dir_test
    )
    monkeypatch.setenv('PROJECT_ROOT', tmpdir.as_posix())

    #############
    # Split stage
    #############
    in_path = data_dir / 'default.csv'
    split_out = subprocess.run([
        'python', 'split.py',
        '--data_path', in_path.as_posix()
    ], cwd=model_selection_repo_dir, check=True)

    # Test that script ran without error
    assert split_out.returncode == 0

    # Test number of output data files
    stage_name = 'split'
    out_file_paths = list((data_dir / stage_name).glob('*'))
    assert len(out_file_paths) == 3 * 2  # = number of splits * data sets per split  # noqa: E501

    # Test shape of output data
    with open(in_path, 'r') as fp:
        input_data_file = csv.reader(fp)
        row_count = sum(1 for row in input_data_file)

    input_data_n_records = row_count - 1
    stage_params = params[stage_name]
    expected_n_records = [
        round(input_data_n_records * stage_params['train_ratio']),
        round(input_data_n_records * stage_params['test_ratio']),
        round(
            input_data_n_records
            * (1 - stage_params['train_ratio'] - stage_params['test_ratio'])
        )
    ]

    expected_n_fields = [len(stage_params['non_target_cols']), 1]  # [n-non-target, n-target]  # noqa: E501
    expected_shapes = frozenset(product(expected_n_records, expected_n_fields))

    actual_shapes = []
    for out_path in out_file_paths:
        df = pd.read_csv(out_path)
        actual_shapes.append(df.shape)

    assert frozenset(actual_shapes) == expected_shapes

    ###########
    # Fit stage
    ###########
    stage_name = 'fit_train'
    stage_params = params[stage_name]

    fit_out = subprocess.run([
        'python', 'fit.py',
        '--stage_name', stage_name
    ], cwd=model_selection_repo_dir, check=True)

    # Test that script ran without error
    assert fit_out.returncode == 0

    out_file_paths = list((data_dir / stage_name).glob('*'))

    assert len(out_file_paths) == len(stage_params['model_params'])

    ################
    # Evaluate stage
    ################
    stage_name = 'evaluate_fit_train'
    stage_params = params[stage_name]

    evaluate_out = subprocess.run([
        'python', 'evaluate.py',
        '--stage_name', stage_name
    ], cwd=model_selection_repo_dir, check=True)

    assert evaluate_out.returncode == 0

    out_file_paths = list((data_dir / stage_name).glob('*.json'))
    assert out_file_paths  # non-empty metric file list

    # Assert metric file(s) can be loaded
    for out_file_path in out_file_paths:
        with open(out_file_path, 'r') as fp:
            try:
                json.load(fp)
            except json.decoder.JSONDecodeError as err:
                assert False, err

    ####################################################
    # Fit selected model with training + validation data
    ####################################################
    fit_selected_out = subprocess.run([
        'python', 'fit.py',
        '--stage_name', 'fit_selected_model',

    ], cwd=model_selection_repo_dir, check=True)

    assert fit_selected_out.returncode == 0

    ######################################
    # Evaluate selected model on test data
    ######################################
    evaluate_selected_out = subprocess.run([
        'python', 'evaluate.py', '--stage_name', 'evaluate_fit_test'
    ], cwd=model_selection_repo_dir, check=True)

    assert evaluate_selected_out.returncode == 0


def test_population_scores(tmpdir, monkeypatch):
    '''TODO refactor away (some) duplication with above end-to-end'''
    # Test setup
    project_root = Path(os.environ['PROJECT_ROOT'])
    model_selection_repo_dir = (
        project_root / 'risk_learning' / 'model_selection'
    )

    tmpdir = Path(tmpdir)
    data_dir = tmpdir / 'notebooks' / 'data'
    data_dir.mkdir(parents=True)

    shutil.copy(
        src=project_root / 'notebooks' / 'data' / 'default.csv',
        dst=data_dir
    )
    model_selection_test_dir = tmpdir / 'risk_learning' / 'model_selection'
    model_selection_test_dir.mkdir(parents=True)

    copy_tree(
        src=model_selection_repo_dir.as_posix(),
        dst=model_selection_test_dir.as_posix()
    )
    monkeypatch.setenv('PROJECT_ROOT', tmpdir.as_posix())

    out = subprocess.run(
        ['python', 'run-pipeline.py'],
        cwd=model_selection_test_dir, check=True
    )

    assert out.returncode == 0

    score_expected_lower_name = 'mean_male_score'
    score_expected_higher_name = 'mean_female_score'

    # Read in metric results
    msg = ''
    for metric_path in (data_dir / 'evaluate_fit_train').glob('*.json'):
        with open(metric_path, 'r') as fp:
            metrics = yaml.safe_load(fp)
        if (
            metrics[score_expected_lower_name]
            >= metrics[score_expected_higher_name]
        ):
            msg += (
                f'\nScore expectation failed for {metric_path.stem}:\n'
                f'{score_expected_lower_name} of {metrics[score_expected_lower_name]}\n'  # noqa: E501
                f'not lower than {score_expected_higher_name} of {metrics[score_expected_higher_name]}'  # noqa: E501
            )

    # TODO refactor away some RY from above
    for metric_path in (data_dir / 'evaluate_selected_model').glob('*.json'):
        with open(metric_path, 'r') as fp:
            metrics = yaml.safe_load(fp)
        if (
            metrics[score_expected_lower_name]
            >= metrics[score_expected_higher_name]
        ):
            msg += (
                f'\nScore expectation failed for {metric_path.stem}:\n'
                f'{score_expected_lower_name} of {metrics[score_expected_lower_name]}\n'  # noqa: E501
                f'not lower than {score_expected_higher_name} of {metrics[score_expected_higher_name]}'  # noqa: E501
            )

    assert not msg, msg  # TODO make less slick? E.g. if msg !='': assert False, msg ...  # noqa: E501


# Test split script
@pytest.mark.parametrize(
    'train_ratio,test_ratio,ExpectedException',
    [
        (0.6, 0.2, None),
        (0.9, 0.9, ValueError),
        (-0.5, 0.8, ValueError),
        (0.5, -0.3, ValueError),
    ]
)
def test_get_validation_ratio_split(
    train_ratio, test_ratio, ExpectedException
):
    if ExpectedException is None:
        split.validate_split_ratios(train_ratio, test_ratio)
    else:
        with pytest.raises(ExpectedException):
            split.validate_split_ratios(train_ratio, test_ratio)
