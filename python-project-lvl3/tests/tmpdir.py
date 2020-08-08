"""This is a simple analogue of the tempfile library"""

import os
import shutil

__all__ = ["TemporaryDirectory"]


class TemporaryDirectory(object):
    """Create and return a temporary directory. It used as a context manager
    Example use:

        with TemporaryDirectory(PATH_TO_DIR) as tmpdir:
            ...

    After exiting the context, the temporary directory will be deleted
    """
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return "<{} {}>".format(self.__class__.__name__, self.path)

    def __enter__(self):
        return self.path

    def __exit__(self, exc, value, tb):
        if os.path.exists(self.path):
            shutil.rmtree(self.path)
