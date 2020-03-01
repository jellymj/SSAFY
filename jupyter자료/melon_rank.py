from bs4 import BeautifulSoup
import requests
import csv
from pprint import pprint

melon_url = 'https://www.melon.com/chart/index.htm'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
response = requests.get(melon_url, headers = headers).text
data = BeautifulSoup(response, 'html.parser')
songs = data.select('#lst50')

result = []
for song in songs:
    rank = song.select_one('td:nth-child(2) > div > span.rank').text
    title = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    # singer = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    singers = song.select('td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
    item = {'rank':rank, 'title':title, 'singer':','.join([singer.text for singer in singers])}
    result.append(item)

with open('melon_rank.csv', 'w', encoding = 'utf-8', newline='') as csvfile:
    fieldnames = ['rank', 'title', 'singer']
    csv_writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    csv_writer.writeheader()
    for item in result:
        csv_writer.writerow(item)