from pymongo import MongoClient
import RPi.GPIO as GPIO
import time

client = MongoClient("mongodb+srv://Berrykind:poseidon@cluster0.z7rql.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

def CalNexts_id(self) :
    max = 0
    x = self.find().sort("s_id")
    for i in x:
        if i['s_id'] > max:
            max = i['s_id']
    return max + 1

db = client.get_database('Serving_Robot')
Center = db.Center
i = int()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(17, GPIO.OUT)
p = GPIO.PWM(17, 100)

while True:
    try:
        button_state =GPIO.input(18)
        if button_state==False:
            print('Button ON')
            i = CalNexts_id(Center)
            data={'s_id' : i, 'table_no' : 1, 'sig' : 1, 'now_work' : 1}
            Center.insert_one(data)

            p.start(100)
            p.ChangeDutyCycle(90)

            p.ChangeFrequency(699)
            time.sleep(.2)
            p.ChangeFrequency(880)
            time.sleep(.3)

            p.stop()

    except KeyboardInterrupt:
        pass
        print('Exit with ^C. Goodbye!')
        GPIO.cleanup()
        exit()
