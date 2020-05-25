print ('Hello, sparta')

a = 3      # 3을 a에 넣는다
b = a      # a를 b에 넣는다
a = a + 1  # a+1을 다시 a에 넣는다
print(a)
num1 = a*b # a*b의 값을 num1이라는 변수에 넣는다
num2 = 99 # 99의 값을 num2이라는 변수에 넣는다
print(num1,num2)
# 변수의 이름은 마음대로 지을 수 있음!
# 진짜 "마음대로" 짓는 게 좋을까? var1, var2 이렇게?

name = 'bob' # 변수에는 문자열이 들어갈 수도 있고,
age = 12 # 숫자가 들어갈 수도 있고,

person = {'name' : 'bob', 'age' : 12 } #dictionary 
print(person['age'])

shin = {'name' : '신동현' , 'age' : 22}

people = [person,shin] #리스트,array
print(people[0])

print(people)
name='신동현'
is_number = True # True 또는 False -> "Boolean"형이 들어갈 수도 있습니다.

#########
# 그리고 List, Dictionary 도 들어갈 수도 있죠. 그게 뭔지는 아래에서!

def sum(num1, num2):
    print(num1,num2)
    return num1 + num2  

result = sum(1,2)
print(result)

def is_adult(age):
    if age > 19: 
        print("성인입니다") 
    else: 
        print("성인이 아닙니다")

print(is_adult(30))

ages = [10, 30, 27, 101, 58]

for apple in ages: 
   
    is_adult(apple) 

# 메일주소가 맞는지 판단하기
a = 'spartacodingclub@gmail.com'

#채워야하는 함수
def check_mail(s):
    return '@' in s
       
	## 여기에 코딩을 해주세요

#결과값
print(check_mail(a))

#아래와 같이 출력됩니다
True

#입력값
a = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']

#채워야하는 함수
def count_list(a_list):
    result = {}
    for fruit in a_list:
        if fruit in result:
            result[fruit] = result[fruit] + 1
        else:
            result[fruit] = 1
	## 여기에 코딩을 해주세요
    return result

#결과값
print(count_list(a))

#아래와 같이 출력됩니다
{'사과': 1, '감': 3, '배': 1, '포도': 3, '딸기': 2, '수박': 1}

import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()
print (rjson['RealtimeCityAir']['row'][0]['CO'])