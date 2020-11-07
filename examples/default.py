import os
from greensms.client import GreenSMS

os.environ['GREENSMS_USER'] = 'username'
os.environ['GREENSMS_PASS'] = 'password'

client = GreenSMS()