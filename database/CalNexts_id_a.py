from pymongo import MongoClient

# client = MongoClient("mongodb+srv://Berrykind:<password>@cluster0.z7rql.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
client=MongoClient('localhost', 27017)
db=client.Serving_Robot
Kitchen=db.kitchen

def CalNexts_id(self) :                 # self에는 Colection이름이 들어가면 됩니다.
    max = int()
    max = 0
    x = self.find().sort("s_id")
    for i in x:
        if i['s_id'] > max:
            max = i['s_id']
    return max + 1

#사용예시 (마지막 s_id가 2인 경우)

i = int()

i = CalNexts_id(Kitchen)

Kitchen.insert_one({'s_id':i})          # s_id가 3인 데이터가 입력됩니다.
