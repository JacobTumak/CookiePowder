{% set is_open_source = cookiecutter.open_source_license != 'Not open-source' -%}
# {{ cookiecutter.project_name }}

Version: {{ cookiecutter.version }}

{% if is_open_source %}
[![PyPI Version](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }})

[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest)](https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?version=latest)

[![Travis Status](https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg)](target: https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
{%- endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
Free software: {{ cookiecutter.open_source_license }}
Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
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