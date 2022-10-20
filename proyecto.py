import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('I am your Alexa') #Para q hable cuando empieza el programa
engine.say('what can i do for you?')
engine.runAndWait()
try:   # te deja ver errores en el codigo
    with sr.Microphone() as source:
        print('listening...') #para saber cuando te esta escuchando
        voice = listener.listen(source) #tenemos q hablar fuerte para q nos escuche
        command = listener.recognize_google(voice) #para que google te tire el texto    
        command = command.lower()
        if "alexa" in command:    #para q solo conteste en el caso q digan alexa
            print(command)
except:   #te deja arreglar el error
    pass 