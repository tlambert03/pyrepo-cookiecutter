"""{{ cookiecutter.project_short_description }}"""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("{{cookiecutter.project_name}}")
except PackageNotFoundError:
    __version__ = "uninstalled"

__author__ = "{{ cookiecutter.full_name }}"
__email__ = "{{ cookiecutter.email }}"
