from flask import Flask, render_template, request, jsonify, url_for,redirect,send_from_directory
from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
from werkzeug.utils import secure_filename
import pandas as pd
import os

app = Flask(__name__)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.hangangdb  # 'dbsparta'라는 이름의 db를 만듭니다.



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/review')
def review_date():
    return render_template('review.html')

@app.route('/howtogo')
def show_location():
    return render_template('location.html')
@app.route('/fastestway')
def fastest_route():
    return render_template('location2.html')

@app.route('/bicycle')
def show_bickeinfo():
    return render_template('bicycle.html')

###### review image uploading

app.config['UPLOAD_FOLDER'] = 'static/uploadimg'

@app.route('/upload')
def render_html():
    return render_template('upload.html')

@app.route('/fileUpload',methods = ['POST'])
def upload_file():
    f = request.files['file']
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
    return 'success!'

@app.route('/test')
def test():
    filename = 'static/uploadimg/sparta.png'
    return render_template('test.html',filename=filename)

###review(메모장활용)
@app.route('/memo', methods=['POST'])
def post_reviews():
    # 1. 클라이언트로부터 데이터를 받기
    id_receive = request.form['id_give']
    title_receive = request.form['title_give']
    park_receive = request.form['park_give']
    comment_receive = request.form['comment_give']

    review = {'title': title_receive, 'id': id_receive, 'park': park_receive, 'comment': comment_receive}

    # 3. mongoDB에 데이터를 넣기
    db.reviews.insert_one(review)

    return jsonify({'result': 'success'})


@app.route('/memo', methods=['GET'])
def read_reviews():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read)
    result = list(db.reviews.find({}, {'_id': 0}))
    # 2. articles라는 키 값으로 article 정보 보내주기
    return jsonify({'result': 'success', 'reviews': result})

##########################
#bicycle_info
##########################

