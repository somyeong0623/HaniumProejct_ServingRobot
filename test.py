from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient
import datetime

# aws 접속용
# client = MongoClient('mongodb://test:test@13.125.65.160', 27017)
# 로컬 접속용
client = MongoClient('localhost', 27017)

db = client.Serving_Robot
Order = db.Order
Kitchen = db.Kitchen
Center = db.Center
Robot = db.Robot
MenuList = db.MenuList
MenuList_max = db.MenuList_max
MenuList_min = db.MenuList_min

a = datetime.datetime.now()
print(a)


def CalNexts_o_id(self):  # self에는 Colection이름이 들어가면 됩니다.
    max = int()
    max = 0
    x = self.find().sort("o_id")
    for j in x:
        if j['o_id'] > max:
            max = j['o_id']
    return max + 1


dic_name = {0: "전주비빔밥", 1: "뚝배기불고기", 2: "김치찌개", 3: "된장찌개",
            4: "짜장면", 5: "짬뽕", 6: "탕수육", 7: "볶음밥",
            8: "토마토파스타", 9: "함박스테이크", 10: "오므라이스", 11: "페퍼로니피자",
            12: "등심돈까스", 13: "오코노미야끼", 14: "가츠동", 15: "모듬초밥(10p)"}

dic_count = {0: 0, 1: 0, 2: 0, 3: 0,
             4: 0, 5: 0, 6: 0, 7: 0,
             8: 0, 9: 0, 10: 0, 11: 0,
             12: 0, 13: 0, 14: 0, 15: 0}

dic_price = {0: 7000, 1: 8000, 2: 6500, 3: 6500,
             4: 7000, 5: 7000, 6: 8000, 7: 7000,
             8: 8000, 9: 9000, 10: 8000, 11: 10000,
             12: 8000, 13: 7000, 14: 7000, 15: 8000}

dic_total_price = {0: 0, 1: 0, 2: 0, 3: 0,
                   4: 0, 5: 0, 6: 0, 7: 0,
                   8: 0, 9: 0, 10: 0, 11: 0,
                   12: 0, 13: 0, 14: 0, 15: 0}


def CountMenu(collection):
    x = collection.find().sort("o_id")
    for i in x:
        for j in i['menu']:
            id = j['id']
            name = j['name']
            count = int(j['count'])
            print(id, name, count)
            dic_count[id] = dic_count[id] + count
            dic_total_price[id] = dic_price[id] * dic_count[id]


db.MenuList.drop()
CountMenu(Order)
# print(dic_count)
# print(dic_total_price)

# for i in range(0,16):
#     print(i,dic_name[i],dic_count[i],dic_total_price[i])
#     doc = {
#         'm_id': i,
#         'menu_name': dic_name[i],
#         'menu_count':dic_count[i],
#         'menu_total_price': dic_total_price[i]
#     }
#     MenuList.insert(doc)

# 최다 판매 메뉴
max = 0
max_index = 0
for i in range(0, 16):
    if max < dic_count[i]:
        max = dic_count[i]
        max_index = i
print("최다 판매 메뉴: ", dic_name[max_index], dic_count[max_index], dic_total_price[max_index])

for i in range(0, 16):
    if max == dic_count[i]:
        doc = {
            'm_id': i,
            'menu_name': dic_name[i],
            'menu_count': dic_count[i],
            'menu_total_price': dic_total_price[i]
        }
        MenuList_max.insert(doc)

# 최소 판매 메뉴
min = 10000
min_index = 0
for i in range(0, 16):
    if dic_count[i]!=0:
        if min > dic_count[i]:
            min = dic_count[i]
            min_index = i
print("최소 판매 메뉴: ", dic_name[min_index], dic_count[min_index], dic_total_price[min_index])

for i in range(0, 16):
    if min == dic_count[i]:
        doc = {
            'm_id': i,
            'menu_name': dic_name[i],
            'menu_count': dic_count[i],
            'menu_total_price': dic_total_price[i]
        }
        MenuList_min.insert(doc)

## 총 매출액
# total_price=0
# for i in range(0,16):
#     total_price=total_price+dic_total_price[i]
# print(total_price)

# max_menu=""
# max=0
# max_index=0
# for i in range(0,16):
#     if max<dic_count[i]:
#         max=dic_count[i]
#         max_name=dic_name[i]
#
# print(max_name)
