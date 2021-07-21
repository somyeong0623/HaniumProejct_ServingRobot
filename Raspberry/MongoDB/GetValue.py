from pymongo import MongoClient

client = MongoClient("mongodb+srv://Berrykind:<password>@cluster0.z7rql.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.get_database('student_db')
records = db.student_records

def GetValue(self, s_id, target) :              # self에는 Collection, s_id에는 확인하고 싶은 s_id, target은 추출하고 싶은 데이터이름
    results = int()

    temp = self.find({'s_id':s_id})

    for j in temp :
        results = j[target]

    if results == 0 :
        return 0
    else :
        return results

# 사용예시 s_id 3일 때 table_no가 5, s_id 3일 때 sig가 0이면

i = int()
j = int()

i = GetValue(records, 3, 'table_no')
j = GetValue(records, 3, 'sig')

print(i)
print(j)