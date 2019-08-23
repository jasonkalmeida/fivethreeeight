import urllib.request
import datetime
import requests
from bs4 import BeautifulSoup

currDate = datetime.datetime.now();

def checkTime():
    page = requests.get("https://data.fivethirtyeight.com")
    soup = BeautifulSoup(page.content, 'html.parser')
    siteTime = soup.find("table", {"id": "dataIndex"}).find("td", {"id": "polls"}).parent.find("td", {"class": "date"})['datetime']
    pollTime = datetime.datetime

    print(pollTime)

def getFile():
    print('Beginning file download with urllib2...')
    url = 'https://projects.fivethirtyeight.com/polls-page/president_primary_polls.csv'
    urllib.request.urlretrieve(url, currDate.strftime("%m") + '-' + currDate.strftime("%d") + '-polls.csv')

getFile();
