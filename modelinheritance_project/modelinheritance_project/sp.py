import speech_recognition as sr
import gtts,os
from translate import Translator

r=sr.Recognizer()

with sr.Microphone() as source:

    print("SPEAK SOMETHING")
    audio = r.listen(source)
    t=r.recognize_google(audio)
    print("you said :" ,format(t))
    print("TIME'S UP..........THANKS")

    print(" PLEASE ENTER 1.telugu,2.hindi,3.tamil,4.kannada,5.malaylam ")
    ch = float(input("Enter a your choice: "))
    if ch == 1:

        text = r.recognize_google(audio)
        translator = Translator(from_lang="en", to_lang="te")
        translation = translator.translate(text)

        #print("you said :", format(text))


    elif ch == 2:
        text = r.recognize_google(audio, language='hi-in')
        print("you said :", format(text))
    elif ch == 3:
        text = r.recognize_google(audio, language='ta')
        print("you said :", format(text))
    elif ch == 4:
        text = r.recognize_google(audio, language='kn')
        print("you said :", format(text))
    elif ch == 5:
        text = r.recognize_google(audio, language='ml')
        print("you said :", format(text))




    else:
        print(" SORRY ,PLEASE PICK FORM THE GIVEN OPTIONS ")