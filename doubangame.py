import requests
from bs4 import BeautifulSoup
import json
import pandas
url = 'https://www.douban.com/j/ilmen/game/search?genres=&platforms=94&q=&sort=rating&more={}'
def parseGameList(url):
    newgamelist = []
    n = 1
    for i in range(n): #页数
        newurl = url.format(i+1)
        res = requests.get(newurl)
        jd = json.loads(res.text)
        for cnt in jd['games']: #每个项目
            newgamelist.append(cnt)
        p = round((i+1) * 100/n)
        print("\r进度:{0}%".format(p), end='', flush=True)
    return newgamelist
newgame = parseGameList(url)
df = pandas.DataFrame(newgame)
df.to_excel('gamelist.xlsx')
