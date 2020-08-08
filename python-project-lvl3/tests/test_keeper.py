"""Automatic tests for keeper.py module"""

import os
import pytest
import page_loader.keeper
import page_loader.config as config
from tmpdir import TemporaryDirectory

TEST_DIR = config.tests['directory']


def test_save_source_locally():
    with TemporaryDirectory(TEST_DIR):
        file_name = 'mytest.txt'
        content = 'Hello Keeper!'
        success = page_loader.keeper.save_source_locally(
            file_name, TEST_DIR, content)

        file_path = os.path.join(TEST_DIR, file_name)
        file_content = ''
        with open(file_path, 'r') as fh:
            file_content = fh.read()

        assert(
            isinstance(success, bool)
            and success is True
            and os.path.exists(TEST_DIR)
            and file_content == content
        )


@pytest.mark.parametrize(
    'output_dir', [
        (os.path.join(TEST_DIR, 'autotest_01')),
        (os.path.join(TEST_DIR, 'autotest_02/nested/more/more/more')),
        (
            os.path.join(
                TEST_DIR,
                'autotest_03/кирилическое наименование каталога/test'
            )
        ),
    ]
)
def test_directory_creation(output_dir):
    with TemporaryDirectory(TEST_DIR):
        file_name = 'check_dir_createion.txt'
        content = 'Hello Keeper!'
        page_loader.keeper.save_source_locally(
            file_name, output_dir, content)

        file_path = os.path.join(output_dir, file_name)
        assert os.path.exists(file_path)


def test_create_directory_with_exception():
    with pytest.raises(PermissionError):
        page_loader.keeper.save_source_locally(
            'test.txt', '/page_loader', 'Hello Keeper!'
        )
