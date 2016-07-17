import logging
import cherrypy
import json

import infrastructure.requestutils
from infrastructure.decorators import *

import application

logger = logging.getLogger('aquamon.' + __name__)

class HealthcheckHandler(infrastructure.requestutils.DefaultHandler):
   def GET(self, **args):
      print application.Config.config
      content = open('/tmp/switch.status').read()
      return(content)