def getBikeInfo(location):
    print("##################")
    print(location)
    print("##################")
    base_dir = 'Users/yehee/Desktop/LegoHangang/LegoHangang'
    excel_file = 'static/bicycle_info.xlsx'
    excel_dir = os.path.join(base_dir, excel_file)

    # read a excel file and make it as a DataFrame
    if location == 1:
        df_bicycle = pd.read_excel(excel_dir,
                                  sheet_name = 'yeouido',
                                  names = ['id', 'location', 'where', 'address', 'latitude', 'longitude'],
                                  dtype = {'id':int, 'location': str,
                                             'where': str,
                                             'address': str,
                                             'latitude': float,
                                             'longitude': float},
                                  index_col = 'id',
                                  na_values = ',',
                                  comment = '#')
        df = pd.DataFrame(df_bicycle)
    elif location == 2:
        df_bicycle = pd.read_excel(excel_dir,
                                  sheet_name = 'nanji',
                                  names = ['id', 'location', 'where', 'address', 'latitude', 'longitude'],
                                  dtype = {'id':int, 'location': str,
                                             'where': str,
                                             'address': str,
                                             'latitude': float,
                                             'longitude': float},
                                  index_col = 'id',
                                  na_values = ',',
                                  comment = '#')
        df = pd.DataFrame(df_bicycle)
    elif location == 3:
        df_bicycle = pd.read_excel(excel_dir,
                                  sheet_name = 'dduksum',
                                  names = ['id', 'location', 'where', 'address', 'latitude', 'longitude'],
                                  dtype = {'id':int, 'location': str,
                                             'where': str,
                                             'address': str,
                                             'latitude': float,
                                             'longitude': float},
                                  index_col = 'id',
                                  na_values = ',',
                                  comment = '#')
        df = pd.DataFrame(df_bicycle)
    elif location == 4:
        df_bicycle = pd.read_excel(excel_dir,
                                  sheet_name = 'gwangnaru',
                                  names = ['id', 'location', 'where', 'address', 'latitude', 'longitude'],
                                  dtype = {'id':int, 'location': str,
                                             'where': str,
                                             'address': str,
                                             'latitude': float,
                                             'longitude': float},
                                  index_col = 'id',
                                  na_values = ',',
                                  comment = '#')
        df = pd.DataFrame(df_bicycle)
    elif location == 5:
        df_bicycle = pd.read_excel(excel_dir,
                                  sheet_name = 'gangseo',
                                  names = ['id', 'location', 'where', 'address', 'latitude', 'longitude'],
                                  dtype = {'id':int, 'location': str,
                                             'where': str,
                                             'address': str,
                                             'latitude': float,
                                             'longitude': float},
                                  index_col = 'id',
                                  na_values = ',',
                                  comment = '#')
        df = pd.DataFrame(df_bicycle)
    elif location == 6:
        df_bicycle = pd.read_excel(excel_dir,
                                  sheet_name = 'jamsil',
                                  names = ['id', 'location', 'where', 'address', 'latitude', 'longitude'],
                                  dtype = {'id':int, 'location': str,
                                             'where': str,
                                             'address': str,
                                             'latitude': float,
                                             'longitude': float},
                                  index_col = 'id',
                                  na_values = ',',
                                  comment = '#')
        df = pd.DataFrame(df_bicycle)
    elif location == 7:
        df_bicycle = pd.read_excel(excel_dir,
                                  sheet_name = 'mangwon',
                                  names = ['id', 'location', 'where', 'address', 'latitude', 'longitude'],
                                  dtype = {'id':int, 'location': str,
                                             'where': str,
                                             'address': str,
                                             'latitude': float,
                                             'longitude': float},
                                  index_col = 'id',
                                  na_values = ',',
                                  comment = '#')
        df = pd.DataFrame(df_bicycle)
    elif location == 8:
        df_bicycle = pd.read_excel(excel_dir,
                                  sheet_name = 'yangwha',
                                  names = ['id', 'location', 'where', 'address', 'latitude', 'longitude'],
                                  dtype = {'id':int, 'location': str,
                                             'where': str,
                                             'address': str,
                                             'latitude': float,
                                             'longitude': float},
                                  index_col = 'id',
                                  na_values = ',',
                                  comment = '#')
        df = pd.DataFrame(df_bicycle)
    elif location == 9:
        df_bicycle = pd.read_excel(excel_dir,
                                  sheet_name = 'ichon',
                                  names = ['id', 'location', 'where', 'address', 'latitude', 'longitude'],
                                  dtype = {'id':int, 'location': str,
                                             'where': str,
                                             'address': str,
                                             'latitude': float,
                                             'longitude': float},
                                  index_col = 'id',
                                  na_values = ',',
                                  comment = '#')
        df = pd.DataFrame(df_bicycle)
    elif location == 10:
        df_bicycle = pd.read_excel(excel_dir,
                                  sheet_name = 'jamwon',
                                  names = ['id', 'location', 'where', 'address', 'latitude', 'longitude'],
                                  dtype = {'id': int, 'location': str,
                                             'where': str,
                                             'address': str,
                                             'latitude': float,
                                             'longitude': float},
                                  index_col = 'id',
                                  na_values = ',',
                                  comment = '#')
        df = pd.DataFrame(df_bicycle)
    else:
        df_bicycle = pd.read_excel(excel_dir,
                                   sheet_name='banpo',
                                   names=['id', 'location', 'where', 'address', 'latitude', 'longitude'],
                                   dtype={'id': int, 'location': str,
                                          'where': str,
                                          'address': str,
                                          'latitude': float,
                                          'longitude': float},
                                   index_col='id',
                                   na_values=',',
                                   comment='#')
        df = pd.DataFrame(df_bicycle)

    convert_bicycle = df.to_dict()
    return convert_bicycle

@app.route("/bicycle_locate", methods=["GET"])
def my_excel_data():
    q = request.args.get('locate')

    data = getBikeInfo(q)
    print("#######################")
    print(data)
    print("#######################")
    # 돌아오는 data는 dataframe이기 때문에 data to list변환을 해주어야합니다.
    df_data = pd.DataFrame(data)
    convert_data = df_data.to_dict()
    print(convert_data)

    return convert_data



##########################
#rent_info
##########################
# base_dir = 'Users/yehee/Desktop/LegoHangang/LegoHangang'
# excel_file = 'static/rent_info.xlsx'
# excel_dir = os.path.join(base_dir, excel_file)

# read a excel file and make it as a DataFrame

