from mody import Tayson
from datetime import timezone, datetime, timedelta
from asyncio import sleep
from time import strftime
from config import *
from pyrogram.errors import FloodWait

user_name = Mody.USER_NAME

def zhrf_time(time):
  time = str(time)
  repl = ["𝟎","𝟏","𝟐","𝟑","𝟒","𝟓","𝟔","𝟕","𝟖","𝟗"]
  curn = ["0","1","2","3","4","5","6","7","8","9"]
  for i in range(0,10) :
    time = time.replace(curn[i],repl[i])
  return time

async def main():
   ay = None
   while r.get(f"{sudo_id}clockk") :
      time = datetime.now(tz=timezone(timedelta(hours=2))).strftime('%I:%M')
      my_name = r.get(f"{sudo_id}clockk")
      try:
         if ay != time:
            ay = time
            await app.update_profile(first_name=user_name ,last_name=f'{zhrf_time(time)}')
         else:
            await sleep(0)
      except FloodWait as e:
         await sleep(e.value)
         await sleep(7)
