# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "{{ cookiecutter.project_name }}"
copyright = "{% now 'local', '%Y' %}, {{ cookiecutter.full_name }}"
author = "{{ cookiecutter.full_name }}"

django_settings = {% if cookiecutter.create_django_default_files.lower() == 'y' -%}
        "{{ cookiecutter.project_slug }}.config.settings"
    {%- else -%}
        <#FIXME: replace with import path to django settings>
    {%- endif %}

# The short X.Y version.
version = "{{ cookiecutter.version }}"
# The full version, including alpha/beta/rc tags.
release = "{{ cookiecutter.version }}"

# The master toctree document.
master_doc = "index"

# The suffix(es) of source filenames.
source_suffix = [".rst", ".md"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "autodoc2",
    "sphinx.ext.napoleon",
    "sphinxcontrib_django",
]

myst_enable_extensions = [
    "colon_fence",
    "fieldlist",
    "linkify",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "sphinx_rtd_theme"
html_theme = "furo"
html_theme_options = {
    "source_repository": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    "source_branch": "master",
    # "announcement": "<b>v0.1.0</b> is now out! See the Changelog for details",
}

# -- Options for autodoc2 -------------------------------------------------
# https://sphinx-autodoc2.readthedocs.io/en/latest/
autodoc2_render_plugin = "myst"
autodoc2_packages = [
    {
        "path": "../../signoffs",
        "auto_mode": False,
    },
]

autodoc2_module_all_regexes = [
]