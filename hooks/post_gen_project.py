from pathlib import Path

{% if cookiecutter.use_cython != 'y'%}
(Path(".").resolve() / '.github' / 'workflows' / 'cython.yml').unlink()
(Path(".").resolve() / 'Makefile').unlink()
(Path(".").resolve() / 'src' / '{{ cookiecutter.project_slug }}' / '_util.py').unlink()
{% endif %}

