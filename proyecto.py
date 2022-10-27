import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices') #para cambiarle la voz
engine.setProperty('voice', voices[1].id) #tiene 2 voces posibles, 0 es masculina y 1 es femenina   

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:   # te deja ver errores en el codigo
        with sr.Microphone() as source:
            print('listening...') #para saber cuando te esta escuchando
            voice = listener.listen(source) #tenemos q hablar fuerte para q nos escuche
            command = listener.recognize_google(voice) #para que google te tire el texto    
            command = command.lower()
            if "alexa" in command:    #para q solo conteste en el caso q digan alexa
                command = command.replace('alexa', '') #saca alexa del texto, para q no lo diga
                print(command)
    except:   #te deja arreglar el error
        pass 
    return command

def run_alexa(): #para q ponga musica
    command = take_command()
    print(command)
    if 'play' in command: 
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song) #con esto escucho musica en youtube
    elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M') #en 24hs
            print(time)
            talk('Current time is ' + time)
            time = datetime.datetime.now().strftime('%I:%M %p') #en 12hs
            print(time)
            talk('Current time is ' + time)
    elif 'who is' in command: #para buscar en wikipedia
            person = command.replace('who is ', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else: #por si no te escucha o no te entiende
        talk('Please say the command again')

while True:
    run_alexa()      