# pyrepo-cookiecutter

personal repo bootstrap

### use it

Recommend using [`cruft`](https://github.com/cruft/cruft) instead of cookiecutter:

```sh
cruft create https://github.com/tlambert03/pyrepo-cookiecutter
```

### update it

To update an existing project that was created from this template using cruft,
run `cruft update` in the root of the project.

### stuff included

- [PEP 517](https://peps.python.org/pep-0517/) build system with [setuptools
  backend](https://setuptools.pypa.io/en/latest/build_meta.html) (build with `python -m build`)
- [PEP 621](https://peps.python.org/pep-0621/) metadata in `pyproject.toml`
- git tag-based versioning with
  [setuptools-scm](https://github.com/pypa/setuptools_scm)
- autodeplot to PyPI on tagged commit (set `TWINE_API_KEY` env var on github)
- Testing with [tox](https://tox.wiki/en/latest/) &
  [pytest](https://docs.pytest.org/en/7.1.x/)
- CI & testing with [github actions](https://docs.github.com/en/actions) and
  [`tox-gh-actions`](https://github.com/ymyzk/tox-gh-actions)
- [pre-commit](https://pre-commit.com/) with
  - [conventional-pre-commit](https://github.com/compilerla/conventional-pre-commit)
  - [autoflake](https://github.com/PyCQA/autoflake)
  - [isort](https://github.com/PyCQA/isort)
  - [black](https://github.com/psf/black)
  - [pyupgrade](https://github.com/asottile/pyupgrade)
  - [flake8](https://github.com/PyCQA/flake8)
  - [mypy](https://github.com/python/mypy)
- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) encouraged (auto-changelogs coming)
