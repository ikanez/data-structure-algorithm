"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

all_nums = []

for i in texts:
    all_nums.append(i[0])
    all_nums.append(i[1])

for i in calls:
    all_nums.append(i[0])
    all_nums.append(i[1])

set_nums = set(all_nums)
print("There are",len(set_nums),"different telephone numbers in the records.")