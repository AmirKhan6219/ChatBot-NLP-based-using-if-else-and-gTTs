# CHATBOT(NLP based using if-else and gTTs)
  1. A chatbot is an artificial intelligence (AI) software that can simulate a conversation (or a chat) with a user in natural language through 
     messaging applications, websites, mobile apps, or through the telephone.
  2. Users communicate with these tools using a chat interface or via voice, just like they would converse with another person. Chatbots interpret the words given to them by a 
     person and provide a pre-set answer.
  3. Example: Amazon Alexa, Google Assistant, Ernest, Buddy, etc.

# Libraries
  1. SpeechRecognition
  2. PyAudio
  3. gTTs 

  Google Text to Speech API commonly known as the gTTS API is a very easy-to-use tool which converts the text entered, into audio which can be saved as an mp3 file.
  The gTTS API supports several languages including English, Hindi, Tamil, French, German, and many more.

# Steps used in this project
# 1. Record the Audio and return it as String
     A recording is done using a microphone and sends to the Google speech recognition engine to recognize the audio.
     An error occurs when google could not understand what was said, such as UnknownvalueError and RequestError. 

# 2. Convert the text into Audio
     gTTs is used to convert the text into audio by setting the language='English' and slow='False'.
     Here slow='False' means to speed-up.
     Save the converted audio to a file named assistant_response.mp3.
     Play the converted file.

# 3. Wake words or phrase
     A list of wakes words is provided in ordered to wake the 'bot' such as Hey Bot, Hi Bot, etc.
     Returning True when the user said the wake words else False.

# 4. Get the date
     Get the current date based on the user input by using the DateTime function.
     
# 5. Return random greeting response
     return a randomly chosen response, if the user input is a greeting.
     greeting input as 'hey', 'hi'.
     Randomly Response as 'hello', 'hey there'.

# 6. Get the answer about the person and also the city name asked by the user
     Get the answer from Wikipedia which was asked from the user.
     Example1 : Who is Virat Kohali?
     Example2 : Where is Mumbai city?
     Wikipedia will search it and return.

# 7. Check conditions if wake word is True
     If Wake Word is True,
     Repeats steps based on the user input text and check all the conditions

# Technologies used
  1. Python
  2. Machine Learning
