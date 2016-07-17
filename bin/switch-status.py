#!/usr/bin/env python2.7
import os
import sys
import smtplib
import email.utils
from email.mime.text import MIMEText

import RPi.GPIO as GPIO
import time
import json

toEmail = 'mitchell.broome@gmail.com'
fromEmail = 'mitchell.broome2@gail.com'


def sendAlert(msg):
    import smtplib

    #gmail_user = 'mitchell.broome2@gmail.com'
    gmail_user = 'mitchell.broome@gmail.com'
    #gmail_pwd = 'Rwezkzcs1'
    gmail_pwd = 'jmczywngotibzvlv'
    FROM = fromEmail
    TO = [toEmail]
    SUBJECT = msg
    TEXT = msg

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

# setup the gpio pin to watch for input
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering
GPIO.setup(10, GPIO.IN)    # set GPIO10 as input (button)

# Define a threaded callback function to run in another thread when events are detected
if GPIO.input(10):
   print 'switch on'
   sendAlert('switch on')
   fd = open('/tmp/switch.status', 'w')
   fd.write(json.dumps({'status': 'on'}))
   fd.close()
else:
   print 'switch off'
   sendAlert('switch off')
   fd = open('/tmp/switch.status', 'w')
   fd.write(json.dumps({'status': 'off'}))
   fd.close()

GPIO.cleanup()

