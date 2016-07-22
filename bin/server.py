#!/usr/bin/python
import os
import sys
import argparse
import logging
import time

import cherrypy


import pprint
pp = pprint.PrettyPrinter(indent=4)

# account for where we live including the lib path
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
sys.path.append(scriptPath + '/../lib/')

import application

logger = logging.getLogger('aquamon')

def parseArgs():
   parser = argparse.ArgumentParser(description='aquamon')
   parser.add_argument('--debug', action="store_true", dest="debug")

   parser.add_argument('-p', action="store", dest="port", default=80, help='Port to listen on')
   parser.add_argument('--ui', action="store_true", dest="localui", default=False, help='Enable local ui')

   args = parser.parse_args()
   return(args)

if __name__ == '__main__':
   args = parseArgs()

   # if we are running in debug mode, do a simple start
   logger.info('Started')

   cherrypy.quickstart(None, '/', config=application.setupRoutes())


