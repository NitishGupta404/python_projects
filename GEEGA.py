import speech_recognition as sr
import pyttsx3 as sp
import os
import webbrowser
import random
import requests
import json
import wikipedia
import datetime
from playsound import playsound
import  pywhatkit
import  pyjokes



engine = sp.init('sapi5')
voice = engine.getProperty('voices')
# print(voice)
engine.setProperty('voice', voice[1].id)

def takecomand():
    r = sr.Recognizer()
    # for index, name in enumerate(sr.Microphone.list_microphone_names()):
    #     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
    with sr.Microphone(device_index=0) as Source:
        print("Listening.....")
        sound()
        r.energy_threshold=600
        r.pause_threshold = 2
        audio = r.listen(Source)
        try:
            query= r.recognize_google(audio, language='eng-in')
            print(query)
        except :
            print("Please say that again.....")
            # speak("Please say that again.....")
            return "NONE"
        return query

def speak(given):
    engine.say(given)
    engine.runAndWait()

def sound():
    playsound('Listening.wav')



def wishme():
    hr = int(datetime.datetime.now().hour)
    if hr >=0 and hr<=12:
        speak("Good morning!")
    elif hr>12 and hr<=15:
        speak("Good afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Geega!,how may I help you!")


if __name__ == '__main__':
    wishme()
    while True:
        chromepath= r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        query=takecomand().lower()

        if "tell me about" in query:
            speak("Searching web...!")
            query=query.replace("tell me about" , "")
            try:
                res=wikipedia.summary(query , sentences=2)
                print(res)
                speak(res)
            except Exception as e:
                print("Please be more specific!")
                speak("Please be more specific!")

        elif "open youtube" in query:
                webbrowser.register('chrome' , None , webbrowser.BackgroundBrowser(chromepath))
                webbrowser.get('chrome').open("youtube.com")
        elif "open google" in query:
                webbrowser.register('chrome' , None , webbrowser.BackgroundBrowser(chromepath))
                webbrowser.get('chrome').open("google.com")

        elif "some news"  in query:
            r=requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=c9eefcf37899409587f88f7027573575").text
            news=json.loads(r)
            arts=news['articles']
            for index,item in enumerate(arts):
                if index==3:
                    break
                speak(item['title'])
                print(f"if you want to know more about news no.{index + 1} click on the link below")
                print(item['url'])

        elif "the time" in query:
            speak(datetime.datetime.now().strftime("%H:%M:%S"))

        elif "weather outside" in query:
            r=requests.get("http://api.openweathermap.org/data/2.5/weather?q=Kanpur&units=metric&appid=f0cecf94071ffaa59f21896b2d066e7f").text
            getweather=json.loads(r)
            main_weather =getweather["weather"][0]['main']
            des_weather = getweather["weather"][0]['description']
            temprature = getweather["main"]['temp']
            speak(f"the temprature outside is {temprature} degree celcius")
            speak(f"the weather outside is {main_weather}y  so it will be{des_weather}")

        # elif "air quality" in query:
        #     r=requests.get("https://api.breezometer.com/air-quality/v2/current-conditions?lat=26.449923&lon=80.331871&key=00d0914819f0495d9f32f9abeb162c7e").text
        #     aqi_data=json.loads(r)
        #     aqi1=aqi_data["data"]["indexes"]["baqi"]['aqi']
        #     aqi2 = aqi_data["data"]["indexes"]["baqi"]['category']
        #     speak(f" since the air quality index is {aqi1}! hence there is {aqi2}")

        elif "open photoshop" in query:
            try:
                os.startfile("C:\\Program Files\\Adobe\\Adobe.Photoshop.CC.20.0.6.Portable.x64\\PhotoshopPortable.exe")
            except Exception as e:
                speak("Some error occurred")

        elif "what can you do" in query:
            speak("I can give you weather information!...")
            speak("I can tell you time!...")
            speak("I can give you some news!...")
            speak("I can give you info about any thing on web!...")
            speak("I can open youtube!...")
            speak("I can open google!...")
            speak("I can open photoshop!...")

        elif "say hello"  in query:
            speak("Hello I am geega ! ...How are you?")

        elif "i'm fine" in query:
            speak("good to know!...")


        elif "toss a coin" in query:
            playsound('coinflip.mp3')
            coin =["head" , "tail"]
            cho= random.choice(coin)
            speak(f"its a..  {cho}")

        elif "advise me" in query:
            r=requests.get("https://api.adviceslip.com/advice").text
            advice=json.loads(r)
            advice_given=advice["slip"]['advice']
            speak(advice_given)
            pass

        elif "convert text" in query:
            speak("What text you want to convert to hand writing?")
            con_text=takecomand()
            pywhatkit.text_to_handwriting(con_text ,rgb=[0,0,255])

        elif "play" in query:
            song=query.replace("play" ," ")
            pywhatkit.playonyt(query)

        elif  "search" in query:
            g_search=query.replace("search" ," ")
            pywhatkit.search(g_search)

        elif "crack a joke" in query:
            speak(pyjokes.get_joke())

        elif "take notes" in query:
            speak("Please start dictating after beep")
            notes=takecomand()
            timestamp=datetime.datetime.now().strftime("%H:%M:%S")
            try:
                with open("notes.txt" ,"a") as f:
                    f.write(f"noted at {timestamp}\n")
                    f.write(f"{notes}\n")
            except Exception as e:
                speak("Something went wrong")
            speak("noted...")

        elif "open notes" in query:
            try:
                os.startfile("notes.txt")
            except :
                speak("Something went wrong")

        elif "read notes" in query:

            with open("notes.txt" ,"r") as f:
                content=f.read()
            if content == " ":
                speak("Notes are empty")
            else:
                speak(content)

        elif "meaning" in query:
            app_id = '098ea27b'
            app_key = '0b8204038ad730d7cf832d959a0349f4'
            language = 'en-us'
            fields = 'definitions'
            strictMatch = 'false'
            speak("please say the word")
            word_id =takecomand()

            try:
                url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;
                r=requests.get(url, headers = {'app_id': app_id, 'app_key': app_key}).text
                defin_data = json.loads(r)
                definition = defin_data["results"][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
                speak(definition)
                definition2 = defin_data["results"][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]['definitions'][0]
                speak(definition2)
                definition3 = defin_data["results"][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['definitions'][0]
                speak(definition3)
            except Exception as e:
                speak("could not find the word in oxford dictionary")

        elif "movie" in query:
            speak("speak the name of the movie/series after the sound")
            name = takecomand()

            r = requests.get(f"http://www.omdbapi.com/?t={name}&plot=full&apikey=a98c33eb").text

            moviedata = json.loads(r)
            # print(moviedata)
            try:
                m_name = moviedata['Title']
                speak(f"Title {m_name}")
            except:
                speak("Please check the spelling")
            try:
                m_release = moviedata['Released']
                speak(f"Release date {m_release}")
            except:
                speak("Not available")
            try:
                m_length = moviedata['Runtime']
                int_m_len = m_length.replace(" min", "")
                int_m_len = int(int_m_len)
                int_m_len = int_m_len / 60
                speak(f"Run time {int_m_len} hrs")

            except:
                speak("Not available")
            try:
                m_genre = moviedata['Genre']
                speak(f"Genre {m_genre}")
            except:
                speak("Not available")
            try:
                m_cast = moviedata['Actors']
                speak(f"Actors {m_cast}")
            except:
                speak("Not available")
            try:
                m_plot = moviedata['Plot']
                speak(f"Plot {m_plot}")
            except:
                speak("Not available")

            try:
                m_rating = moviedata['imdbRating']
                speak(f"Imdb rating {m_rating}")
            except:
                speak("Not available")

            try:
                pass
            except Exception as e:
                speak("no data found")

        else :
            if "sleep"  in query:
                speak("I am going to sleep")
                break


