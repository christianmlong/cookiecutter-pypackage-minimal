# pylint: disable=invalid-name
"""

    config.py

    Common configuration for the {{ cookiecutter.package_name }} package.

"""

import os
import logging
import ConfigParser as configparser

package_dir = os.path.dirname(__file__)
config_file_name = 'config.ini'
config_file_path = os.path.join(package_dir, config_file_name)
CONFIG = configparser.ConfigParser()
CONFIG.read(config_file_path)
DEBUG_LOG = CONFIG.getboolean('misc', 'debug_log')

logging.basicConfig()
LOG = logging.getLogger('{{ cookiecutter.package_name }}')

# Most logs are written to stdout, and we let the process manager (e.g.
# Upstart) take care of logging them to the right place. However, the
# {{ cookiecutter.package_name }} package also can log certain special occurrences (e.g.
# exceptions) to its own log files, located at /var/log/ciam/{{ cookiecutter.package_name }}.
LOG_DIR = '/var/log/ciam/{{ cookiecutter.package_name }}'

if DEBUG_LOG:
    LOG.setLevel(logging.DEBUG)
else:
    LOG.setLevel(logging.INFO)

