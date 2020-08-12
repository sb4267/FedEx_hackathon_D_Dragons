import subprocess

command = "ffmpeg -i ./2020-08-11-17-19-27.webm -ab 160k -ac 2 -ar 44100 -vn audio.wav"

subprocess.call(command, shell=True)
