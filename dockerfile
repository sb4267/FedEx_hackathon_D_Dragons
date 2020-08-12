FROM tensorflow/tensorflow:latest-py3

ENV PYTHONUNBUFFERED 1
RUN pip uninstall keras
RUN pip install keras==2.1.2
RUN python -m pip install --upgrade pip
RUN pip install tensorflow
ENV PYTHONUNBUFFERED 1

RUN mkdir /new_app

WORKDIR /new_app

ADD . /new_app/

RUN apt-get update && apt-get install -y vim && apt-get install -y libportaudio2 && apt-get install -y libsndfile1 && apt-get install -y ffmpeg
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN pip uninstall portaudio

CMD python manage.py runserver 0.0.0.0:$PORT
