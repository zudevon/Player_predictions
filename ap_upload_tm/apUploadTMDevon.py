import pandas as pd
import json
import csv
import sys, getopt


bssids = pd.read_csv("APs/BSSIDs-Table 1.csv")
sheet1 = pd.read_csv("APs/Sheet1-Table 1.csv")
sheet2 = pd.read_csv("APs/Sheet2-Table 1.csv")


bssids.columns = ['room', 'name', 'mac', 'bssids', 'del']
del bssids['del']

print(bssids['name'][0])
# print(bssids[0][0])

print(len(bssids['name'])) # 479 rows in bssids df

import numpy as np

"""

data = {}
data['key'] = 'value'
json_data = json.dumps(data)

"""
counter = 0
tm_aps = {}
data = {}


for i in range(0, 478):

    temp_dict = {}
    temp_dict2 = {}


    if pd.notna(bssids['name'][i]):  # check to see if you have an item in the row.

        # add name
        name = bssids['name'][i]
        # print(bssids['name'][i])

        # add room number from first column
        temp_dict['room'] =  bssids['room'][i]
        # print(bssids['room'][i])

        # add mac address
        temp_dict['mac'] = bssids['mac'][i]
        # print(bssids['mac'][i])

        # add first bssids
        bssid_list = []
        bssid_list.append(bssids['bssids'][i])

        # print(bssids['bssids'][i])

        while pd.notna(bssids['bssids'][i+1]):
            i += 1

            # add all bssid's for this name
            if i <= 478 and pd.notna(bssids['bssids'][i]):

                bssid_list.append(bssids['bssids'][i])
                # print(bssids['bssids'][i])

            if i == 478:
                break

        temp_dict['bssids'] = bssid_list

        counter += 1

        tm_aps[name] = temp_dict

# print(tm_aps)
# print(temp_dict)

tm_ap_json = json.dumps(tm_aps)
# print(tm_ap_json)

jsonfile = open('file.json', 'w')

# json.dump(dictionary, file_to_write_to, indent=4)

json.dump(tm_aps, jsonfile, indent=4)
