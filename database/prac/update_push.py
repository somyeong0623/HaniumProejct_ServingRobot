# Working with mongoDB Atlas using Python
# 유툽 참고

from pymongo import MongoClient

# # client=MongoClient("mongodb+srv://somyeong:teentop0816@cluster0.dluuf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
client = MongoClient('localhost', 27017)
db = client.mydb
test = db.test

## doc안의 원소안에 리스트 추가하는 법

doc = {
    "o_s_id": 1,
    "table_no": 2,
    "menu": [{
        "id": 1,
        "name": "김치찌개",
        "count": 2
    }]
}
# db.menu.insert(doc)
# db.menu.update(
#     {"o_s_id":1},
#     {
#  "$push":{
#         "menu":[
#            {"id":3, "name":"짬뽕","count":1}
#         ]
#     }
# })
db.menu.update(
    {"o_s_id":1},
    {"$set":{"table_no":100}}
)

# db.menu.update(
#     {
#         "o_s_id": 1,
#         "menu": {"$elemMatch": {"name": "짬뽕"}}
#     },
#     {"menu.$.count": 10}
# )
