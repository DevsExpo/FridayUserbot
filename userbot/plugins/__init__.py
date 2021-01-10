from userbot import topfunc
from userbot.Configs import Config
from userbot.plugins import timefunc
from userbot.utils import friday_on_cmd
from var import Var

idgen = topfunc.id_generator
findnemo = topfunc.stark_finder
issudousing = Config.SUDO_USERS
islogokay = Config.PRIVATE_GROUP_ID
isdbfine = Var.DB_URI
isherokuokay = Var.HEROKU_APP_NAME
gdriveisshit = Config.AUTH_TOKEN_DATA
wttrapi = Config.OPEN_WEATHER_MAP_APPID
rmbg = Config.REM_BG_API_KEY
hmmok = Config.LYDIA_API
currentversion = "7.5"
if issudousing:
    amiusingsudo = "𝑨𝒄𝒕𝒊𝒗𝒆 ✓"
else:
    amiusingsudo = "𝑰𝒏𝒂𝒄𝒕𝒊𝒗𝒆 ✘"

if islogokay:
    logchat = "𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒆𝒅 ✓"
else:
    logchat = "𝑫𝒊𝒔𝒄𝒐𝒏𝒏𝒆𝒄𝒕𝒆𝒅 ✘"

if isherokuokay:
    riplife = "𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒆𝒅 ✓"
else:
    riplife = "𝑫𝒊𝒔𝒄𝒐𝒏𝒏𝒆𝒄𝒕𝒆𝒅 ✘"

if gdriveisshit:
    wearenoob = "𝑨𝒄𝒕𝒊𝒗𝒆 ✓"
else:
    wearenoob = "𝑰𝒏𝒂𝒄𝒕𝒊𝒗𝒆 ✘"

if rmbg:
    gendu = "𝑨𝒅𝒅𝒆𝒅 ✓"
else:
    gendu = "𝑵𝒐𝒕 𝒂𝒅𝒅𝒆𝒅 ✘"

if wttrapi:
    starknoobs = "𝑨𝒅𝒅𝒆𝒅 ✓"
else:
    starknoobs = "𝑵𝒐𝒕 𝒂𝒅𝒅𝒆𝒅 ✘"

if hmmok:
    meiko = "𝑨𝒅𝒅𝒆𝒅 ✓"
else:
    meiko = "𝑵𝒐𝒕 𝒂𝒅𝒅𝒆𝒅 ✘"

if isdbfine:
    dbstats = "𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒆𝒅 ✓"
else:
    dbstats = "𝑫𝒊𝒔𝒄𝒐𝒏𝒏𝒆𝒄𝒕𝒆𝒅 ✘"

inlinestats = (
    f"🏴‍☠ CɪᴘʜᴇʀX Ⲃⲟⲧ Ⲋⲧⲁⲧⲋ 🏴‍☠\n"
    f"ᴠᴇʀsɪᴏɴ = {currentversion} \n"
    f"ᴅᴀᴛᴀʙᴀsᴇ = {dbstats} \n"
    f"sᴜᴅᴏ = {amiusingsudo} \n"
    f"ʟᴏɢ-ᴄʜᴀᴛ = {logchat} \n"
    f"sᴇʀᴠᴇʀ = {riplife} \n"
    f"ɢ-ᴅʀɪᴠᴇ = {wearenoob}"
)
