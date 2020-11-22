#Import the libraries
import os
import speech_recognition as sr
import datetime
import warnings
import calendar
import random
import wikipedia
import warnings
from gtts import gTTS

#Ignore Any type of warning
warnings.filterwarnings('ignore')

#Record audio and return it as string
def recordAudio():
    #Record the Audio
    rec= sr.Recognizer() #creating a Recognizer object

    #open the microphone and start recording
    with sr.Microphone() as source:
        print('Please Say Something...')
        audio= rec.listen(source) #listens for the user's input

    #Use Google speech recognition
    data=''
    try:
        data= rec.recognize_google(audio) #Recognize the audio
        print('You said: ' + data)

    #Error occurs when google could not understand what was said
    except sr.UnknownValueError: #Check for Unknown error
        print('Unknown Error: Googe Speech Recognition could not understand the audio')
    except sr.RequestError as e: #Check for Request error
        print('Request result from Google Speech Recognition service error'+ e)

    return data

# A Funtion to convert the text into audio
def assistantResponse(text):
    print(text)

    #Convert the Text to speech
    obj= gTTS(text= text, lang='en', slow= False)

    #Save the coverted audio to a file
    obj.save('assistant_response.mp3')

    #Play the converted file
    os.system('start assistant_response.mp3')

# A function for wake words or phrase
def wakeWord(text):
    Wake_Words=['hey alpha', 'hi alpha'] #A list of wake words

    text = text.lower() #Convert text in lower case to compare with Wake Words as they are in lower case

    #Check to see if the user command/text contains a wake word/phrase
    for phrase in Wake_Words:
        if phrase in text:
            return True
    #If wake is not found in the text from loop so return false
    return False

#A Function to get the current date
def getDate():
    now= datetime.datetime.now()
    my_date= datetime.datetime.today()
    weekday= calendar.day_name[my_date.weekday()] #eg. Friday
    monthNum= now.month
    dayNum= now.day

    #A list of months
    month_name= ['Janvary', 'Fabriary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                 'November', 'December']

    #A list of ordinal Numbers
    ordinalNumbers= ['1st', '2nd', '3rd', '4rh', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                     '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21th', '22th', '23th', '24th', '25th',
                     '26th', '27th', '28th', '29th', '30th', '31th']
    return  'Today is ' +weekday + ' the ' + ordinalNumbers[dayNum-1] + ' ' +  month_name[monthNum-1] + '.'

#A function to return a random greeting response
def greeting(text):
    #Greeting inputs
    Greetings_inp= ['hi', 'hey', 'greetings', 'wassup', 'hello']

    #Greeting_resonses
    Greeting_Responses= ['hello', 'hey there']

    # if the user input is greeting, then return a randomly chosen response
    for word in text.split():
        if word.lower() in Greetings_inp:
            return random.choice(Greeting_Responses) #Choosing randomly any resonse from the list 'Greeting_Response'

    #If no greeting was detected then return an empty string
    return ''

#A function to get the answer about the person asked by the user eg. Who is Virat Kohli
def getPerson(text):
    wordList= text.split() #Spliting the text into a list of words
    for i in range(0, len(wordList)):
        #A Check to Compare the first word with 'who' and the next word with 'is'.
        #If true, return the person's first name and person's last name
        if i+3 <= len(wordList)-1 and wordList[i].lower()=='who' and wordList[i+1].lower()=='is':
            #Returning the person's first and last name
            return wordList[i+2] + ' ' + wordList[i+3]

while True:

    #Record the Audio
    text= recordAudio()
    response= ''
    #Check for the Wake words/hrase
    if(wakeWord(text)==True):
        #Check for greetings by the users
        response= response+ greeting(text)

        #Check to see if the user said anything having to do with the date
        if('date' in text):
            get_date= getDate()
            response= response+ ' ' +get_date

        # Check to see if the user said anything having to do with the time
        if ('time' in text):
            now= datetime.datetime.now()
            meridiem= ''
            if now.hour >= 12:
                meridiem= 'PM' # Post Meriem (PM) after mid-day
                hour= now.hour-12
            else:
                meridiem= 'AM' #Ante Meridiem (AM) before mid-day
                hour= now.hour

            #Convert minute into a proper string
            if now.minute<10:
                minute= '0' + str(now.minute)
            else:
                minute= str(now.minute)

            response= response + ' ' + 'it is '+str(hour)+ ':' + minute+ ' '+ meridiem+' .'

        #Check to see if the user said 'who is'
        if('who is' in text):
            person= getPerson(text)
            #finding result from the search
            #sentences=2 get the 2 sentances from wikipedia
            wiki= wikipedia.summary(person, sentences=2)
            response= response+ ' ' + wiki

        if('how are you' in text):
            response= response+ ' Its been a good day. Whats about you?'

        if ('what is your name' in text):
            response = response + ' My name is Alpha'

        if ('who has created you' in text):
            response = response + ' I am created by amir khan who is a student of Lovely Professional University, Jalandhar, Punjab'

        #Have the assistant response back using audio and the text from response
        assistantResponse(response)

