#Working with mongoDB Atlas using Python
#유툽 참고

from pymongo import MongoClient
# # client=MongoClient("mongodb+srv://somyeong:teentop0816@cluster0.dluuf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
client=MongoClient('localhost', 27017)
db=client.mydb
test=db.test

## doc안의 원소안에 리스트 추가하는 법

doc={
    "o_s_id":2,
    "table_no":2,
    "menu":""
}

# db.menu.insert(doc)
# db.menu.update(
#     {"o_s_id":1},
#     {
#  "$set":{
#         "menu":[
#            {"id":3, "name":"짬뽕","count":1}
#         ]
#     }
# })
# db.Order.update(
#         {"o_s_id":2},
#         {
#             "$set": {
#                 "menu": [
#                     {"name": "김치찌개", "count": 3},
#                     {"name": "전주비빔밥", "count": 5}
#                 ]
#             }
#         })
db.menu.update(
        {"o_s_id":2},
        {
            "$set": {
                "menu": [
                    {"name": "김치찌개", "count": 3},
                    {"name": "전주비빔밥", "count": 5}
                ]
            }
        })

## 음식 수량 조절했을때 Order의 menu의 count update 하는코드

