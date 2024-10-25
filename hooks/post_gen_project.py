#!/usr/bin/env python
import os
import re
import sys
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

django_default_files = [
    "{{ cookiecutter.project_slug }}/config/__init__.py",
    "{{ cookiecutter.project_slug }}/config/asgi.py",
    "{{ cookiecutter.project_slug }}/config/settings.py",
    "{{ cookiecutter.project_slug }}/config/urls.py",
    "{{ cookiecutter.project_slug }}/config/wsgi.py",
    "manage.py",
]


def get_py_ver():
    version_info = sys.version_info
    version_string = f"{version_info.major}.{version_info.minor}.{version_info.micro}"
    return version_string


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def generate_django_secret_key():
    subprocess.run(['pip', 'install', '-q', 'django'])
    from django.core.management.utils import get_random_secret_key
    django_secret = get_random_secret_key()

    with open('{{ cookiecutter.project_slug }}/config/settings.py', "r") as file:
        content = file.read()

    # Construct the pattern to match the variable assignment
    pattern = r"{} = .*".format(re.escape('SECRET_KEY'))

    # Replace the variable assignment with the new value
    replaced_content = re.sub(pattern, "{} = '{}'".format('SECRET_KEY', django_secret), content)

    with open('{{ cookiecutter.project_slug }}/config/settings.py', "w") as file:
        file.write(replaced_content)


if __name__ == '__main__':

    if '{{ cookiecutter.open_source_license }}' == 'None':
        os.remove('LICENSE')

    if '{{ cookiecutter.generate_requirements_files }}'.lower() == 'y':
        subprocess.run(['pip', 'install', 'pip-tools'])
        subprocess.run(['pip-compile', '-o', 'requirements.txt', 'pyproject.toml', '--resolver=backtracking'])
        subprocess.run(['pip-compile', '-o', 'requirements_dev.txt', 'pyproject.toml', '--resolver=backtracking', '--all-extras'])
        subprocess.run(['pip-compile', '-o', 'docs/requirements_docs.txt', 'pyproject.toml', '--resolver=backtracking', '--extra=docs'])

    if '{{ cookiecutter.install_requirements }}'.lower() == 'y':
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
        subprocess.run(['pip', 'install', '-r', 'requirements_dev.txt'])

    if '{{ cookiecutter.create_django_default_files }}'.lower() == 'y':
        if '{{ cookiecutter.generate_django_secret_key }}'.lower() == 'y':
            generate_django_secret_key()
    else:
        for filepath in django_default_files:
            remove_file(filepath)
