# FRIDAY

<p align="center">
<img src="Logo.jpeg" alt="FRIDAY">

Best User Bot To Manage Your Telegram Account 
## Most PowerFul And Better And Secure

## By Team #SᴛᴀʀᴋGᴀɴɢ™

### For any query or want to know how it works join Group And Channel 

<a href="https://t.me/FridaySupportOfficial"><img src="https://img.shields.io/badge/Join-Telegram%20Channel-red.svg?logo=Telegram"></a>
<a href="https://t.me/fridayOT"><img src="https://img.shields.io/badge/Join-Telegram%20Group-blue.svg?logo=telegram"></a>

## HOW TO DEPLOY 

I THANK INFOTEL FOR THIER FREE VIDEO SERVICE WATCH VIDEO ON HOW TO DEPLOY 

<a href="https://youtu.be/xfHcm_e92eQ"><img src="https://img.shields.io/badge/How%20To-Deploy-red.svg?logo=Youtube"></a>

## Installing Heroku 

### The Easy Way
[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/SHER321/fridayuserbot)

## GET STRING SESSION FROM REPL RUN 

[![Repl.it](https://img.shields.io/badge/REPL%20RUN-Run%20Online-blue.svg)](https://friday.starkgang.repl.run)

### The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/starkGang/Fridayuserbot
cd FridayUserbot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```


### UniBorg Configuration


The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.

