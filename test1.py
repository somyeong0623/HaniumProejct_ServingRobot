from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient
import datetime
client = MongoClient('localhost', 27017)

db = client.Serving_Robot
Robot=db.Robot
now=datetime.datetime.now()
print(datetime.datetime.now())
# now_work=1인 데이터 찾기
def GetValue(self, now_work, target):  # self에는 Collection, s_id에는 확인하고 싶은 s_id, target은 추출하고 싶은 데이터이름
    results = int()

    temp = self.find({'now_work': now_work})

    for j in temp:
        results = j[target]
        # 여기서 for문 인 이유 ??

    if results == 0:
        return 0
    else:
        return results

s_id = GetValue(Robot, 1, 's_id')
print(s_id)


# Time=db.Time
now=datetime.datetime.now()
# doc = {"time": now}
# Time.insert(doc)