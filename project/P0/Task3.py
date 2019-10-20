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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

import pandas as pd

def check_bangalore(num):
  '''
  (080) is the area code for fixed line telephones in Bangalore.
  Fixed line numbers include parentheses, so Bangalore numbers
  have the form (080)xxxxxxx.)
  '''
  import re
  
  match = re.findall(r'\(080\)',num)
  
  if match:
    return 1
  else:
    return 0
   

def check_fixed(num):
  '''
  Fixed lines start with an area code enclosed in brackets. The area
  codes vary in length but always begin with 0
  '''
  import re
  
  match = re.findall(r'\(0', num)
  
  if match:
    return True
  else:
    return False

def check_mobile(num):
  '''
  Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
  '''
  if num[:1] in '789':
        if ' ' in num:
            return True

  return False
          

def check_tele(num):
  '''
   Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.
  '''
  import re
  
  match = re.findall(r'^140',num)
    
  if check_mobile(num) == False and check_fixed(num) == False and match:
    return True
  else:
    return False
        
def identify_codes(num):
    import re
    
    code = ''
    if check_fixed(num):
        code = re.findall(r'\((.*?)\)',num)[0]
    if check_mobile(num):
        code = num[:4]
    if check_tele(num):
        code = '140'
        
    return code

# convert calls to pandas dataframe
calls_df = pd.DataFrame(calls, columns=['a','b','call_dt','duration'])
calls_df['a_bangalore'] = calls_df.a.apply(lambda x: check_bangalore(x))
calls_df['b_bangalore'] = calls_df.b.apply(lambda x: check_bangalore(x))
calls_df['a_codes'] = calls_df.a.apply(lambda x: identify_codes(x))
calls_df['b_codes'] = calls_df.b.apply(lambda x: identify_codes(x))


'''
PART A
'''
code_list = []
called_by_bangalore = calls_df[calls_df.a_bangalore == 1] # caller is from bangalore
code_list = pd.unique(called_by_bangalore.b_codes.values.ravel('K'))

print("The numbers called by people in Bangalore have codes:")
for i in sorted(code_list):
  print(i)


'''
PART B
'''
percentage = 0
banga_a = calls_df[calls_df.a_bangalore == 1]
banga_b = banga_a[banga_a.b_bangalore == 1]
pct =  len(banga_b)/len(banga_a)*100


print(round(pct,2), "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

