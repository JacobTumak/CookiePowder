# CookiePowder

Version: 0.1.0

CookiePowder is a [cookiecutter](https://pypi.org/project/cookiecutter-python/) template for Django/Python packages,
with tooling and package layout tailored to [powderflask](https://github.com/powderflask)'s workflow i.e. cookiecutter-pypowder

Distributed under the MIT License.

## Features

- [pyproject.toml](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/) build configuration
- [Sphinx](https://www.sphinx-doc.org/en/master/) and [MyST parser](https://myst-parser.readthedocs.io/en/latest/intro.html) 
  build documentation for [Read The Docs](https://readthedocs.org/)
- [invoke](https://www.pyinvoke.org/) tasks CLI automations
- [pip-tools](https://github.com/jazzband/pip-tools) dependency management 
- [bumpver](https://pypi.org/project/bumpver/) and [semantic versioning](https://semver.org/) 
- [isort](https://pypi.org/project/isort/), [black](https://pypi.org/project/black/), and 
  [flake8](https://pypi.org/project/flake8/) opinionated code style / linting 
- [tox](https://pypi.org/project/tox/), [pytest](https://pypi.org/project/pytest/), 
  and [GitHub Actions](https://docs.github.com/en/actions) unit testing and CI 

## Get Started

1. Install `cookiecutter`:

    ```console
    pip install cookiecutter
    ```

2. Run `cookiecutter` with the repository URL for this template:

    ```console
    cookiecutter https://github.com/JacobTumak/CookiePowder
    ```

3. Follow the prompts to generate your project directory.


## Acknowledgements

This cookiecutter template was heavily based on the official [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).

Technologies and decisions [documentation](https://docs.google.com/document/d/1le7BcslojMajsj_rh83VQiki9TPiUJLYHYrCP_WHbYA/edit#heading=h.m9dlnvvcuxln)