# df_yeouido = pd.read_excel(excel_dir,
#                           sheet_name = 'yeouido',
#                           names = ['id', 'name', 'location', 'latitude', 'longitude', 'time', 'url', 'comment'],
#                           dtype = {'id':int, 'name': str,
#                                      'location': str,
#                                      'latitude': float,
#                                      'longitude': float, 'time':str, 'url':str, 'comment':str},
#                           index_col = 'id',
#                           na_values = ',',
#                           comment = '#')
#
# df_gwangnaru = pd.read_excel(excel_dir,
#                           sheet_name = 'gwangnaru',
#                           names = ['id', 'name', 'location', 'latitude', 'longitude', 'time', 'url', 'comment'],
#                           dtype = {'id':int, 'name': str,
#                                      'location': str,
#                                      'latitude': float,
#                                      'longitude': float, 'time':str, 'url':str, 'comment':str},
#                           index_col = 'id',
#                           na_values = ',',
#                           comment = '#')
#
# df_nanji = pd.read_excel(excel_dir,
#                           sheet_name = 'nanji',
#                           names = ['id', 'name', 'location', 'latitude', 'longitude', 'time', 'url', 'comment'],
#                           dtype = {'id':int, 'name': str,
#                                      'location': str,
#                                      'latitude': float,
#                                      'longitude': float, 'time':str, 'url':str, 'comment':str},
#                           index_col = 'id',
#                           na_values = ',',
#                           comment = '#')
#
# df_ichon = pd.read_excel(excel_dir,
#                           sheet_name = 'ichon',
#                           names = ['id', 'name', 'location', 'latitude', 'longitude', 'time', 'url', 'comment'],
#                           dtype = {'id':int, 'name': str,
#                                      'location': str,
#                                      'latitude': float,
#                                      'longitude': float, 'time':str, 'url':str, 'comment':str},
#                           index_col = 'id',
#                           na_values = ',',
#                           comment = '#')
#
# df_banpo = pd.read_excel(excel_dir,
#                           sheet_name = 'banpo',
#                           names = ['id', 'name', 'location', 'latitude', 'longitude', 'time', 'url', 'comment'],
#                           dtype = {'id':int, 'name': str,
#                                      'location': str,
#                                      'latitude': float,
#                                      'longitude': float, 'time':str, 'url':str, 'comment':str},
#                           index_col = 'id',
#                           na_values = ',',
#                           comment = '#')
#
# df_jamwon = pd.read_excel(excel_dir,
#                           sheet_name = 'jamwon',
#                           names = ['id', 'name', 'location', 'latitude', 'longitude', 'time', 'url', 'comment'],
#                           dtype = {'id':int, 'name': str,
#                                      'location': str,
#                                      'latitude': float,
#                                      'longitude': float, 'time':str, 'url':str, 'comment':str},
#                           index_col = 'id',
#                           na_values = ',',
#                           comment = '#')
#
# df_mangwon = pd.read_excel(excel_dir,
#                           sheet_name = 'mangwon',
#                           names = ['id', 'name', 'location', 'latitude', 'longitude', 'time', 'url', 'comment'],
#                           dtype = {'id':int, 'name': str,
#                                      'location': str,
#                                      'latitude': float,
#                                      'longitude': float, 'time':str, 'url':str, 'comment':str},
#                           index_col = 'id',
#                           na_values = ',',
#                           comment = '#')
#
# df_yangwha = pd.read_excel(excel_dir,
#                           sheet_name = 'yangwha',
#                           names = ['id', 'name', 'location', 'latitude', 'longitude', 'time', 'url', 'comment'],
#                           dtype = {'id':int, 'name': str,
#                                      'location': str,
#                                      'latitude': float,
#                                      'longitude': float, 'time':str, 'url':str, 'comment':str},
#                           index_col = 'id',
#                           na_values = ',',
#                           comment = '#')
#
# df_dduksum = pd.read_excel(excel_dir,
#                           sheet_name = 'dduksum',
#                           names = ['id', 'name', 'location', 'latitude', 'longitude', 'time', 'url', 'comment'],
#                           dtype = {'id':int, 'name': str,
#                                      'location': str,
#                                      'latitude': float,
#                                      'longitude': float, 'time':str, 'url':str, 'comment':str},
#                           index_col = 'id',
#                           na_values = ',',
#                           comment = '#')

#print(df_yeouido)
#print(df_gwangnaru)
#print(df_banpo)
#print(df_ichon)
#print(df_jamwon)
#print(df_yangwha)
#print(df_dduksum)
#print(df_nanji)
#print(df_mangwon)




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



# 날씨

# html = requests.get('https://search.naver.com/search.naver?query=날씨')
#
# soup = BeautifulSoup(html.text, 'html.parser')
#
# data1 = soup.find('div', {'class': 'weather_box'})
#
# find_address = data1.find('span', {'class':'btn_select'}).text
# print('현재 위치: '+find_address)
#
# find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
# print('현재 온도: '+find_currenttemp+'℃')
#
# data2 = data1.findAll('dd')
# find_dust = data2[0].find('span', {'class':'num'}).text
# find_ultra_dust = data2[1].find('span', {'class':'num'}).text
# find_ozone = data2[2].find('span', {'class':'num'}).text
# print('현재 미세먼지: '+find_dust)
# print('현재 초미세먼지: '+find_ultra_dust)
# print('현재 오존지수: '+find_ozone)


# 실행
if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)


