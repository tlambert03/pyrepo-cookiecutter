{% if cookiecutter.version_control == 'bump2version' -%}
__version__ = '0.0.1'
{%- else -%}
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
{%- endif %}
__author__ = "{{ cookiecutter.full_name }}"
__email__ = "{{ cookiecutter.email }}"
