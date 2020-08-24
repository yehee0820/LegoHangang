from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.hangangdb  # 'dbsparta'라는 이름의 db를 만듭니다.

@app.route('/')
def index():
    return render_template('place.html')


@app.route('/get_location', methods=['POST'])
def test_origin():
    user_SX = request.form['user_longitude']
    user_SY = request.form['user_latitude']

    origin = {
        'SX' : user_SX,
        'SY' : user_SY
    }

    return jsonify({'result':origin})

####################

@app.route('/date', methods=['POST'])
def post_article():
    # 1. 클라이언트로부터 데이터를 받기
    name_receive = request.form['nickname']
    title_receive = request.form['title']
    loc_receive = request.form['parkLoc']
    img_receive = request.form['img']
    comment_receive = request.form['comment']


    review = {'nickname': name_receive, 'title': title_receive, 'parkLoc': loc_receive, 'img': img_receive, 'comment': comment_receive}

    # 3. mongoDB에 데이터를 넣기
    db.reviews.insert_one(review)

    return jsonify({'result': 'success', 'data': review})


@app.route('/date', methods=['GET'])
def read_reviews():
    result = list(db.reviews.find({}, {'_id': 0}))

    return jsonify({'result': 'success', 'reviews': result})

if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)


