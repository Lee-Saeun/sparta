from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/test', methods=['POST']) #method다르면 경로 겹쳐도 됨! 
def test_post():
   title_receive = request.form['title_give'] #form을 통해 
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!','title':title_receive})

@app.route('/test', methods=['GET'])
def test_get():
   title_receive = request.args.get('title_give') # args에 쿼리 파라미터를 저장 , title_receive에 저장한다 . 데이터를 가져오려면 args.get('키값')
   print(title_receive) #요청한거 다 기록됨 
   return jsonify({'result':'success', 'msg': '이 요청은 GET!','title':title_receive}) #응답값이 항상 고정되어 있음 

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)