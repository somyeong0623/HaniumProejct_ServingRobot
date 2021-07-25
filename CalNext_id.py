from pymongo import MongoClient

client=MongoClient('localhost', 27017)
db=client.Serving_Robot
Order = db.Order

def CalNexts_id(records) :                 # self에는 Colection이름이 들어가면 됩니다.
    max = int()
    max = 0
    x = records.find().sort("_id")
    # print(x[0])
    for i in x:
        if i['_id'] > max:
            max = i['_id']
    return max + 1

i = int()
i = CalNexts_id(Order)
db.Order.insert_one({'_id':i})

#초기에, collection에 아무런 insert를 하지 않았을 경우, CalNexts_id함수에서 for문을 돌지않기 때문에 1를 return 받음
#그러므로 주문번호를 1번부터 매길것이라면,  수동으로 s_id=0을 넣어주지 않아도 될것 같습니다.

# s_id를 1씩 증가시켜서 각각의 주문 건을 s_id를 통해 고유하게 구별할수 있다고 생각하는데
# 랜덤으로 부여되는 _id값이 필요하지않다고 생각되어서 _id값을 1부터 증가하게 함수를 수정해보았습니다.(이부분 의견 부탁드립니당)