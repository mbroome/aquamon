import os
import sys
import smtplib
import email.utils
from email.mime.text import MIMEText

import time
import json

import application

def send(to, subject, msg):
   import smtplib

   gmail_user = application.Config.gmail['user']
   gmail_pwd = application.Config.gmail['key']

   FROM = 'mitchell.broome@gmail.com'
   TO = [to]
   SUBJECT = subject
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
   except Exception, e:
      print "failed to send mail"
      print e

