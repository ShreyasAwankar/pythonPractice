import pyttsx3
from datetime import datetime
import time

speaker = pyttsx3.init()
def Alarm(alarmtype,stopper):
    for i in range (1,5):
        speaker.say(alarmtype)
        speaker.runAndWait()
        time.sleep(5)
        inp = input()
        if inp == stopper:
            break

def log(Entry):
    with open ("Routine_logs.txt", "a") as f:
        f.write(f"{Entry}, {datetime.now()}\n")

waterTime = time.time()
miniBreakTime = time.time()
exBrakeTime = time.time()

water_interval = 10
miniBreak_interval = 30
exBreak_interval = 60

waterAlarm = "Time to drink the water..."
miniBreakAlarm = "Take a mini break."
exAlarm = "Exercise Time."

while True:
    if time.time() - waterTime > water_interval:
        print ("Water drinking time...!")
        Alarm(waterAlarm,"drank")
        waterTime = time.time()
        log("Drank water at")

    if time.time() - miniBreakTime > miniBreak_interval:
        print ("Do some eye exercise...")
        Alarm(miniBreakAlarm,"done")
        miniBreakTime = time.time()
        log("Eye exercise done at")

    if time.time() - exBrakeTime > exBreak_interval:
        print ("Strech out or exercise and refresh yourself")
        Alarm(exAlarm,"exdone")
        exBrakeTime = time.time()
        log("Exercise done at")












