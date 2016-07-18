import os
import sys
import json
import base64
import threading
import logging
import time
import RPi.GPIO as GPIO

import pprint
pp = pprint.PrettyPrinter(indent=4)

from infrastructure.exceptions import *

import application
import background.readswitch
import background.readtemp

logger = logging.getLogger('aquamon.' + __name__)

data = {}
interval = 300

class Monitor(threading.Thread):
   def __init__(self):
      self.threadName = 'Monitor'

      self.probes = {}
      self.probes['readswitch'] = background.readswitch.Check()
      self.probes['readtemp'] = background.readtemp.Check()

      threading.Thread.__init__(self, name=self.threadName)

   def run(self):
      logger.info('starting the monitor run loop: %s' % self.threadName)

      while True:
         for monitor in application.Config.config['monitor']:
            response = {}
            if self.probes.has_key(application.Config.config['monitor'][monitor]['function']) and not application.Config.config['monitor'][monitor].has_key('disabled'):
               try:
                  response = self.probes[application.Config.config['monitor'][monitor]['function']].check(monitor, application.Config.config['monitor'][monitor])
               except Exception, e:
                  pp.pprint(e)

               #pp.pprint(response)
               data[monitor] = response
         time.sleep(interval)


def cleanup():
   print 'cleanup!'
   GPIO.cleanup()
   os._exit(True)


