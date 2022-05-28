#!/usr/bin/env python
import os
import subprocess
from contextlib import suppress
import sys

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


# if __name__ == "__main__":

#     if "PYTEST_CURRENT_TEST" in os.environ:
#         sys.exit()

#     with suppress(Exception):
#         subprocess.run(["git", "init", "-q"])
#         subprocess.run(["git", "add", "."])
#         subprocess.run(["git", "commit", "-q", "-m", "Initial commit"])

#     try:
#         print("install pre-commit ...")
#         subprocess.run(["pip", "install", "pre-commit"], stdout=subprocess.DEVNULL)
#         print("updating pre-commit...")
#         subprocess.run(["pre-commit", "autoupdate"], stdout=subprocess.DEVNULL)
#         subprocess.run(["pre-commit", "install"])
#     except Exception:
#         print("Failed to install pre-commit.  Do it manually.")
