from pymongo import MongoClient

client=MongoClient('localhost', 27017)
db=client.prac


# db.users.insert_one({'name': '덤블도어', 'age': 116})
# db.users.insert_one({'name': '맥고나걸', 'age': 85})
# db.users.insert_one({'name': '스네이프', 'age': 60})
# db.users.insert_one({'name': '해리', 'age': 40})
# db.users.insert_one({'name': '허마이오니', 'age': 40})
# db.users.insert_one({'name': '론', 'age': 40})



# print(all_users[0])
# print(all_users[0]['name'])
#
# for user in all_users:
#     print(user)

##### mongoDb에 저장된 특정값 조회하기 : READ
same_ages=list(db.users.find({'age':40}))

# for user in same_ages:
#     print(user)

## Update
db.users.update_one({'name':'덤블도어'}, {'$set':{'age':19}})
all_users=list(db.users.find({},{'_id':False}))

for user in all_users:
    print(user)




# <----------id값 1씩 증가시킴 ----------->
# db=client.prac
# user2=db.prac
#
# def CalNexts_id(user2) :                 # self에는 Colection이름이 들어가면 됩니다.
#     max = int()
#     max = 0
#     x = user2.find().sort("s_id")
#     for i in x:
#         if i['s_id'] > max:
#             max = i['s_id']
#     return max + 1
#
# #사용예시 (마지막 s_id가 2인 경우)
#
# i = int()
#
# i = CalNexts_id(user2)
# db.user2.insert_one({'s_id':i})          # s_id가 3인 데이터가 입력됩니다.
