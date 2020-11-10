import os
from greensms.client import GreenSMS

os.environ['GREENSMS_USER'] = 'test'
os.environ['GREENSMS_PASS'] = 'test'

client = GreenSMS()
