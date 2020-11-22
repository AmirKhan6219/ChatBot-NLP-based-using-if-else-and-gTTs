# CHATBOT(NLP based using if-else and gTTs)
1. A chatbot is an artificial intelligence (AI) software that can simulate a conversation (or a chat) with a user in natural language through 
   messaging applications, websites, mobile apps or through the telephone.
2. Users communicate with these tools using a chat interface or via voice, just like they would converse with another person. Chatbots interpret the words given to them by a 
   person and provide a pre-set answer.
3. Example: Amazon Alexa, Google Assistant, Ernest, Buddy, etc.

# Libraries
1. SpeechRecognition
2. PyAudio
3. gTTs 
Google Text to Speech API commonly known as the gTTS API is a very easy to use tool which converts the text entered, into audio which can be saved as a mp3 file.
The gTTS API supports several languages including English, Hindi, Tamil, French, German and many more.

# Steps used in this project
# 1. Record the Audio and return it as String
     Recording is done using microphone and send to the google speech recognition engine to recognize the audio.
     Error occurs when google could not understand what was said, such as UnknownvalueError and RequestError. 
     
# 2. Convert the tetx into Audio
     gTTs is used to convert the text into audio by setting the language='English' and slow='False'.
     Here slow='False' means to speed-up.
     Save the coverted audio to a file named assistant_response.mp3.
     Play the converted file.
     
     
   



