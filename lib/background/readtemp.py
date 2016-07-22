import os
import sys
import json
import base64
import logging
import time

import pprint
pp = pprint.PrettyPrinter(indent=4)

from infrastructure.exceptions import *

import application

logger = logging.getLogger('aquamon.' + __name__)


class Check():
   def __init__(self):
      self.deviceDir = '/sys/bus/w1/devices'

   def check(self, monitor, config):
      data = {}

      filename = '%s/%s/w1_slave' % (self.deviceDir, config['probe'])
      try:
         contents = open(filename, 'r').read()
         lines = contents.split('\n')
         loaded = False
         for line in lines:
            if line[-3:] == 'YES':
               loaded = True
            elif loaded and len(line):
               parts = line.split('t=')
               measurement = parts[1]
               temp_c = float(measurement) / 1000.0
               temp_f = temp_c * 9.0 / 5.0 + 32.0

               data = {'point': monitor, 'value': temp_f, 'polltime': time.time()}
      except Exception, e:
         pp.pprint(e)

      return(data)

