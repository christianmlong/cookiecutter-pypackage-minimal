"""
    This is the single source of the version number for the application.
    We use the 'bumpversion' package to increment the version number.
    'bumpversion' also tracks the version number in its .bumpversion.rc file,
    but this file contains the authoritative information.
"""
__version__ = '{{ cookiecutter.package_version }}'
