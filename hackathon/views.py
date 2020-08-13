from django.shortcuts import render
import sounddevice as sd
import soundfile as sf
from django.views.decorators.csrf import csrf_exempt
import base64
import speech_recognition as sr
import io
import os
import ntpath
import time as tine
from datetime import datetime, date, time, timedelta
import json
import subprocess
from gtts import gTTS
from playsound import playsound
from .lak_pickle import chatbot_response
from .tracker import track_shipment
from .rates import check_rates
from .text_speaker import text_speaker
new_list=''
rates_list=[]
query_rate = []
caught_tag = ''
var_rates=''
add_postal = False

r = sr.Recognizer()
# Create your views here.
def homepage(request):

    #
    # if request.method=='POST':
    #     samplerate = 44100  # Hertz
    #     duration = 3  # seconds
    #     filename = 'output.wav'
    #
    #     mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
    #                     channels=1, blocking=True)
    #     sf.write(filename, mydata, samplerate)


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
        global caught_tag
        img_st="new"
        img_st = (request.POST).get('captured_rec')
        now=datetime.now()
        date_str=('%s-%02d-%02d-%02d'%(now.date(),now.hour,now.minute,now.second))
        string_i_want=str('media/audios/'+date_str+'.webm')
        _, audio_name = ntpath.split(string_i_want)
        # for each in os.listdir('media/audios/'):
        #     if not each == audio_name:
        #         os.remove('media/audios/'+each)
        wav_file = open(string_i_want, "wb")
        decode_string = base64.b64decode(img_st)
        wav_file.write(decode_string)
        wav_c_file=str('media/audios/'+date_str+'.wav')
        command = str("ffmpeg -i "+string_i_want+" -ac 2 -f wav "+wav_c_file)
        subprocess.call(command, shell=True)
        r = sr.Recognizer()
        harvard = sr.AudioFile(wav_c_file)
        s_google=''
        with harvard as source:
           audio = r.record(source)
        var2=1
        try:
            s_google=r.recognize_google(audio)
        except Exception as e:
            s_google=e
            var2=0
        if var2 !=0:
            caught_tag,chat_response=chatbot_response(s_google)
        global var_rates
        global add_postal
        if caught_tag=="rates":
            var_rates='rates'
            add_postal = False

        if caught_tag=="Tracking" or caught_tag=="tracking":
            text_speaker(caught_tag,chat_response)
            global new_list
            new_list="Tracking"
            return render(request, 'auto_home.html')
        elif new_list =="Tracking":
            track_response=track_shipment(str(s_google))
            text_speaker("tracked",track_response)
            new_list=''
            return render(request, 'auto_home.html')
        elif var_rates=="rates" :
            global query_rate
            print('=========================================================================================')
            print(query_rate)
            print('==========================================================================================')
            if len(query_rate) == 0 and add_postal == False :
                text_speaker(s_google,'What is the senders postal code')
                add_postal = True
                # query_rate.append(s_google)hgjgjh
                return render(request, 'auto_home.html')
            elif len(query_rate) == 0 and add_postal == True :
                text_speaker(s_google,'What is the recipient postal code')
                # add_postal = True
                query_rate.append(s_google)
                return render(request, 'auto_home.html')
            elif len(query_rate) == 1:
                text_speaker(s_google, 'What is the weight of the package in pounds')
                query_rate.append(s_google)
                return render(request, 'auto_home.html')
            elif len(query_rate) == 2:
                # text_speaker(s_google, 'What is the weight of the package in pounds')
                query_rate.append(s_google)
                # return render(request, 'auto_home.html')
            # elif len(query_rate) == 3:
                rate = check_rates(query_rate[0],query_rate[1],query_rate[2])
                if type(rate) == float or type(rate) == int:
                    message_out = "The rate for delivering a " + str(query_rate[2]) + " pounds package from " + str(
                        query_rate[0]) + " to " + str(query_rate[1]) + " is " + str(rate) + " Dollors"
                else:
                    message_out = str(rate)

                query_rate = []
                var_rates = ''
                add_postal = False
                text_speaker(message_out,message_out)
                return render(request, 'auto_home.html')

            else:
                var_rates = ''
                add_postal = False
                query_rate = []
                text_speaker("invalid", "please enter a valid response")
                return render(request, 'auto_home.html')
        elif new_list =="Tracking":
            track_response=track_shipment(str(s_google))
            text_speaker("tracked",track_response)
            new_list=''
            return render(request, 'auto_home.html')
        elif caught_tag=="greeting" :
            text_speaker(s_google,chat_response)
            return render(request, 'auto_home.html')
        elif caught_tag=="goodbye" :
            text_speaker(caught_tag,chat_response)
            return render(request, 'auto_home.html')
        else:
            var_rates = ''
            add_postal = False
            text_speaker("invalid","please enter a valid response")
            return render(request, 'auto_home.html')




@csrf_exempt
def waiter(request):
    if request.method == 'GET':
        captured_rec = request.GET['captured_rec']
        # img_st = (request.POST).get('captured_rec')
        print("sleeping")
        tine.sleep(10)
        print("slept")
        return render(request, 'auto_home.html')
