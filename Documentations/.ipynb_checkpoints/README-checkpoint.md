<h1>Fedex Voice Assistant</h1>


<b>Business Value:</b> Our goal is to enhance the interaction of the users with the services provided by FedEx. We want to increase the ways users can use your services, faster and easier. Rather than using the services in a browser, we let the users interact with the services directly using their voice.

<b>Technical Innovation:</b> A voice assistant is a digital assistant that uses voice recognition, speech synthesis, and natural language processing (NLP) to provide a service through a particular application. We have used this to create a basic voice assistant application that can take your voice inputs and provide back with the correct information through voice.

<b>Business implementation:</b> This application is designed in Python, Django, and deployed in Heroku. It uses Tracking and Rates API's from FedEx portal and provides the information to the users. The roadmap to production requires customizing the application to a specific set of rules and connecting with various API's as required.

Watch the overview video...


<h2>Overview</h2>

Many devices we use every day utilize voice assistants. They’re on our smartphones and inside smart speakers in our homes. Many mobile apps and operating systems use them. Additionally, certain technology in cars, as well as in retail, education, healthcare, and telecommunications environments, can be operated by voices.

People try to check for a lot of Business directly using their voice assistants to check if this feature is available or not? Currently, the customer or a Business user needs to go into the FedEx website and navigate to the services to get some basic information on Tracking or checking for rates of delivery from one place to another. If we can automate that process and provide a way to the customers that they can use the voice assistants to do this for them, we will succeed in enhancing their experience.

Similar to the chat assistant FedEx website already have, we need to deploy the voice assistant which connects to the APIs and provides the details to the customer. We should be using these APIs to interact with some of the existing voice assistants like Google Assistant, Siri, Cortana, Alexa, etc.


<h2>The App Demo</h2>

The app is written using the Django framework. We created two versions of the app. One uses Keras, Tensorflow framework and another uses NLTK in python for text processing.

[![alt text] (https://github.com/sb4267/FedEx_hackathon_D_Dragons/blob/master/Documentations/screenshot.png](https://github.com/sb4267/FedEx_hackathon_D_Dragons/blob/master/Documentations/FedEx%20Hackathon%20Demo_D%20Dragons.mp4)

<h2>The Design</h2>

This app uses the Django framework and it communicates with the two FedEx APIs. We have implemented this as a Python/Django app, running in Heroku. The data pipeline receives real-time voice data from the user, which it converts to text and tokenize the sentences, Lemmatize, create the bag of words, and calculate the similarity of the words in the query, connect to the respective API, get the response and convert back to the voice and sends to the customer.

![alt text](https://github.com/sb4267/FedEx_hackathon_sb4267/blob/master/Documentations/Architecture_diagram.png)
<h2>The Data Pipeline</h2>

The data pipeline is written in Python and deployed as a Django app running in Heroku Web App. The data pipeline reads raw text file we created for basic responses and uses python text processing to take voice inputs, conversion of voice to text,  tokenize, Lemmatize, create the bag of words, and calculate the similarity of the words in the query, connect to the respective API, get the response and convert back to the voice.


<h2>Important Links</h2>

+ Git Hub: https://github.com/sb4267/FedEx_hackathon_sb4267
+ Heroku(free tier) web app launched: https://myfed17snd.herokuapp.com/
+ Azure : https://fedexhackathon.azurewebsites.net/

+ Fedex API list
    + checking rates: https://apis-sandbox.fedex.com/rate/v1/rates/quotes
    + Tracking a package: https://apis-sandbox.fedex.com/track/v1/trackingnumbers

+ PPT Presentation
    + https://github.com/sb4267/FedEx_hackathon_sb4267/blob/master/Documentations/Fedex%20Presentation.pptx
    
+ Instructions to execute the project
    + install the required packages from requirements.txt
    + in the terminal/command prompt for the home directory where the file manage.py file is present
    + run the following command
    + python manage.py runserver
    + it would show a usual destination file with local host similar to this (http://127.0.0.1:8000/)
    