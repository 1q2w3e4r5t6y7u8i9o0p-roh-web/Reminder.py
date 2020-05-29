import datetime
import pyttsx3

try:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()


    hour = int(input('Write hour\n'))
    minute = int(input('Wrte minute\n'))
    query = input('what do you want to be reminded of\n')

    speak('You\'l be reminded sir')

    while True:
        if (hour == datetime.datetime.now().hour and minute == datetime.datetime.now().minute):
            speak(f'sir its a reminder     {query}')
            print(query)
            break

except Exception as e:
    e = 'Invalid input'
    speak(e)
    print(e)

    quit()
