#Working with mongoDB Atlas using Python
#유툽 참고

from pymongo import MongoClient
# # client=MongoClient("mongodb+srv://somyeong:teentop0816@cluster0.dluuf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
client=MongoClient('localhost', 27017)
db=client.Serving_Robot
Robot=db.Robot
Center=db.Center


def GetValue(self,_id, target) :              # self에는 Collection, s_id에는 확인하고 싶은 s_id, target은 추출하고 싶은 데이터이름
    results = int()

    temp = self.find({'_id':_id})

    for j in temp :
        results = j[target]
        #여기서 for문 인 이유 ??

    if results == 0 :
        return 0
    else :
        return results

index=int()
index=1
for i in range(1,10):
    cur_id = GetValue(Center, index, "_id")
    print(cur_id)
    index+=1

x=Center.find.sort("_id")
print(x)
