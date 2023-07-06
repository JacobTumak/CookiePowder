{% set is_open_source = cookiecutter.open_source_license != 'Not open-source' -%}
# {{ cookiecutter.project_name }}

{% if is_open_source %}
[![PyPI Version](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest)](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest)
{% endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io

{{ cookiecutter.project_name }} is free software distributed under the {{ cookiecutter.open_source_license }}.
{% endif %}


## Features

- Feature 1
- Feature 2
- Feature 3


## Get Started

1. The First Step
2. The Second Step
3. The Third Step


## Acknowledgements

This project would be impossible to maintain without the help of our generous contributors.