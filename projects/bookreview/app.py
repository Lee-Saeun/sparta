from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분 route 패쓰에 요청하면 index.html을 반환해라 
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
	# 1. 클라이언트가 준 title, author, review 가져오기.
	# 2. DB에 정보 삽입하기, 그리고 그걸 읽어오기 
	# 3. 성공 여부 & 성공 메시지 반환하기
    title = request.form['title']
    author = request.form['author']
    review = request.form['review']
    db.reviews.insert_one({
        'title' : title,
        'author' : author,
        'review' : review
    })
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})

@app.route('/reviews', methods=['GET'])
def read_reviews():
    reviews = list(db.reviews.find({},{"_id":False})) #알아듣기 위해서는 list로 감싸 주고, id라는 속성값은 제외해줘야 함 
    return jsonify({'result':'success', 'msg': '이 요청은 GET!','reviews':reviews}) #이게 response라는 변수에 들어가 있을 것이다 


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)