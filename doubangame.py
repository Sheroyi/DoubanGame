import requests
from bs4 import BeautifulSoup
import json
import pandas
url = 'https://www.douban.com/j/ilmen/game/search?genres=&platforms=94&q=&sort=rating&more={}'
def parseGameList(url):
    newgamelist = []
    for i in range(1,501): #页数
        newurl = url.format(i)
        res = requests.get(newurl)
        jd = json.loads(res.text)
        for cnt in jd['games']: #每个项目
            newgamelist.append(cnt)
        print(i)
    return newgamelist
newgame = parseGameList(url)
df = pandas.DataFrame(newgame)
df.to_excel('newgame.xlsx')
