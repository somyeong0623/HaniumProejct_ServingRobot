from pymongo import MongoClient

client = MongoClient("mongodb+srv://Berrykind:<password>@cluster0.z7rql.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.get_database('student_db')
records = db.student_records


def GetValue(self, s_id, target):
    results = int()

    temp = self.find({'s_id': s_id})

    for j in temp:
        results = j[target]

    if results == 0:
        return 0
    else:
        return results

# 뒤에 쌓인 호출 데이터 확인
def GoToServing(now_r_s_id) :
    r_s_id = now_r_s_id + 1
    r_data = {'s_id': r_s_id, 'table_no': GetValue(Center, r_s_id, 'table_no'),
            'sig': GetValue(Center, r_s_id, 'sig'), 'now_work': GetValue(Center, r_s_id, 'now_work')}
    Robot.insert_one(r_data)

    while GetValue(Robot, r_s_id, 'sig'):
        print('Order Wait', r_s_id, 's_id DB')
        time.sleep(5)
        # 주문 중 대기! sig가 0으로 바뀌면 동작

        # 이어진 호출이 있는지 확인!
    next_sig = GetValue(Center, r_s_id + 1, 'sig')

    if next_sig == 1:
        print('Order to Order ', r_s_id + 1, 'th s_id')
        Robot.update_one({'s_id': r_s_id}, {'$set': {'now_work': 0}})
        r_s_id = GoToServing(r_s_id)
        return r_s_id

    print(r_s_id + 1, 's_id sig != 1')
    return r_s_id
