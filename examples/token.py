import os
from greensms.client import GreenSMS

os.environ['GREENSMS_TOKEN'] = '1234'  # Change this value to your actual Token
token_client = GreenSMS()
res = token_client.account.balance()
