from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def initial():
    return render_template('index_initial.html')

@app.route('/pos')
def pos():
    return render_template('index.html')


# 서버 연결 확인 API
@app.route('/order', methods=['GET'])
def show_pos():
    sample_receive = request.args.get('sample_give')
    # phone_number=request.args.get('phone_number')
    # orders = list(db.orders.find({}, {'_id': False}))
    return jsonify({'msg': 'GET 연결 완료!'})

# 정보 입력 API
@app.route('/order', methods=['POST'])
def save_order():
    table_number_receive = request.form['table_number_give']
    phone_number_receive = request.form['phone_number_give']

    doc={
        'table_number':table_number_receive,
        'phone_number':phone_number_receive,
    }
    # db.orders.insert_one(doc)

    return jsonify({'msg': 'post 요청 완료!'})

# 주문 목록보기(Read) API
# 주문하기(POST) API

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)