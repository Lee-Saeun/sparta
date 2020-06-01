import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('  div.music-list-wrap > table.list-wrap > tbody > tr')

for music in musics : 
    title = music.select_one('td.info > a').text.strip()
    rank = music.select_one('td.number').text.split('\n')[0]
    artist = music.select_one('td.info > a.artist').text.strip()
    print(rank, title, artist)
    