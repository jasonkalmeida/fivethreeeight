import urllib.request

print('Beginning file download with urllib2...')

url = 'https://projects.fivethirtyeight.com/polls-page/president_primary_polls.csv'
urllib.request.urlretrieve(url, 'polls.csv')
