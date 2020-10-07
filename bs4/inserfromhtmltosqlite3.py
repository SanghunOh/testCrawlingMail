import requests
from bs4 import BeautifulSoup
import sqlite3

path = 'datas/sample03.html'

with open(path) as fp:						# shared github
    soup = BeautifulSoup(fp, features='lxml')
    links = soup.select('p[id]')					# 속성 존재 여부 검색

    with sqlite3.connect("datas/db.sqlite3") as con:
        cur = con.cursor()
        title = ''
        link = ''
        query = "INSERT INTO sample03 (title,link, create_date) VALUES (?,?,datetime('now'))"
        for link in links:
            title = str.strip(link.get_text())
            link = link['id']
            cur.execute(query,(title,link))
        con.commit()

