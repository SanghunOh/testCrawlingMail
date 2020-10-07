import requests
from bs4 import BeautifulSoup
import sqlite3
from pymongo import MongoClient

path = 'datas/sample03.html'
db_url = 'mongodb://192.168.0.6:27017/'

def scheduler_sample():
    with open(path) as fp:						        # shared github
        soup = BeautifulSoup(fp, features='lxml')
        links = soup.select('p[id]')					# 속성 존재 여부 검색

        # connect MongoDB
        with MongoClient(db_url) as client:
            sampledb = client['sample03db']						# get Database
            # check collections
            if ("sampleCollection" not in sampledb.list_collection_names()):
                sampledb.create_collection('sampleCollection')

            title = ''
            link = ''
            for link in links:
                title = str.strip(link.get_text())
                link = link['id']
                data = {'title': title, 'id': link}
                infor = sampledb.sampleCollection.insert_one(data)
                print(infor.inserted_id)
