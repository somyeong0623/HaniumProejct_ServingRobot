from pymongo import MongoClient
import time

client = MongoClient("mongodb+srv://Berrykind:<password>@cluster0.z7rql.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.get_database('Serving_Robot')

Robot = db.Robot
Center = db.Center

r_s_id = int(1)
c_s_id = int(0)

def GetValue(self, s_id, target) :
    results = int()

    temp = self.find({'s_id':s_id})

    for j in temp :
        results = j[target]

    if results == 0 :
        return 0
    else :
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
        print('Go To ', r_s_id + 1, 's_id Serving')
        Robot.update_one({'s_id': r_s_id}, {'$set': {'now_work': 0}})
        GoToServing(r_s_id)
        return r_s_id + 1

    print(r_s_id + 1, 's_id sig != 1')
    return r_s_id

while True:
    c_s_id = GetValue(Center,r_s_id,'s_id')

    if c_s_id == 0 :
        print('No Data in Collection')
        time.sleep(5)

    else :
        r_data = {'s_id' : c_s_id, 'table_no' : GetValue(Center, c_s_id, 'table_no'),'sig' : GetValue(Center, c_s_id, 'sig'),'now_work' : GetValue(Center, c_s_id, 'now_work') }
        Robot.insert_one(r_data)

        if GetValue(Center, r_s_id, 'sig') == 1 :
            print('Serving! Serving!! Serving!!!')
            # 식당으로 서빙하러 가기!

            while GetValue(Robot, r_s_id, 'sig') :
                print('Order Wait', r_s_id, 's_id DB')
                time.sleep(5)
                # 주문 중 대기! sig가 0으로 바뀌면 동작
                # 주방으로 복귀, 알고리즘 마무리

            next_sig = GetValue(Center, c_s_id + 1, 'sig')

            if next_sig == 1 :
                print('Go To ', r_s_id + 1, 's_id Serving')
                Robot.update_one({'s_id': r_s_id}, {'$set': {'now_work': 0}})
                r_s_id = GoToServing(r_s_id)

            Robot.update_one({'s_id': r_s_id}, {'$set': {'now_work' : 0}})
            r_s_id += 1


        elif GetValue(Center, r_s_id, 'sig') == 0 :
            print('Kitchen! Kitchen!! Kitchen!!!')
            # 주방에서 서빙 준비 중!

            while not(GetValue(Robot, r_s_id, 'sig')) :
                GetValue(Robot, r_s_id, 'sig')
                print('Serving Ready Wait', r_s_id, 's_id DB')
                time.sleep(5)
                # 서빙 준비 대기 중! sig가 1으로 바뀌면 동작

            while GetValue(Robot, r_s_id, 'sig'):
                print('Serving Complete Wait', r_s_id, 's_id DB')
                time.sleep(5)
                # 서빙 완료 대기! sig가 0으로 바뀌면 동작
                # 주방으로 복귀, 알고리즘 마무리

            Robot.update_one({'s_id': r_s_id}, {'$set': {'now_work': 0}})
            r_s_id += 1