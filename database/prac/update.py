#update연습

from pymongo import MongoClient

client=MongoClient('localhost', 27017)
db=client.mydb

# db.test2.update({"name":"Abet"},{"$set": {"age":20}})
# db.test2.update({"name":"Betty"},{"name":"Betty 2nd", "age":1})
# db.test2.update({"name":"David"},{"$unset":{"score":1}})
# db.test2.update({"name":"Elly"},{"$set":{"name":"Elly","age":"17"}},
#                 "$upsert"="true")
#criteria에 해당되는 document가 존재하지 않는다면 새로 추가하기

#여러 document의 특정 field수정
#age 20보다 낮거나 같은 doc의 score을 10으로 수정
# db.test2.update(
#     {"age":{"$lte":20}},
#     {"$set":{"score":10}},
#     {"multi":"true"}
# )

#배열에 값 추가
# #Charlie doc의 skills배열에 "angularjs"추가
# db.test2.update(
#     {"name":"Charlie"},
#     {"$push":{"skills":"angularjs"}}
# )

#배열에 값 여러개 추가 + 오름차순 정렬
# db.test2.update(
#     {"name":"Charlie"},
#     {"$push":{
#         "skills":{
#             "$each":["c++","java"],
#             "$sort":1
#         }
#     }}
# )

#배열에 값 제거하기
#Charli document에서 skills값의 mongodb 제거
# db.test2.update(
#     {"name":"Charlie"},
#     {"$pull":{"skils":"mongodb"}}
# )

#배열에서 값 여러개 제거
#Charlie document에서 skills 배열 중 "angularjs"와 "java"제거
db.test2.update(
    {"name":"Charlie"},
    {"$pull":{"skills":{"$in":["angularjs","java"]}}}
)