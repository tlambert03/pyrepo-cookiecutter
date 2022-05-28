{% if cookiecutter.version_control == 'setuptools-scm' -%}
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("{{cookiecutter.project_name}}")
except PackageNotFoundError:
    __version__ = "uninstalled"
{%- else -%}
__version__ = '0.1.0'
{%- endif %}
__author__ = "{{ cookiecutter.full_name }}"
__email__ = "{{ cookiecutter.email }}"
