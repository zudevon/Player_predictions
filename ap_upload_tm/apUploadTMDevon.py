import pandas as pd
import json
import csv
import sys, getopt


bssids = pd.read_csv("APs/BSSIDs-Table 1.csv")
sheet1 = pd.read_csv("APs/Sheet1-Table 1.csv")
sheet2 = pd.read_csv("APs/Sheet2-Table 1.csv")


bssids.columns = ['room', 'name', 'mac', 'bssids', 'del']
del bssids['del']

# csvfile = open("APs/BSSIDs-Table 1.csv", 'r')
# jsonfile = open('file.json', 'w')
#
# fieldnames = ("1","mac","bssids","4", "5")
# reader = csv.DictReader(csvfile, fieldnames)
# for row in reader:
#     json.dump(row, jsonfile)
#     jsonfile.write('\n')
#
#
# json_data = open('file.json').read()
#
# json_file = json.loads(json_data)

# print(json_file)

print(bssids['name'][0])
# print(bssids[0][0])

print(len(bssids['name'])) # 479 rows in bssids df

print(bssids['name'][1])

import numpy as np

"""
import json

data = {}
data['key'] = 'value'
json_data = json.dumps(data)
"""

for i in range(0, 479):

    if bssids['name'][i] != np.nan:  # check to see if you have an item in the row.

        # add name
        print(bssids['name'][i])
        # add room number from first column
        print(bssids['room'][i])
        # add mac address
        print(bssids['mac'][i])
        # add first bssids
        print(bssids['bssids'][i])

        while bssids['bssids'][i] != np.nan:
            i += 1

            # add all bssid's for this name
            if i < 479:
                if bssids['bssids'][i]:
                    print(bssids['bssids'][i])
            if bssids['bssids'][i] == np.nan:
                break


