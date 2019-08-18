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

import pandas as pd

calls_df = pd.DataFrame.from_records(calls, exclude=['call_dt','duration'], columns = ['a','b','call_dt','duration']) 
texts_df = pd.DataFrame.from_records(texts, exclude=['text_dt'], columns = ['a','b','text_dt'])

combined_dt = pd.concat([calls_df,texts_df])
set_nums = pd.unique(combined_dt[['a', 'b']].values.ravel('K'))

print("There are",len(set_nums),"different telephone numbers in the records.")