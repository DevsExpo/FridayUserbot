import os
from json import loads, JSONDecodeError
from fridaybot.Configs import Config
from googletrans import LANGUAGES
from google_trans_new import google_translator
import logging

k = logging.getLogger("TR-ENGINE")
lang = Config.LANG

async def tr_engine(event, text, parse_mode='md'):
    kk = Config.LANG if LANGUAGES.get(Config.LANG) else 'en'
    if kk == 'en':
        await event.edit(text, parse_mode=parse_mode)
    else:
        try:
            translator = google_translator()
            translated = translator.translate(text, lang_tgt=kk)
            hmm = translated
        except:
            hmm = text
    await event.edit(hmm, parse_mode=parse_mode)        
    return
