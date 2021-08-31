from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

# aws 접속용
# client = MongoClient('mongodb://test:test@localhost', 27017)
# 로컬 접속용
client = MongoClient('localhost', 27017)

db = client.Serving_Robot
Order = db.Order
Kitchen = db.Kitchen
Center = db.Center
Robot = db.Robot


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

    for j in temp:
        results = j[target]
        # 여기서 for문 인 이유 ??

    if results == 0:
        return 0
    else:
        return results


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
@app.route('/initial', methods=['POST'])
def save_table_no():
    i = CalNexts_o_id(Order)
    table_no_receive = request.form['table_no_give']
    table_num = int(table_no_receive)

    # data=request.json
    # table_no_receive=jsonify(data)['table_no_give']
    print("table num : ", table_num)
    doc = {
        'o_id': i,
        'table_no': table_num,
        'menu': "",
        'total_price': 0,
        'status': "처리중"
    }
    Order.insert_one(doc)
    return jsonify({'o_id': i})


# 메뉴화면 연결 확인
@app.route('/menu', methods=['GET'])
def show_menu():
    return jsonify()


@app.route('/menu', methods=['POST'])
def menu_payment():
    data = request.get_json()
    menu_list = data['menulist_give']
    o_id = int(data['o_id_give'])
    total_price = int(data['total_price_give'])
    db.Order.update(
        {"o_id": o_id},
        {
            "$set": {
                "menu": menu_list,
                "total_price": total_price
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
    print(orders)
    return jsonify({'all_orders': orders})


# 상태변경 버튼 눌렀을때 주문내역 상태값 변경
@app.route('/process', methods=['POST'])
def status_change():
    data = request.get_json()
    o_id = data['o_id_give']
    print("o_id : ", o_id)

    db.Order.update(
        {"o_id": o_id},
        {
            "$set": {
                "status": "처리완료"
            }
        })
    return jsonify()

# 로봇pos에서 주문 완료 (결제 완료)
# Robot colleton의 해당 호출건을 sig=0, now_work=0 으로 update.
@app.route('/order_complete', methods=['POST'])
def order_complete():
    db.Robot.update_one(
        {"now_work": 1},
        {
            "$set": {
                "r_move": 0
            }
        })
    return jsonify({'msg': '로봇이 도착하였습니다'})


# 로봇 호출 버튼
@app.route('/robot_call', methods=['POST'])
def robot_call():
    data = request.get_json()
    table_no_receive = data['table_no_give']
    table_int = int(table_no_receive)
    print(table_int)
    i = int()
    i = CalNexts_s_id(Center)
    data = {'s_id': i, 'table_no': table_int, 'sig': 0, 'now_work': 1}
    Center.insert_one(data)

    return jsonify({'msg': '호출정보가 Center에 저장되었습니다!.'})


# 로봇 도착 버튼
# Robot collection에서 now_work 1인 쿼리의 r_move=0으로 변경
@app.route('/robot_arrive', methods=['POST'])
def robot_arrive():
    db.Robot.update_one(
        {"now_work": 1},
        {
            "$set": {
                "r_move": 0
            }
        })
    return jsonify({'msg': '로봇이 도착하였습니다'})


# 서빙준비완료 버튼
#  //robot(collection)에서 now_work=1인 쿼리중 맨위 데이터의 sig=0이면  sig=1로 update, r_move=1로 update
# 로봇호출할때는 checkbox 체크해야되고, [로봇호출]누르고 나서 바로 [서빙준비완료] 버튼 눌러야함.
@app.route('/prepare_complete', methods=['POST'])
def prepare_complete():
    check = int()
    num = GetValue(Robot, 1, 'table_no')

    db.Robot.update_one(
        {"now_work": 1},
        {
            "$set": {
                "sig": 1,
                "r_move": 1
            }
        })

    return jsonify({'msg': str(num) + '번 테이블의 주문이 서빙준비가 완료되었습니다'})


# face화면 // 서빙받기 완료(로봇 도착) 버튼
# Robot collection에서 now_work=1인 데이터 now_work=0으로 수정, r_move=0으로 변경
@app.route('/robot_arrive2', methods=['POST'])
def robot_arrive2():
    db.Robot.update_one(
        {"now_work": 1},
        {
            "$set": {
                "sig": 0,
                "now_work": 0,
                "r_move": 0
            }
        })

    return jsonify({'msg': "로봇이 도착하였습니다. "})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
