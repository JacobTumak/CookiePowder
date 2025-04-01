#!/usr/bin/env python
import os
import subprocess
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


class Opts:
    """
    Stores selected options referenced in this script.
    Each jinja string is resolved by cookiecutter before this file is run
    """
    project_slug = "{{ cookiecutter.project_slug }}"
    open_source_license = '{{ cookiecutter.open_source_license }}'.lower()
    gen_requirements_files = '{{ cookiecutter.generate_requirements_files }}'.lower()
    create_django_default_files = '{{ cookiecutter.create_django_default_files }}'.lower()
    setup_docs = '{{ cookiecutter.setup_docs }}'.lower()


django_default_files = [
    f"{Opts.project_slug}/config/__init__.py",
    f"{Opts.project_slug}/config/asgi.py",
    f"{Opts.project_slug}/config/settings.py",
    f"{Opts.project_slug}/config/urls.py",
    f"{Opts.project_slug}/config/wsgi.py",
    "manage.py",
]


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if Opts.open_source_license == 'none':
        os.remove('LICENSE')

    if Opts.gen_requirements_files == 'y':
        subprocess.run(['pip', 'install', 'pip-tools'])
        subprocess.run(['pip-compile', '-o', 'requirements.txt', 'pyproject.toml', '--resolver=backtracking'])
        subprocess.run(['pip-compile', '-o', 'requirements_dev.txt', 'pyproject.toml', '--resolver=backtracking', '--all-extras'])
        if Opts.setup_docs == 'y':
            subprocess.run(
                [
                    'pip-compile',
                    '-o', 'docs/requirements_docs.txt', 'pyproject.toml',
                    '--resolver=backtracking',
                    '--extra=docs'
                 ]
            )

    if Opts.create_django_default_files != 'y':
        for filepath in django_default_files:
            remove_file(filepath)

    if Opts.setup_docs != 'y':
        shutil.rmtree(f'{PROJECT_DIRECTORY}/docs')
        remove_file(f"{PROJECT_DIRECTORY}/.readthedocs.yaml")
