#!/usr/bin/python
import os
import sys
import argparse
import logging
import time


import pprint
pp = pprint.PrettyPrinter(indent=4)

# account for where we live including the lib path
scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
sys.path.append(scriptPath + '/../lib/')

import background.monitor

logger = logging.getLogger('aquamon')

def parseArgs():
   parser = argparse.ArgumentParser(description='aquamon')
   parser.add_argument('--debug', action="store_true", dest="debug")

   args = parser.parse_args()
   return(args)

if __name__ == '__main__':
   args = parseArgs()

   mon = background.monitor.Monitor()
   mon.daemon = True

   mon.start()
   try:
      while True:
         time.sleep(2)
   except:
      background.monitor.cleanup()

   background.monitor.cleanup()
