#!/usr/bin/env sh

VIRTUALENV_DIR=$WORKON_HOME/{{ cookiecutter.package_name }}
VIRTUALENV_PIP=$VIRTUALENV_DIR/bin/pip
VIRTUALENV_PROJECT_FILE=$VIRTUALENV_DIR/.project

virtualenv "$VIRTUALENV_DIR"
"$VIRTUALENV_PIP" install --upgrade -r requirements/dev_requirements.txt

# Mimic what virtualenvwrapper's setvirtualenvproject command does
pwd > "$VIRTUALENV_PROJECT_FILE"


git init
git add -A
git commit -m "Initial commit"


echo New project {{ cookiecutter.package_name }} created.
echo Type \'workon {{ cookiecutter.package_name }}\' to activate the virtualenv.
