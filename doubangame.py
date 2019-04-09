import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
print('请输入抓取页数：')
n = int(input())
url = 'https://www.douban.com/j/ilmen/game/search?genres=&platforms=94&q=&sort=rating&more={}'
def parseGameList(url,n):
    newgamelist = []
    for i in range(n): #页数
        newurl = url.format(i+1)
        res = requests.get(newurl)
        jd = json.loads(res.text)
        for cnt in jd['games']: #每个项目
            newgamelist.append(cnt)
        p = round((i+1) * 100/n)
        print("\r抓取进度:{0}%".format(p), end='', flush=True)
        if(i == (n-1)):
            print("\n完成！")
    return newgamelist
newgame = parseGameList(url,n)
df = pd.DataFrame(newgame)
df.to_excel('gamelist.xlsx')
