import os
import requests
'''
with open('data.csv') as f:
    reader = csv.reader(f)
    my_list = list(reader)
print("csv to list:",my_list)
'''

url="http://127.0.0.1:5000/upload/"
files = {'upload_file': open('data.csv','rb')}

#print(os.path.getsize('data.csv'))

#headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
x = requests.post(url, files = files)
print(x.text)
