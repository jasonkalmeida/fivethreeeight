import urllib.request
import datetime
import requests
from bs4 import BeautifulSoup
import csv
import json
import sys
import shutil





currDate = datetime.datetime.now();

def checkTime():
    page = requests.get("https://data.fivethirtyeight.com")
    soup = BeautifulSoup(page.content, 'html.parser')
    siteTime = soup.find("table", {"id": "dataIndex"}).find("td", {"id": "polls"}).parent.find("td", {"class": "date"})['datetime']

    with open("cache.json", "r") as fin:
        data = json.load(fin)
        lastUp = data["lastUpdate"]
        if(lastUp != siteTime):
            print("Not same")
            shutil.move(data["currentFile"], "OldFiles/" + data["currentFile"])
            newName = getFile()
            update = {
                "lastUpdate": siteTime,
                "currentFile": newName
            }
            print(update)
            with open("cache.json","w+") as f:
                f.write(json.dumps(update, indent=4))
                f.close()
        else:
            print("Is same")

def getFile():
    print('Beginning file download with urllib2...')
    newFileName = currDate.strftime("%m") + '-' + currDate.strftime("%d") + '-polls.csv'
    url = 'https://projects.fivethirtyeight.com/polls-page/president_primary_polls.csv'
    urllib.request.urlretrieve(url, currDate.strftime("%m") + '-' + currDate.strftime("%d") + '-polls.csv')
    return newFileName;

#Needs work
def currentCandidates():
    with open("cache.json", "r") as file:
        cache = json.load(file)
        with open(cache["currentFile"]) as infile:
            reader = csv.DictReader(infile)

            count = 0
            currPoll = "null"
            cand = []

            while(count < 3):
                row = next(reader)
                if(row['poll_id'] != currPoll):
                    count+=1
                    currPoll = row['poll_id']
                    print(currPoll)
                if row['answer'] not in cand:
                    cand.append(row['answer'])

            print(cand)
            return cand




#checkTime()
#getFile();

currentCandidates()
