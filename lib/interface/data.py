import logging
import cherrypy
import json

import infrastructure.requestutils
from infrastructure.decorators import *

import application
import background.monitor

logger = logging.getLogger('aquamon.' + __name__)

class DataHandler(infrastructure.requestutils.DefaultHandler):
   def GET(self, **args):
      content = background.monitor.data.copy()
      return(json.dumps(content, indent=4, sort_keys=True))

