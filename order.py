from pymongo import MongoClient
import time
# client = MongoClient("mongodb+srv://Berrykind:<password>@cluster0.z7rql.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
client=MongoClient('localhost', 27017)
db = client.get_database('Serving_Robot')

Order= db.Order

def CalNexts_id(self) :
    max = int()
    max = 0
    x = self.find().sort("o_s_id")
    for i in x:
        if i['o_s_id'] > max:
            max = i['o_s_id']
    return max + 1

i = int()

i = CalNexts_id(Order)
print(i)
# Order.insert_one({'o_s_id':i})
#o_s_id의미 :  order_s_id

Order.insert_one({
    "o_s_id":i,
    "table_no":2,
    "menu":[{
        "id":1,
        "name":"김치찌개",
        "count":1
    }]
})

