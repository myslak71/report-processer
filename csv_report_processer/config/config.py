import os
import logging
import yaml
from logging import config

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

config.dictConfig(yaml.safe_load(open(os.path.join(DIR_PATH, 'logger.yaml'))))

LOGGER = logging.getLogger('crp_logger')
