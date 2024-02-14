import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error fetching results; {0}".format(e))

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    if sptext() == "bixby":
        while True:
            data1 = sptext()

            if "your name" in data1:
                name ="My name is Bixby "
                speechtx(name)

            elif "old are you" in data1:
                 age = " I am one year old"
                 speechtx(age) 

            elif "time" in data1: 
                time = datetime.datetime.now().strftime("%I%M%p")  
                speechtx(time)

            elif 'youtube' in data1: 
            # webbrowser.set_url("http://www.youtube.com/search")
                url = "http://www.youtube.com/"
                webbrowser.open(url)
            
            elif 'pw gate' in data1: 
            # webbrowser.set_url("http://www.youtube.com/search")
                 url = "https://www.pw.live/study/batches/study"
                 webbrowser.open(url)    

            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                print(joke_1)
                speechtx(joke_1)

            # elif 'play song' in data1:
            #     add=
            #     listsong = os.listdir(add)
            #     print(listsong)
            #     os.startfile(os.path.join(add,listsong[0]))     

            elif "exit" in data1: 
                speechtx("thankyou")
                break 
            time.sleep(5)  

    else:
        print("thanks")