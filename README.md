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
- uses `src` layout ([why?](https://hynek.me/articles/testing-packaging/))

### other steps

- setup the [pre-commit.ci](https://pre-commit.ci/) service to run all pre-commit
  checks on every PR (in case contributors aren't running it locally).

### Conventional Commits

This is setup to use [Conventional
Commits](https://www.conventionalcommits.org/en/v1.0.0/) (or at least, that's a
goal). To get it working:

- Use the `conventional-pre-commit` step in pre-commit. It will force you to use
  conventional commits locally.
- [VS Code]: Add the [Conventional
  Commits](https://marketplace.visualstudio.com/items?itemName=vivaxy.vscode-conventional-commits)
  extension, making it easier to create conventional commits.
- This still doesn't protect GitHub PR commits, so add the [Semantic
  PRs](https://github.com/marketplace/semantic-prs) GitHub App to check that PR
  titles follow the Convention Commits Spec (and require squash commits)
- Set up [`python-semantic-release` on GitHub
  Actions](https://python-semantic-release.readthedocs.io/en/latest/automatic-releases/github-actions.html)
  (included in `ci.yml`)
- Protect the `main` branch:
  - use only PRs for `main`
  - use squash merge
  - require the `Semantic PRs` check to pass for merging
  - consider allowing only `semantic-release` to push to that branch.

- Future: use [frappucino](https://github.com/Carreau/frappuccino) or
  [griffe](https://github.com/mkdocstrings/griffe) to detect breaking API
  changes & add a GitHub action to enforce a `!` in the title or `BREAKING
  CHANGE` footer.
