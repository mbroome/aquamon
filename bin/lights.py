#!/usr/bin/python
import os
import sys
import argparse
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../lib')

from Adafruit_PWM_Servo_Driver import PWM

import time

def parseArgs():
   parser = argparse.ArgumentParser(description='lights')
   parser.add_argument('--debug', action="store_true", dest="debug")

   parser.add_argument('-c', nargs='*', dest="channels", required=True, help='Channels')

   parser.add_argument('-s', action="store", dest="startpercent", default=0, help='Start')
   parser.add_argument('-p', action="store", dest="percent", help='Percent')
   parser.add_argument('-t', action="store", dest="timeframe", help='Timeframe')
   parser.add_argument('-r', action="store_true", dest="reverse", help='Reverse')

   parser.add_argument('--cmd', action="store", dest="command", choices=('on', 'off'), help='Command')

   args = parser.parse_args()
   return(args)

def createSteps(low, up, leng):
    step = ((up-low) * 1.0 / leng)
    return [low+i*step for i in xrange(leng)]

args = parseArgs()

startpercent = int(args.startpercent)

pwm = PWM(0x40)
pwm.setPWMFreq(100)

if args.command:
   print args.command
   if args.command == 'on':
      pulse = 4000
   else:
      pulse = 0
   for i in args.channels:
      pwm.setPWM(int(i), 0, pulse)

   sys.exit(0)

points = createSteps(startpercent, 4096*int(args.percent)/100, int(args.timeframe) * 4)
if args.reverse:
   points = list(reversed(points))
del(points[0])

start = time.time()
for pulse in points:
   for i in args.channels:
      pwm.setPWM(int(i), 0, int(pulse))
   time.sleep(0.25)
   
