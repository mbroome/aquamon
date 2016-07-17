import logging
import base64
import functools
import json
import cherrypy

import pprint
pp = pprint.PrettyPrinter(indent=4)

from infrastructure.exceptions import *

logger = logging.getLogger('aquamon.' + __name__)

