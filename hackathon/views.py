from django.shortcuts import render
import sounddevice as sd
import soundfile as sf
# Create your views here.
def homepage(request):
    if request.method=='POST':
        samplerate = 44100  # Hertz
        duration = 3  # seconds
        filename = 'output.wav'

        mydata = sd.rec(int(samplerate * duration), samplerate=samplerate,
                        channels=1, blocking=True)
        sf.write(filename, mydata, samplerate)


    return render(request, 'home1.html')

def whatdidisay(request):
    import speech_recognition as sr
    r = sr.Recognizer()
    harvard = sr.AudioFile('output.wav')
    with harvard as source:
       audio = r.record(source)

    s=r.recognize_google(audio)
    return render(request, 'homepage1.html',{'s':s})
