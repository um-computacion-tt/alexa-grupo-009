import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) 
recalling = []

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try: 
        with sr.Microphone() as source:
            talk('listening...') 
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice) 
            command = command.lower()
            if "alexa" in command:    
                command = command.replace('alexa', '') 
    except:   
        pass 
    return command

def run_alexa(): 
    command = take_command()
    print(command)
    recalling.append(command)

    if 'play' in command:                                           
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:                                          
            time = datetime.datetime.now().strftime('%H:%M') 
            print(time)
            talk('Current time is ' + time)
            #time = datetime.datetime.now().strftime('%I:%M %p') 
            #print(time)
            #talk('Current time is ' + time)
    elif 'who is' in command: 
            person = command.replace('who is ', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'who are you' in command:
        talk('i am your personal virtual assistand')
    elif 'where is' in command:
            place = command.replace ('where is', '')
            info = wikipedia.summary(place,1)
            print(info)
            talk(info)
    elif 'goodbye' in command:
        pass
    elif 'function' in command:
        print('i have the following function: ')
        talk('i have the following function: ')
        print('for every function to work you have to say alexa first, and then the command')
        talk('for every function to work you have to say alexa first, and then the command')
        print('for looking videos in youtube you say the command "play" ')
        talk('for looking videos in youtube you say the command "play" ')
        print('for the time you say the command "time" ')
        talk('for the time you say the command "time" ')
        print('for looking a short description of a person you say the command "who is" ')
        talk('for looking a short description of a person you say the command "who is" ')
        print('for looking for a place, like a country or a city you say the command "where is" ')
        talk('for looking for a place, like a country or a city you say the command "where is" ')
        print('if you want me to tell you a joke you say the command "joke" ')
        talk('if you want me to tell you a joke you say the command "joke" ')
        print('if you want to know who i am you say the command "who are you" ')
        talk('if you want to know who i am you say the command "who are you" ')
        print('if you do not want to continue talking to me you say the command "goodbye" ')
        talk('if you do not want to continue talking to me you say the command "goodbye" ')        
    else: 
        talk('Please say the command again') 

while True:
    run_alexa()
    if 'goodbye' in recalling[-1]:
        break
    elif 'play' in recalling[-1]:
        break