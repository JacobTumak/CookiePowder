{% set is_open_source = cookiecutter.open_source_license != 'None' -%}
# {{ cookiecutter.project_name }}

{% if is_open_source %}
[![PyPI Version](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
{%- if cookiecutter.setup_docs.lower() == 'y' %}[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest)](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest){% endif %}
[![Tests](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/pytest.yaml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/pytest.yaml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
{% endif %}

Version: {{ cookiecutter.version }}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
{% if cookiecutter.setup_docs.lower() == 'y' -%}
Documentation: <https://{{ cookiecutter.project_slug }}.readthedocs.io>
{%- endif %}

{{ cookiecutter.project_name }} is free software distributed under the {{ cookiecutter.open_source_license }}.
{% endif %}


## Features

- Feature 1
- Feature 2
- Feature 3


## Quick Start

1. Install the `{{ cookiecutter.project_slug }}` package from PyPI
    ```bash
    $ pip install {{ cookiecutter.project_slug }}
    ```

2. Add `'{{ cookiecutter.project_slug }}'` to `INSTALLED_APPS`:
    ```python
    INSTALLED_APPS = [
        ...,
        "{{ cookiecutter.project_slug }}",
           ...,
    ]
    ```
   
## Get Me Some of That
* [Source Code](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
{% if cookiecutter.setup_docs.lower() == 'y' -%}
* [Read The Docs](https://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/)
{%- endif %}
* [Issues](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/issues)
* [PyPI](https://pypi.org/project/{{ cookiecutter.project_slug }})

[{{ cookiecutter.open_source_license }}](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/blob/master/LICENSE)

### Check Out the Demo App

1. `pip install -e git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git#egg={{ cookiecutter.project_slug }}`
1. `python {{ cookiecutter.project_slug }}/manage.py install_demo`
1. `python {{ cookiecutter.project_slug }}/manage.py runserver`


### Acknowledgments
This project would be impossible to maintain without the help of our generous [contributors](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/graphs/contributors)

#### Technology Colophon

Without django and the django dev team, the universe would have fewer rainbows and ponies.

This package was originally created with [`cookiecutter`](https://www.cookiecutter.io/) 
and the [`cookiecutter-powder-pypackage`](https://github.com/JacobTumak/CookiePowder) project template.


## For Developers
Initialise the development environment using the invoke task
   ```bash
   inv tox.venv
   ```
Or create it with tox directly
   ```bash
   tox d -e dev .venv
   ```
Or install the dev requirements with pip
   ```bash
   pip install -r reqirements_dev.txt
   ```

### Tests
   ```bash
   pytest
   ```
or
   ```bash
   tox r
   ```
or run tox environments in parallel using
   ```bash
   tox p
   ```

### Code Style / Linting
   ```bash
   $ isort
   $ black
   $ flake8
   ```

### Versioning
 * [Semantic Versioning](https://semver.org/)
   ```bash
   $ bumpver show
   ```

{% if cookiecutter.setup_docs.lower() == 'y' %}
### Docs
 * [Sphinx](https://www.sphinx-doc.org/en/master/) + [MyST parser](https://myst-parser.readthedocs.io/en/latest/intro.html)
 * [Read The Docs](https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/)
{% endif %}

### Build / Deploy Automation
 * [invoke](https://www.pyinvoke.org/)
   ```bash
   $ invoke -l
   ```
 * [GitHub Actions](https://docs.github.com/en/actions) (see [.github/workflows](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/tree/master/.github/workflows))
 * [GitHub Webhooks](https://docs.github.com/en/webhooks)  (see [settings/hooks](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/settings/hooks))
