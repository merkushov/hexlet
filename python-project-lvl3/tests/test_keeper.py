'''Automatic tests for keeper.py module'''

import os
import shutil
import page_loader.keeper

TEST_DIR = './tests/result'


def _remove_test_dir():
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)

    return True


def test_save_source_locally():
    _remove_test_dir()

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

    _remove_test_dir()
