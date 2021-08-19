#호출벨 버튼 눌렀을때 가정해서 손님 호출
#
# from pymongo import MongoClient
# import RPi.GPIO as GPIO
# import time
from pymongo import MongoClient
# client = MongoClient("mongodb+srv://Berrykind:<password>@cluster0.z7rql.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
client = MongoClient('localhost', 27017)
db = client.Serving_Robot
Order = db.Order
Kitchen = db.Kitchen
Center = db.Center

def CalNexts_id(self) :
    max = int()
    max = 0
    x = self.find().sort("s_id")
    for i in x:
        if i['s_id'] > max:
            max = i['s_id']
    return max + 1


#
# GPIO.setmode(GPIO.BCM)
#
# GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)

i = int()
i = CalNexts_id(Center)
print(i)
state=True #버튼 누른상태
#state=False

if state==True:
    i=db.Center.count()+1
    data={'s_id':i, 'table_no':1, 'sig':1, 'now_work':1}
    Center.insert_one(data)

# while True:
#     try:
#         button_state =GPIO.input(18)
#         if button_state==False:
#             print('Button ON')
#             i = CalNexts_id(Center)
#             data={'s_id' : i, 'table_no' : 1, 'sig' : 1, 'now_work' : 1}
#             Center.insert_one(data)
#             time.sleep(0.2)
#
#     except KeyboardInterrupt:
#         pass
#         print('Exit with ^C. Goodbye!')
#         GPIO.cleanup()
#         exit()
