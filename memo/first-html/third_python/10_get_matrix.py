from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

movie = db.movies.find_one({'title':'매트릭스'}) # collection에 접근하려면 db.collection이름 
print(movie)
movie_star = movie['star']
print(movie['star'])
#하나 찾는 거는 find_one

same_star_movies = list(db.movies.find({'star': movie_star })) #여러 개 찾는 거는 find. 이거를 list로 감싸고 
for same_star_movie in same_star_movies :
    print(same_star_movie['title'])


