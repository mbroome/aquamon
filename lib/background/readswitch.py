import os
import sys
import json
import base64
import logging
import time
import RPi.GPIO as GPIO

import pprint
pp = pprint.PrettyPrinter(indent=4)

from infrastructure.exceptions import *
import application
import model.sendemail

from background.gpiostate import STATUS as GPIOStatus

logger = logging.getLogger('aquamon.' + __name__)


class Check():
   def __init__(self):
      GPIO.setmode(GPIO.BCM)
      self.states = {False: 'off', True: 'on'}


   def check(self, monitor, config):
      pin = self.pinSetup(monitor)

      status = GPIO.input(pin)
      if self.states[status] == config['trigger']:
         print 'Trigger happend!'
         model.sendemail.send(application.Config.config['contact'][config['alert']], config['description'], config['description'])
      data = {'monitor': monitor, 'status': self.states[status], 'polltime': time.time()}
      return(data)

   def pinSetup(self, monitor):
      pinConfig = application.Config.config['pinout'][monitor]
      if not GPIOStatus.has_key(pinConfig['pin']):
         GPIO.setup(pinConfig['pin'], GPIO.IN)
         GPIOStatus[pinConfig['pin']] = True

      return(pinConfig['pin'])
