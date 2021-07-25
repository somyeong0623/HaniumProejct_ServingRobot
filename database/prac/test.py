from pymongo import MongoClient

client=MongoClient('localhost', 27017)
db=client.mydb

doc={"_id":1, "age":18, "name":"somyeong" }
db.users.insert_one(doc)

# a=db.test.find().limit(3)
# c=db.test.find().skip(4)
# b=int()
# # for i in a:
# #     b=i['_id']
# #     print(i)
# #     print(b)
# #
# for i in c:
#     c_=i['_id']
#     print(i)
#     print(c_)