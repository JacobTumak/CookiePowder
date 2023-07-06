#!/usr/bin/env python
import os
import re
import sys
import subprocess
import datetime

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

django_default_files = [
    "{{cookiecutter.project_slug}}/__init__.py",
    "{{cookiecutter.project_slug}}/asgi.py",
    "{{cookiecutter.project_slug}}/settings.py",
    "{{cookiecutter.project_slug}}/urls.py",
    "{{cookiecutter.project_slug}}/wsgi.py",
    "manage.py",
    "templates"
]


def generate_django_secret():
    subprocess.run(['pip', 'install', '-q', 'django'])
    from django.core.management.utils import get_random_secret_key
    django_secret = get_random_secret_key()

    with open('{{cookiecutter.project_slug}}/settings.py', "r") as file:
        content = file.read()

    # Construct the pattern to match the variable assignment
    pattern = r"{} = .*".format(re.escape('SECRET_KEY'))

    # Replace the variable assignment with the new value
    replaced_content = re.sub(pattern, "{} = '{}'".format('SECRET_KEY', django_secret), content)

    with open('{{cookiecutter.project_slug}}/settings.py', "w") as file:
        file.write(replaced_content)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def replace_var_val(file_path, var_name, new_var_val):

    with open(file_path, "r") as file:
        content = file.read()

    # Construct the pattern to match the variable assignment
    pattern = r"{} = .*".format(re.escape(var_name))

    # Replace the variable assignment with the new value
    replaced_content = re.sub(pattern, "{} = '{}'".format(var_name, new_var_val), content)

    with open(file_path, "w") as file:
        file.write(replaced_content)


def get_py_ver():
    version_info = sys.version_info
    version_string = f"{version_info.major}.{version_info.minor}.{version_info.micro}"
    return version_string


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('docs/AUTHORS.md')

    # if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
    #     cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
    #     os.remove(cli_file)

    if 'Not open-source' == '{{ cookiecutter.open_source_license }}':
        os.remove('LICENSE')

    filepath = "docs/sphinx/conf.py"
    var_name = "copyright"
    new_val = f'{datetime.datetime.now().year}, {{cookiecutter.copyright_entity}}'
    replace_var_val(filepath, var_name, new_val)

    if '{{cookiecutter.generate_requirements_files}}'.lower() == 'y':
        subprocess.run(['pip', 'install', 'pip-tools'])
        subprocess.run(['pip-compile', '-o', 'requirements.txt', 'pyproject.toml', '--resolver=backtracking'])
        subprocess.run(['pip-compile', '-o', 'dev_requirements.txt', 'pyproject.toml', '--resolver=backtracking', '--all-extras'])
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
        subprocess.run(['pip', 'install', '-r', 'dev_requirements.txt'])

    if '{{cookiecutter.create_django_default_files}}'.lower() == 'y':
        if '{{cookiecutter.generate_django_secret_key}}'.lower() == 'y':
            generate_django_secret()

    else:
        for filepath in django_default_files:
            remove_file(filepath)
