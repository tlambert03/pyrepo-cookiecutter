# {{cookiecutter.project_name}}

{% if cookiecutter.license != 'No license' -%}
[![License](https://img.shields.io/pypi/l/{{cookiecutter.project_name}}.svg?color=green)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/raw/master/LICENSE)
{%- endif %}
[![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.project_name}}.svg?color=green)](https://pypi.org/project/{{cookiecutter.project_name}})
[![Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}}.svg?color=green)](https://python.org)
[![tests](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/workflows/tests/badge.svg)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/actions)
[![codecov](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_name}})

{{cookiecutter.project_short_description}}
