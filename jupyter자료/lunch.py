import csv

lunch = {
    '양자강' : '02-111-2222', 
    '김밥카페' : '02-333-4444',
    '순남시래기' : '02-555-6666',
}

# csvfile = open('lunch.csv', 'w', newline='', encoding='utf-8')
# csv_writer = csv.writer(csvfile)
# for item, number in lunch.items():
#     csv_writer.writerow([item, number])
# csvfile.close()

with open('lunch.csv', 'w', newline='', encoding = 'utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    for item, number in lunch.items():
        csv_writer.writerow([item. number])
