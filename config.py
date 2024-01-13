from mody import Tayson
from pyrogram import Client,filters,enums
import redis

r = redis.Redis(
  host='redis-17811.c323.us-east-1-2.ec2.cloud.redislabs.com',
  port=17811,
  password='y41sFD7N8cY5Ob2MGPZkGdrTndVFY92h')

sudo_id = 6094482545
bot_user = Mody.BOT_USER
via_user = Mody.VIA_USER
elhyba = bot_user
via = via_user
api_id = Tayson.APP_ID
api_hash = Tayson.API_HASH
session = Tayson.SESSION
token = Tayson.TG_BOT_TOKEN
sudo_command = [6094482545]
pm = "6094482545"
mention = Mody.MENTION
plugins = dict(root="plugins")
app = Client(via,api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client(elhyba,api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
