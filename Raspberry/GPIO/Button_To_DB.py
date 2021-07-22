from pymongo import MongoClient
import RPi.GPIO as GPIO
import time

client = MongoClient("mongodb+srv://Berrykind:poseidon@cluster0.z7rql.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

def CalNexts_id(self) :
    max = int()
    max = 0
    x = self.find().sort("s_id")
    for i in x:
        if i['s_id'] > max:
            max = i['s_id']
    return max + 1

db = client.get_database('Serving_Robot')
Center = db.Center
i = int()

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    try:
        button_state =GPIO.input(18)
        if button_state==False:
            print('Button ON')
            i = CalNexts_id(Center)
            data={'s_id' : i, 'table_no' : 1, 'sig' : 1, 'now_work' : 1}
            Center.insert_one(data)
            time.sleep(0.2)

    except KeyboardInterrupt:
        pass
        print('Exit with ^C. Goodbye!')
        GPIO.cleanup()
        exit()