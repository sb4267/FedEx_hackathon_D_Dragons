from django.shortcuts import render
import sounddevice as sd
import soundfile as sf
from django.views.decorators.csrf import csrf_exempt
import base64
import speech_recognition as sr
import io
import os
import ntpath
import time
from datetime import datetime, date, time, timedelta
import json
import subprocess
from gtts import gTTS
from playsound import playsound
from . import lak_pickle

r = sr.Recognizer()
# Create your views here.
def homepage(request):

    myobj = gTTS(text=s, lang='en', slow=False)
    myobj.save('media/fedaud/welcome.mp3')
    playsound('media/fedaud/welcome.mp3')


    if request.method=='POST':
        samplerate = 44100  # Hertz
        duration = 3  # seconds
        filename = 'output.wav'

        mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                        channels=1, blocking=True)
        sf.write(filename, mydata, samplerate)


    return render(request, 'auto_home.html')

def whatdidisay(request):

    harvard = sr.AudioFile('output.wav')
    with harvard as source:
       audio = r.record(source)

    s=r.recognize_google(audio)
    return render(request, 'homepage1.html',{'s':s})

@csrf_exempt
def pre_processor(request):
    if request.method == 'POST':
        img_st="new"
        img_st = (request.POST).get('captured_rec')
        now=datetime.now()
        date_str=('%s-%02d-%02d-%02d'%(now.date(),now.hour,now.minute,now.second))
        string_i_want=str('media/audios/'+date_str+'.webm')
        _, audio_name = ntpath.split(string_i_want)
        for each in os.listdir('media/audios/'):
            if not each == audio_name:
                os.remove('media/audios/'+each)
        wav_file = open(string_i_want, "wb")
        decode_string = base64.b64decode(img_st)
        wav_file.write(decode_string)
        # wav_c_file=str('media/audios/'+date_str+'.wav')
        # command = str("ffmpeg -i "+string_i_want+" -ac 2 -f wav "+wav_c_file)
        # subprocess.call(command, shell=True)
        # r = sr.Recognizer()
        # harvard = sr.AudioFile(wav_c_file)
        # s_google=''
        # with harvard as source:
        #    audio = r.record(source)
        # try:
        #     s_google=r.recognize_google(audio)
        # except Exception as e:
        #     s_google=e
        # # s_google="my_test_text"
        # data_pics = {}
        # data_pics['pictures'] = []
        # data_pics['pictures'].append({'path':str(s_google)})
        # with open('media/picture.json','w') as outfile:
        #     json.dump(data_pics, outfile)
        s_google="Hello"
        chat_response=chatbot_response(s_google)
        myobj = gTTS(text=chat_response, lang='en', slow=False)
        myobj.save('media/fedaud/welcome.mp3')
        playsound('media/fedaud/welcome.mp3')

    return render(request, 'auto_home.html')
