"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


import pandas as pd

call_df = pd.DataFrame(calls, columns = ['caller','callee','call_dt','duration']) 
call_df.duration = [int(i) for i in call_df.duration]

caller_profile = pd.DataFrame()
caller_profile['number'] = call_df.caller
caller_profile['duration'] = call_df.duration

callee_profile = pd.DataFrame()
callee_profile['number'] = call_df.callee
callee_profile['duration'] = call_df.duration

call_profile = pd.concat([caller_profile, callee_profile], ignore_index=True)
tt = call_profile.groupby('number').sum().sort_values('duration', ascending=False).reset_index()

print(tt.number[0],"spent the longest time", tt.duration[0] ,"seconds, on the phone during September 2016.")
