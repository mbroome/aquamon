import os
import sys
import json
import base64
import threading
import logging

import cherrypy

import pprint
pp = pprint.PrettyPrinter(indent=4)

# account for where we live including the lib path
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
sys.path.append(scriptPath + '/../lib/')

from infrastructure.exceptions import *

logger = logging.getLogger('aquamon.' + __name__)

class Config():
   def __init__(self):
      self.installDir = os.path.dirname(__file__) + '/../'
      self.config = {}

      self.load()

   # load up some configs
   def load(self):
      self.config = self.loadJSON(self.installDir + '/etc/config.json')
      self.gmail = self.loadJSON('/etc/config/aquamon.json')

   def loadJSON(self, configFile):
      contents = open(configFile, 'r').read()
      data = json.loads(contents)
      return(data)

config = Config()

