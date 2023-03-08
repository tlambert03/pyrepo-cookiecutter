# pyrepo-cookiecutter **simple**

This is my personal python repository bootstrap.

*This is a simplified version: using only a minimal setup without a lot of tooling.*

Feel free to use it as a launching point for your next project!

## How to use it

### 1. Create a new repo with cookiecutter

```sh
pip install cookiecutter
cookiecutter https://github.com/tlambert03/pyrepo-cookiecutter --checkout simple
```

### 2. Run `git init`

After creating the repo, you'll want to initialize a git repo.

```sh
cd <your-package-name>
git init
git add .
git commit -m 'build: Initial Commit'
```

### 3. Install Locally and Run Tests

To run tests locally, you'll need to install the package in editable mode.

I like to first create a new environment dedicated to my package:

```sh
mamba create -n <your-package-name> python
mamba activate <your-package-name>
```

Then install the package in editable mode:

```sh
pip install -e .[test]
```

Finally, run the tests:

```sh
pytest
```

### 4. Upload to GitHub

If you have the [GitHub CLI](https://cli.github.com/) installed, and would like
to create a GitHub repository for your new package:

```sh
gh repo create --source=. --public --remote=origin --push
```

> alternatively, you can follow github's guide for
> [adding a local repository to github](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github#adding-a-local-repository-to-github-using-git)

## Stuff included

- [PEP 517](https://peps.python.org/pep-0517/) build system with [hatch
  backend](https://hatch.pypa.io/)
  - build with `python -m build`, [*not* `python
    setup.py`](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html)!
- [PEP 621](https://peps.python.org/pep-0621/) metadata in `pyproject.toml`
  - *all* additional configurables are also in `pyproject.toml`
- uses `src` layout ([How come?](https://hynek.me/articles/testing-packaging/))
- single source of version is in your top level `__init__.py`
- Testing with [pytest](https://docs.pytest.org/en/7.1.x/)
- basic testing on CI with [github actions](https://docs.github.com/en/actions),
  (see `.github/workflows/test.yml`)

## Deploying to PyPI

When ready to deploy a version, first makd sure to bump the version in
your `__init__.py` and commit it.  

Then, build and upload to PyPI with:

```sh
pip install build
python -m build
twine upload --username YOUR_USER --password YOUR_PASSWORD --skip-existing dist/*
```

(you'll need a PyPI account, and to be the owner/maintainer of the package)
