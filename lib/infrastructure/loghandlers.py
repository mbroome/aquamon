import os
import logging
import json

import cherrypy

import pprint
pp = pprint.PrettyPrinter(indent=4)


def setupLogging(logRootDir):
   logger = logging.getLogger('aquamon')
   exceptionlogger = logging.getLogger('aquamon-exception')
   auditlogger = logging.getLogger('aquamon-audit')

   if not logRootDir:
      logRootDir = '/var/log'

   try:
      os.makedirs(logRootDir + '/aquamon')
   except:
      pass

   # setup the standard logger
   hdlr = logging.FileHandler('%s/aquamon/aquamon.log' % logRootDir)
   formatter = logging.Formatter('{"time": %(asctime)s, "level": "%(levelname)s", "method": "%(name)s[line:%(lineno)s]", "data": %(message)s}', datefmt='%s')
   hdlr.setFormatter(formatter)
   logger.addHandler(hdlr)
   logger.setLevel(logging.INFO)


