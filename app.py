from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient
import datetime

# aws 접속용
client = MongoClient('mongodb://test:test@13.125.65.160', 27017)
# 로컬 접속용
# client = MongoClient('localhost', 27017)

db = client.Serving_Robot
Order = db.Order
Kitchen = db.Kitchen
Center = db.Center
Robot = db.Robot
MenuList = db.MenuList
MenuList_max = db.MenuList_max
MenuList_min = db.MenuList_min

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


def CalNexts_o_id(self):  # self에는 Colection이름이 들어가면 됩니다.
    max = int()
    max = 0
    x = self.find().sort("o_id")
    for j in x:
        if j['o_id'] > max:
            max = j['o_id']
    return max + 1


def CalNexts_s_id(self):  # self에는 Colection이름이 들어가면 됩니다.
    max = int()
    max = 0
    x = self.find().sort("s_id")
    for j in x:
        if j['s_id'] > max:
            max = j['s_id']
    return max + 1


# now_work=1인 데이터 찾기
def GetValue(self, now_work, target):  # self에는 Collection, s_id에는 확인하고 싶은 s_id, target은 추출하고 싶은 데이터이름
    results = int()

    temp = self.find({'now_work': now_work})
    print("temp:",temp)
    for j in temp:
        results = j[target]
        print("results:",results)

    if results == 0:
        return 0
    else:
        return results
#

def GetValue2(self, o_id, target):  # self에는 Collection, s_id에는 확인하고 싶은 s_id, target은 추출하고 싶은 데이터이름
    temp = self.find({'o_id': o_id})
    results2 = int()
    print("temp:", temp)
    for j in temp:
        results2 = j[target]
        print("results2:",results2)

    if results2 == 0:
        return 0
    else:
        return results2


# 초기화면 보여주기
@app.route('/')
def home():
    return render_template('face.html')


@app.route('/start')
def start():
    return render_template('index_initial.html')


# 메뉴화면 보여주기
@app.route('/pos')
def menu():
    return render_template('index.html')


# 초기화면 연결 확인
@app.route('/initial', methods=['GET'])
def show_initial():
    return jsonify()


# 초기화면 : 테이블번호, o_s_id받아와서 Order collection에 doc 추가.
# @app.route('/initial', methods=['POST'])
# def save_table_no():
#     i = CalNexts_o_id(Order)
#     table_no_receive = request.form['table_no_give']
#     table_num = int(table_no_receive)
#
#
#     # print("table num : ", table_num)
#     doc = {
#         'o_id': i,
#         'table_no': table_num,
#         'menu': "",
#         'total_price': 0,
#         'status': "처리중"
#     }
#     Order.insert_one(doc)
#     return jsonify({'o_id': i})


# 메뉴화면 연결 확인
@app.route('/menu', methods=['GET'])
def show_menu():
    return jsonify()


@app.route('/menu', methods=['POST'])
def menu_payment():
    data = request.get_json()
    menu_list = data['menulist_give']
    i = CalNexts_o_id(Order)
    # o_id = int(data['o_id_give'])
    total_price = int(data['total_price_give'])
    now = datetime.datetime.utcnow()
    table_no = GetValue(Robot, 1, 'table_no')

    doc = {
        'o_id': i,
        'table_no': table_no,
        'menu': menu_list,
        'total_price':total_price ,
        'status': "처리중",
        "date": now

    }
    Order.insert_one(doc)


    # db.Order.update(
    #     {"o_id": o_id},
    #     {
    #         "$set": {
    #             "menu": menu_list,
    #             "total_price": total_price,
    #             "date": now
    #         }
    #     })
    db.Robot.update_one(
        {"now_work": 1},
        {
            "$set": {
                "sig": 0
            }
        })
    return jsonify()


# 주방포스 로드
@app.route('/kitchen')
def kitchen():
    return render_template('kitchen.html')


# kitchen pos에 주문내역 보여주는 api
@app.route('/kitchen_pos', methods=['GET'])
def show_order():
    page = 1
    # page = request.args.get('page')
    # if page is None:
    #     page=1
    # print("page : ",page)
    # orders = list(Order.find({}, {'_id': False}).skip((page - 1) * 10).limit(10))
    orders = list(Order.find({}, {'_id': False}))
    # print(orders)
    return jsonify({'all_orders': orders})


# info 페이지 로드
@app.route('/info')
def info():
    return render_template('info.html')


# info 페이지에 판매내역 보여주는 api
@app.route('/show_info', methods=['GET'])
def show_info():
    menu = list(MenuList.find({}, {'_id': False}))
    menu_max = list(MenuList_max.find({}, {'_id': False}))
    menu_min = list(MenuList_min.find({}, {'_id': False}))

    print("menu나오니?",menu)
    return jsonify({'all_menu': menu, 'menu_max': menu_max, 'menu_min': menu_min})


