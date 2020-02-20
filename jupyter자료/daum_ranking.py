from bs4 import BeautifulSoup
import requests
from pprint import pprint
import csv

response = requests.get('https://www.daum.net/').text
# print(response)
data = BeautifulSoup(response, 'html.parser')
# print(data)
rankings = data.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li > div > div:nth-child(2) > span.txt_issue > a')
# pprint(rankings)

result_dict = {}
result_list = []
for idx, ranking in enumerate(rankings, 1):
    # print(f'{idx}위:{ranking.text}')
    # result_dict[f'{idx}위'] = ranking.text
    result_dict = {'rank':f'{idx}위', 'ranker':ranking.text}
    result_list.append(result_dict)
pprint(result_dict)

with open('daum_rank.csv', 'w', encoding ='utf-8', newline='') as csvfile:
    #저장할 데이터들의 필드 이름을 미리 지정한다.(딕셔너리의 key이름과 일치해야 한다.)
    fieldnames = ['rank', 'ranker']
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in result_list:
        csv_writer.writerow(item)