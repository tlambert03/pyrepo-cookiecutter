import setuptools

{% if cookiecutter.version_control == 'setuptools-scm' -%}
setuptools.setup(use_scm_version={"write_to": "{{cookiecutter.project_slug}}/_version.py"})
{%- else -%}
setuptools.setup()
{%- endif %}
