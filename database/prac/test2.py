#Working with mongoDB Atlas using Python
#유툽 참고

from pymongo import MongoClient
# # client=MongoClient("mongodb+srv://somyeong:teentop0816@cluster0.dluuf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
client=MongoClient('localhost', 27017)
db=client.mydb
test=db.test

#
# doc=[
#     { "name": "Abet", "age": 19 },
#     { "name": "Betty", "age": 20 },
#     { "name": "Charlie", "age": 23, "skills": [ "mongodb", "nodejs"] },
#     { "name": "David", "age": 23, "score": 20 }
# ]
# db.people.insert(doc)

doc={
    "o_s_id":1,
    "table_no":2,
    "menu":[{
        "id":1,
        "name":"김치찌개",
        "count":2
    }]
}
# db.menu.insert(doc)
db.menu.update(
    {"o_s_id":1},
    {
 "$push":{
        "menu":[
           {"id":3, "name":"짬뽕","count":1}
        ]
    }
})

