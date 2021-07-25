from pymongo import MongoClient
import time

# client = MongoClient("mongodb+srv://Berrykind:<password>@cluster0.z7rql.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
client=MongoClient('localhost', 27017)
db = client.get_database('Serving_Robot')

Robot = db.Robot
Center = db.Center

r_s_id = int(1)
c_s_id = int(1)

#손님이 결제 완료를 하면 해당 주문건이 center collection에 올라감.
#{s_id, table_no, sig:1, now_work:1}
#center에 주문 건을 넣을때 sig=1, now_work:1 값으로 들어감


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

    while GetValue(Robot, r_s_id, 'sig'):  # sig=1이면 주문 중 대기
        print('Order Wait', r_s_id, 's_id DB')
        time.sleep(5)
    #고객이 결제를 완료하면  sig=0으로 바뀌고, 로봇은 주방으로 이동


    # 이어진 호출이 있는지 확인!
    # 다음 호출이 있다면 sig값은 항상 1이긴 함.
    next_sig = GetValue(Center, r_s_id + 1, 'sig')

    if next_sig == 1:
        # print('Order to Order ', r_s_id + 1, 'th s_id')
        table_no_next = GetValue(Center, c_s_id + 1, 'table_no')
        print(table_no_next, " 번 테이블에서", r_s_id + 1, "번째 주문건 요청")
        Robot.update_one({'s_id': r_s_id}, {'$set': {'now_work': 0}})
        r_s_id = GoToServing(r_s_id)
        return r_s_id

    print(r_s_id + 1, 's_id sig != 1')
    return r_s_id


## Robot 실행 코드 시작
while True:
    c_s_id = GetValue(Center,r_s_id,'s_id')

    if c_s_id == 0 :
        print('No Data in Collection')
        time.sleep(5)

    #서빙 로봇 일 시작
    else :
        r_data = {'s_id' : c_s_id, 'table_no' : GetValue(Center, c_s_id, 'table_no'),'sig' : GetValue(Center, c_s_id, 'sig'),'now_work' : GetValue(Center, c_s_id, 'now_work') }
        Robot.insert_one(r_data)
        #여기서 로봇이 center에서 하나의 호출건을 받아오고
        #그 호출건(center)이 sig=0이면 주방호출, sig=1이면 손님 호출.


        ## center의 sig가 1 : 손님 호출인 경우
        if GetValue(Center, r_s_id, 'sig') == 1 :
            print("손님호출! 손님호출! 손님호출!")
            # print('Serving! Serving!! Serving!!!')
            # 자율주행부분 : 테이블로 이동

            while GetValue(Robot, r_s_id, 'sig') : #손님 주문 받는중
                print('Order Wait', r_s_id, 's_id DB')
                time.sleep(5)

               ##고객이 [결제완료]버튼 누릴시 Robot의 sig=0으로 update
                # 주방으로 복귀, 알고리즘 마무리
                # 자율주행부분 : 주방으로 이동


            next_sig = GetValue(Center, c_s_id + 1, 'sig')

            # 이어진 호출이 있는지 확인!
            if next_sig == 1 :
                table_no_next=GetValue(Center,c_s_id+1,'table_no')
                print(table_no_next," 번 테이블에서",r_s_id+1,"번째 주문건 요청")
                # print('Order to Order ', r_s_id + 1, 'th s_id')

                ##여기 좀더 이해하기
                Robot.update_one({'s_id': r_s_id}, {'$set': {'now_work': 0}})
                r_s_id = GoToServing(r_s_id)

            Robot.update_one({'s_id': r_s_id}, {'$set': {'now_work' : 0}})
            r_s_id += 1

       ##center의 sig값이 0 : 주방 호출인 경우
        elif GetValue(Center, r_s_id, 'sig') == 0 :
            print('Kitchen! Kitchen!! Kitchen!!!')
            # 주방에서 서빙 준비 중!



            while not(GetValue(Robot, r_s_id, 'sig')) : #sig=0인동안 반복
                GetValue(Robot, r_s_id, 'sig')
                print('Serving Ready Wait', r_s_id, 's_id DB')
                time.sleep(5)
                # 서빙 준비 대기 중! sig가 1으로 바뀌면 동작
                #음식 담기 완료 후, 주방직원이 [서빙 준비 완료]버튼 누를 시 , 해당건 Rogot의 sig=1로 변경

            while GetValue(Robot, r_s_id, 'sig'):
                print('Serving Complete Wait', r_s_id, 's_id DB')
                time.sleep(5)
                # sig=1이면 해당 테이블로이동 (자율주행 부분) 하고,
                # 서빙 완료 대기. 손님이 [서빙완료]버튼 누르면 sig가 0으로 바뀌면 동작
                # 주방으로 복귀, 알고리즘 마무리

            next_sig = GetValue(Center, c_s_id + 1, 'sig')

            if next_sig == 1:
                table_no_next = GetValue(Center, c_s_id + 1, 'table_no')
                print(table_no_next, " 번 테이블에서", r_s_id + 1, "번째 주문건 요청")
                # print('Serving to Order ', r_s_id + 1, 'th s_id')
                Robot.update_one({'s_id': r_s_id}, {'$set': {'now_work': 0}})
                r_s_id = GoToServing(r_s_id)
                print('if under line', r_s_id)

            Robot.update_one({'s_id': r_s_id}, {'$set': {'now_work': 0}})
            r_s_id += 1