def CountMenu(collection, ):
    dic_count = {0: 0, 1: 0, 2: 0, 3: 0,
                 4: 0, 5: 0, 6: 0, 7: 0,
                 8: 0, 9: 0, 10: 0, 11: 0,
                 12: 0, 13: 0, 14: 0, 15: 0}
    dic_total_price = {0: 0, 1: 0, 2: 0, 3: 0,
                       4: 0, 5: 0, 6: 0, 7: 0,
                       8: 0, 9: 0, 10: 0, 11: 0,
                       12: 0, 13: 0, 14: 0, 15: 0}

    x = collection.find().sort("o_id")
    for i in x:
        for j in i['menu']:
            id = j['id']
            name = j['name']
            count = int(j['count'])
            # print(id, name, count)
            dic_count[id] = dic_count[id] + count
            dic_total_price[id] = dic_price[id] * dic_count[id]
            # print("dic_count: ", dic_count)

    for i in range(0, 16):
        # print(i, dic_name[i], dic_count[i], dic_total_price[i])
        doc = {
            'm_id': i,
            'menu_name': dic_name[i],
            'menu_count': dic_count[i],
            'menu_total_price': dic_total_price[i]
        }
        MenuList.insert_one(doc)

    # 최다 판매 메뉴
    max = 0
    max_index = 0
    for i in range(0, 16):
        if max < dic_count[i]:
            max = dic_count[i]
            max_index = i
    # print("최다 판매 메뉴: ", dic_name[max_index], dic_count[max_index], dic_total_price[max_index])

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
        if dic_count[i] != 0:
            if min > dic_count[i]:
                min = dic_count[i]
                min_index = i
    # print("최소 판매 메뉴: ", dic_name[min_index], dic_count[min_index], dic_total_price[min_index])

    for i in range(0, 16):
        if min == dic_count[i]:
            doc = {
                'm_id': i,
                'menu_name': dic_name[i],
                'menu_count': dic_count[i],
                'menu_total_price': dic_total_price[i]
            }
            MenuList_min.insert(doc)


# info 페이지로 넘어갈때 MenuList collection 생성하는 api
@app.route('/info_insert', methods=['POST'])
def info_insert():
    db.MenuList.drop()
    db.MenuList_max.drop()
    db.MenuList_min.drop()
    CountMenu(Order)
    # print("dic_count: ", dic_count)
    # print("dic_total_price: ", dic_total_price)
    print("info_insert()함수 성공!")

    return jsonify()


# 상태변경 버튼 눌렀을때 주문내역 상태값 변경
@app.route('/process', methods=['POST'])
def status_change():
    data = request.get_json()
    o_id = data['o_id_give']
    # print("o_id : ", o_id)

    db.Order.update(
        {"o_id": o_id},
        {
            "$set": {
                "status": "처리완료"
            }
        })
    return jsonify()


# 로봇 호출 버튼
@app.route('/robot_call', methods=['POST'])
def robot_call():
    data = request.get_json()
    table_no_receive = data['table_no_give']
    table_int = int(table_no_receive)
    o_id_receive = int(data['o_id_give'])
    print("o_id_receive:",o_id_receive)

    o_status=str()
    o_status = GetValue2(Order, o_id_receive, 'status')

    if o_status=="처리중":
        i = int()
        i = CalNexts_s_id(Center)
        data = {'s_id': i, 'table_no': table_int, 'sig': 0, 'now_work': 1}
        Center.insert_one(data)
        msg='호출정보가 Center에 저장되었습니다!.'
    else:
        msg='이미 처리된 주문건입니다.'

    return jsonify({'msg': msg} )


# 서빙준비완료 버튼
#  //robot(collection)에서 now_work=1인 쿼리중 맨위 데이터의 sig=0이면  sig=1로 update, r_move=1로 update
# 로봇호출할때는 checkbox 체크해야되고, [로봇호출]누르고 나서 바로 [서빙준비완료] 버튼 눌러야함.
@app.route('/prepare_complete', methods=['POST'])
def prepare_complete():
    check = int()
    table_no = GetValue(Robot, 1, 'table_no')
    # print("table_no : ",table_no)

    data = request.get_json()
    order_no_receive = int(data['order_no_give'])
    o_status = GetValue2(Order, order_no_receive, 'status')
    print("o_status:", o_status)

    if o_status=="처리중":
        db.Order.update_one(
            {"o_id": order_no_receive},
            {
                "$set": {
                    "status": "처리완료"
                }
            })

        db.Robot.update_one(
            {"now_work": 1},
            {
                "$set": {
                    "sig": 1
                }
            })
        msg = str(table_no)+'번 테이블 주문의 서빙준비가 완료되었습니다.'
    else:
        msg='이미 처리된 주문건입니다.'
    return jsonify({'msg':msg})


# 데이터 삭제 버튼
@app.route('/delete_data', methods=['POST'])
def delete_data():
    Order.drop()
    Robot.drop()
    Center.drop()
    MenuList.drop()
    MenuList_max.drop()
    MenuList_min.drop()

    return jsonify({'msg': '데이터가 전부 삭제되었습니다.'})


# face화면 // 서빙받기 완료 버튼 ( 누르면 로봇이 주방으로 돌아감.)
# Robot collection에서 now_work=1인 데이터 now_work=0으로 수정, sig=0으로 변경
@app.route('/serving_complete', methods=['POST'])
def serving_complete():
    s_id = GetValue(Robot, 1, 's_id')
    # print("s_id:", s_id)
    if s_id == 0:
        msg = "도착 정보가 없습니다."
    else:
        db.Robot.update_one(
            {"now_work": 1},
            {
                "$set": {
                    "sig": 0,
                    "now_work": 0
                }
            })
        msg = "서빙이 완료되었습니다."
    # print(msg)
    return jsonify({'msg': msg})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
