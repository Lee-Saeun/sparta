import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json() #json형식으로 데이터를 변환해서 rjson이라는 변수에 담아준다! 
rows = rjson['RealtimeCityAir']['row']
for i in rows :
    gu = i['MSRSTE_NM']
    mise = i['IDEX_MVL']
    #print(gu , mise)
    if mise > 50 :
        print('미세먼지 위험 구:'+ gu, mise)