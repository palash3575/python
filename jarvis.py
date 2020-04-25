import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random




owner = 'palash'


os.chdir("/home")
print(os.getcwd())
#for speek function
engine =pyttsx3.init()
engine.setProperty('rate',120)
engine.setProperty('volume',0.3)
engine.setProperty('voice','english')
voices =engine.getProperty('voices')

def speek(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 1 and hour <= 6:
        speek('it is your slepping time so go to sleep immedietly ')
    elif hour >= 7 and hour <= 12:
        speek('good morning')
    elif hour >= 13 and hour <= 15: 
        speek('its noon and time to get ready for going TTC')
    elif hour >= 15 and hour <= 18:
        speek(f"good evening {owner}")
    elif hour >= 19 and hour <= 23:
        speek(f"good night {owner}")
    elif hour == 0:
        speek(f"It is high time to go to bed  {owner} go to bed immedietly lest you shold miss the salah of fazr")
    else:
        print(hour)
        speek('there might be some problem in your algorithm')
        print(hour)


# the wish me fungtion ends here 

def takeCommand():

    r = sr.Recognizer() 

    with sr.Microphone() as source:
        print('listening')
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print('recognizing....')
        query =r.recognize_google(audio , language='en-us')
        speek(query)
        print(f"you said : {query}\n")
		
		



    except Exception as e:
        print(e)    
        print('please say it again...')
        return 'none'
        return query


if __name__ == "__main__":
    wishMe()
    takeCommand()
    while True:
        #to take command by text input enable the following line
    #    query = input('ask your question....').lower()
        
        if 'wikipedia' in query:
            speek('searching in wikipedia ')
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query , sentences = 2)
            speek('according to wikipedia')
            print(results)
            speek(results)
        elif 'open youtube' in query:
            webbrowser.open_new_tab('https://www.youtube.com' )
            speek('opening youtube on default browser')

        elif 'open google' in query:
            webbrowser.open_new_tab('https://www.google.com' )
            speek('opening google')

        elif 'open facebook' in query:
            webbrowser.open_new_tab('https://www.facebook.com' )
            speek('opening facebook')
#play music on terminal bia mpg123 => terminal based audio player only for linux
        elif 'play music' in query:
            music_dir = '/home/palash/Music'
            songs = os.listdir(music_dir)
            rand = random.randrange(0 , len(songs))
            song = os.path.join(music_dir, songs[rand])
            print(song)
            os.popen(f'mpg123 {song}')
            speek('playing music')
        #for opening vs code    
        elif 'open vscode' in query:
            os.popen('code')
            speek('opening the last project of visula studio code please wait a moment')
#speak current time
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:S")
            speek(f"the time is {strTime}")

        elif 'open file manager' in query:
            os.popen('nautilus')
            speek('opening file manager please wait a moment')


        elif 'open blender' in query:
            os.popen('blender')
            speek('opening blender please wait a moment')

        elif 'exit' in query:
            speek(f"good bye {owner}")
            exit()
'''
        elif 'open file manager' in query:
            os.popen('nautilus')
            speek('opening file manager please wait a moment')

        elif 'open file manager' in query:
            os.popen('nautilus')
            speek('opening file manager please wait a moment')

        elif 'open file manager' in query:
            os.popen('nautilus')
            speek('opening file manager please wait a moment')

        elif 'open file manager' in query:
            os.popen('nautilus')
            speek('opening file manager please wait a moment')

        elif 'open file manager' in query:
            os.popen('nautilus')
            speek('opening file manager please wait a moment')


'''



            









