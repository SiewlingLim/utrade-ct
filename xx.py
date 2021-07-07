"""
Output channel that sends emails. Relies on Mandrill, Sendgrid or SMTP to actually send mails.
"""
#import settings
import pprint
from twisted.logger import Logger
log = Logger()
#import mandrill
import requests
#from htmlmin import minify
#from httpd_site import env
#from channel import OutputChannel
#from constants import OUTPUT_CHANNEL_EMAIL
#import sendgrid
#from sendgrid.helpers.mail import *
#from email.MIMEText import MIMEText
from email.mime.text import MIMEText
import smtplib

try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib

#def do_send_alert(input_channel=None, canarydrop=None, **kwargs):
#    msg = input_channel.format_canaryalert(
#                                  params={'subject_required':True,
#                                          'from_display_required':True,
#                                          'from_address_required':True},
#                                  canarydrop=canarydrop,
#                                  **kwargs)
#    self.data = msg
#    if 'type' in canarydrop._drop:
#        self.data['tokentype']   = canarydrop._drop['type']
#
#    self.data['canarytoken'] = canarydrop['canarytoken']
#    self.data['description'] = unicode(canarydrop['memo'], "utf8") if canarydrop['memo'] is not None else ''
#    if settings.SMTP_SERVER:
#        self.smtp_send(msg=msg,canarydrop=canarydrop)
#    else:
#        log.error("No email settings found")

def smtp_send(msg=None, canarydrop=None):
    try:
        fromaddr = 'canary@utrace.org'
        toaddr = 'sllim0803@yahoo.com'

        smtpmsg = MIMEText('testing')
        smtpmsg['From'] = fromaddr
        smtpmsg['To'] = toaddr
        smtpmsg['Subject'] = 'testing_subject' 

        print('starting')
        server = smtplib.SMTP_SSL('smtp.hostinger.com',465)
        print('starting2')
        server.ehlo()
        print('starting')
        server.starttls()
        print('starting')
        server.ehlo()
        print('starting')
        server.login('canary@utrace.org','Welcome@1')
        print('starting')
        text = smtpmsg.as_string()
        print('starting')
        server.sendmail(fromaddr, toaddr, text)

        print('done')
    except smtplib.SMTPException as e:
        log.error('A smtp error occurred: %s - %s' % (e.__class__, e))
        print(e)

smtp_send()
#EmailAdd = 'canary@utrace.org'
#Pass = 'Welcome@1'
#fromaddr = 'canary@utrace.org'
#toaddr = 'sllim0803@yahoo.com'
#
#smtpmsg = MIMEText('testing')
#smtpmsg['From'] = fromaddr
#smtpmsg['To'] = toaddr
#smtpmsg['Subject'] = 'testing_subject' 
#with smtplib.SMTP_SSL('smtp.hostinger.com',465) as smtp: #Added Gmails SMTP Server
#    smtp.login(EmailAdd,Pass) #This command Login SMTP Library using your GMAIL
#    smtp.send_message(smtpmsg) #This Sends the message
