from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.Serving_Robot
Order = db.Order
Kitchen = db.Kitchen


def CalNexts_o_id(self):  # self에는 Colection이름이 들어가면 됩니다.
    max = int()
    max = 0
    x = self.find().sort("o_id")
    for i in x:
        if i['o_id'] > max:
            max = i['o_id']
    return max + 1


# 초기화면 보여주기
@app.route('/')
def home():
    return render_template('index_initial.html')


# 메뉴화면 보여주기
@app.route('/pos')
def menu():
    return render_template('index.html')


# 초기화면 연결 확인
@app.route('/initial', methods=['GET'])
def show_initial():
    sample_receive = request.args.get('sample_give')
    print('초기화면 get 완료')
    return jsonify({'msg': '초기 화면 GET 완료!'})


# 초기화면 : 테이블번호, o_s_id받아와서 Order collection에 doc 추가.
@app.route('/initial', methods=['POST'])
def save_table_no():
    i = int()
    i = CalNexts_o_id(Order)
    table_no_receive = request.form['table_no_give']
    table_num = int(table_no_receive)

    # data=request.json
    # table_no_receive=jsonify(data)['table_no_give']
    print("table num : ", table_num)
    doc = {
        'o_id': i,
        'table_no': table_num,
        'menu': ""
    }
    Order.insert_one(doc)
    return jsonify({'msg': '테이블번호가 저장되었습니다!!', 'o_id': i})


# 메뉴화면 연결 확인
@app.route('/menu', methods=['GET'])
def show_menu():
    return jsonify()



# doc의 menu원소에 메뉴리스트{"name" "count"} 추가
@app.route('/menu', methods=['POST'])
def menu_payment():
    data = request.get_json()
    menu_list = data['menulist_give']
    o_id = int(data['o_id_give'])
    total_price=int(data['total_price_give'])

    for i in menu_list:
        print(i["name"], i["count"])

    print(menu_list)
    print("o_id: ", o_id)

    db.Order.update(
        {"o_id":o_id},
        {
            "$set": {
                "menu": menu_list,
                "total_price":total_price
            }
        })
    return jsonify()


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
