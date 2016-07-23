#!/usr/bin/python
import os
import sys
import argparse
import time
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../lib')

from Adafruit_PWM_Servo_Driver import PWM

import pprint
pp = pprint.PrettyPrinter(indent=4)

def parseArgs():
   parser = argparse.ArgumentParser(description='lights')
   parser.add_argument('--debug', action="store_true", dest="debug")

   parser.add_argument('-f', action="store", dest="file", default='../etc/lights.json', help='File')
   parser.add_argument('-e', action="store", dest="entry", required=True, help='Entry')

   args = parser.parse_args()
   return(args)

args = parseArgs()

def createSteps(low, up, leng):
    step = ((up-low) * 1.0 / leng)
    return [low+i*step for i in xrange(leng)]

content = open(args.file).read()
config = json.loads(content)

timeframe = config[args.entry]['span']

data = {}
pointCount = 0
for channel in config[args.entry]['channels']:
   rev = False
   if config[args.entry]['channels'][channel]['from'] > config[args.entry]['channels'][channel]['to']:
      s = config[args.entry]['channels'][channel]['to']
      e = config[args.entry]['channels'][channel]['from']
      rev = True
   else:
      s = config[args.entry]['channels'][channel]['from']
      e = config[args.entry]['channels'][channel]['to']
   points = createSteps(int(s), 4096*int(e)/100, int(timeframe) * 4)
   #del(points[0])
   pointCount = len(points)
   if rev:
      data[channel] = points[::-1]
   else:
      data[channel] = points

pwm = PWM(0x40)
pwm.setPWMFreq(100)

start = time.time()
for c in range(0, pointCount):
   for channel in data:
      pwm.setPWM(int(channel), 0, int(data[channel][c]))
   time.sleep(0.25)

