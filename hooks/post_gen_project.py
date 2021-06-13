#!/usr/bin/env python
import os
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__" and "No license" == "{{ cookiecutter.license }}":
    remove_file("LICENSE")

    subprocess.run(['git', 'init', '{{cookiecutter.project_name}}'])
    subprocess.run(['git', '-C', '{{cookiecutter.project_name}}', 'add', '.'])
    subprocess.run(['git', '-C', '{{cookiecutter.project_name}}', 'add', '.'])
