import pyttsx3
speaker= pyttsx3.init()
text =input("Insert a text file: ")
speaker.say(text)
speaker.runAndWait()


