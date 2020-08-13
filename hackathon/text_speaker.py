from gtts import gTTS
import base64
import io
import os
import ntpath
import time as tine
from datetime import datetime, date, time, timedelta
import json

def text_speaker(s_google,chat_response):
    
    now=datetime.now()
    date_str=('%s-%02d-%02d-%02d'%(now.date(),now.hour,now.minute,now.second))
    file_name_destination='media/fedaud/'+date_str+'.mp3'
    audio_name = date_str+'.mp3'
    #for each in os.listdir('media/fedaud/'):
    #    if each != audio_name:
    #        os.remove('media/fedaud/'+each)
    myobj = gTTS(text=chat_response, lang='en', slow=False)
    myobj.save(file_name_destination)
    data_pics = {}
    data_pics['pictures'] = []
    data_pics['pictures'].append({'path':str(s_google),'resp_aud':file_name_destination,'resp_txt':chat_response})
    with open('media/picture.json','w') as outfile:
        json.dump(data_pics, outfile)
    return
