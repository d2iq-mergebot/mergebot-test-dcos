import os

import pytest

import release


@pytest.fixture(scope='module')
def config():
    if not os.path.exists('dcos-release.config.yaml'):
        pytest.skip("Skipping because there is no configuration in dcos-release.config.yaml")
    return release.load_config('dcos-release.config.yaml')


@pytest.fixture(scope='module')
def config_testing(config):
    if 'testing' not in config:
        pytest.skip("Skipped because there is no `testing` configuration in dcos-release.config.yaml")
    return config['testing']


@pytest.fixture(scope='module')
def config_aws(config_testing):
    if 'aws' not in config_testing:
        pytest.skip("Skipped because there is no `testing.aws` configuration in dcos-release.config.yaml")
    return config_testing['aws']


@pytest.fixture(scope='module')
def config_azure(config_testing):
    if 'azure' not in config_testing:
        pytest.skip("Skipped because there is no `testing.azure` configuration in dcos-release.config.yaml")
    return config_testing['azure']
