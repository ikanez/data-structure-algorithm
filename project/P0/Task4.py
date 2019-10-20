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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# convert calls to pandas dataframe
import pandas as pd

calls_df = pd.DataFrame(calls, columns=['a','b','call_dt','duration'])
texts_df = pd.DataFrame(texts, columns=['a','b','text_dt'])

# combine all non callers + texters
non_call_maker_df = calls_df.b 
non_call_maker_df.append(texts_df.a)
non_call_maker_df.append(texts_df.b)

# calculate uniqueness of callers and non callers
call_maker_ls = calls_df.a.unique()
non_call_maker_ls = non_call_maker_df.unique()

# find difference between two sets
diff = set(call_maker_ls).difference(set(non_call_maker_ls))
list_tele = sorted(list(diff))

# print
print("These numbers could be telemarketers: ")
for i in list_tele:
    print(i)