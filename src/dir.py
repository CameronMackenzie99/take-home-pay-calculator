"""Handles directory change for exports."""
import os
from contextlib import contextmanager


@contextmanager
def working_directory(path: str):
    """"Set a destination for exported results."""
    cwd = os.getcwd()
    try:
        __dest = os.path.realpath(path)
        if not os.path.exists(__dest):
            os.mkdir(__dest)
        os.chdir(__dest)
        yield
    finally:
        os.chdir(cwd)
