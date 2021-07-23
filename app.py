from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbhomework


# ## HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')


# 주문 목록보기(Read) API
@app.route('/pos', methods=['GET'])
def show_menu():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': 'GET 연결 완료!'})

# 주문하기(POST) API
@app.route('/pos', methods=['POST'])
def save_order():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    # menu_list_receive = request.form['menu_list_give']
    # total_price_receive=request.form['total_price_give']
    #
    # doc={
    #     'menu_list': menu_list_receive,
    #     'total_price': total_price_receive
    # }
    #
    # db.orders.insert_one(doc)

    return jsonify({'msg': '아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ 잘 되니??????'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)