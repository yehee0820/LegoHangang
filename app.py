from flask import Flask, render_template, request, jsonify, url_for
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests







app = Flask(__name__)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.hangangdb  # 'dbsparta'라는 이름의 db를 만듭니다.

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/date')
def review_date():
    return render_template('review.html')

@app.route('/get_location')
def show_location():
    return render_template('location.html')


# location 가져오기 --> 지도 그리기
@app.route('/get_location', methods=['POST'])
def test_origin():
    user_SX = request.form['user_longitude']
    user_SY = request.form['user_latitude']

    origin = {
        'SX' : user_SX,
        'SY' : user_SY
    }

    return jsonify({'result':origin})

# place.html

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://map.naver.com/v5/search/%EC%9D%8C%EC%8B%9D%EC%A0%90?c=14128902.1697737,4512813.4860712,14,0,0,0,dh', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
yeouido_places = soup.select('#_pcmap_list_scroll_container > ul')

for i in range(9):
    for yeouido_eat in yeouido_places:
        span_tag = yeouido_eat.select_one('li:nth-child('+ i +') > div._1IVzZ > a > div._1JnOs > div > span')
        if span_tag is not None:
            name = span_tag.text
            image = yeouido_eat.select_one('li:nth-child('+ i +') > div._2vHLm > ul > li:nth-child(1) > a > div')
            comment = yeouido_eat.select_one('li:nth-child('+ i +') > div._1IVzZ > a > div:nth-child(2) > div')

            print(name, image, comment)


# review.html
@app.route('/date', methods=['POST'])
def upload_file():
    img_receive = request.files['post-img']
    print(img_receive)
    name_receive = request.form['post-nickname']
    title_receive = request.form['post-title']
    loc_receive = request.form['post-location']
    comment_receive = request.form['post-comment']

    review = {'nickname': name_receive, 'title': title_receive, 'parkLoc': loc_receive, 'img': img_receive,
           'comment': comment_receive}

    # 3. mongoDB에 데이터를 넣기
    db.reviews.insert_one(review)

    return jsonify({'result': 'success', 'reviews': review})


@app.route('/date', methods=['GET'])
def read_reviews():
    result = list(db.reviews.find({}, {'_id': 0}))

    return jsonify({'result': 'success', 'reviews': result})


# 실행
if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)


