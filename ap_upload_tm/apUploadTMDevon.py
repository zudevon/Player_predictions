import pandas as pd
import json

bssids = pd.read_csv("APs/BSSIDs-Table 1.csv")
sheet1 = pd.read_csv("APs/Sheet1-Table 1.csv")

bssids.columns = ['room', 'name', 'mac', 'bssids', 'del']
del bssids['del']

data = {}
temp_dict = {}
temp_dict2 = []

for i in range(0, 478):

    if pd.notna(bssids['name'][i]):  # check to see if you have an item in the row.

        temp_dict = {}
        temp_dict['ssid'] = bssids['name'][i].replace("id=", "")
        temp_dict['mac_addresses'] = []
        temp_dict['mac_addresses'].append(bssids['mac'][i].replace("base=", ""))
        temp_dict['mac_addresses'].append(bssids['bssids'][i].replace("bssid=", ""))

        while pd.notna(bssids['bssids'][i+1]):
            i += 1

            if i <= 478 and pd.notna(bssids['bssids'][i]):

                temp_dict['mac_addresses'].append(bssids['bssids'][i].replace("bssid=", ""))

            if i == 478:
                break

        temp_dict2.append(temp_dict)

# TURNS TEMP_DICT2 INTO A JSON

# jsonfile = open('file.json', 'w')
#
# json.dump(temp_dict2, jsonfile, indent=4)

sheet1.columns = ['ap_name', 'ssid', 'mac', 'site', 'building', 'room']

data['data'] = []

for i in range(0, 206):

    if i < 73 or i > 99:  # Rows in between have no importance

        if pd.notna(sheet1['ap_name'][i]):  # check to see if you have an item in the row.

            temp_dict = {}

            # created timestamp
            temp_dict['created_timestamp'] = 0

            # add ssid
            temp_dict['ssid'] = sheet1['ap_name'][i]

            # add  addresses
            temp_dict['mac_addresses'] = [sheet1['mac'][i]]

            for item in temp_dict2:
                if item['ssid'] == temp_dict['ssid']:
                    temp_dict['mac_addresses'] += item['mac_addresses']


            # building
            temp_dict['building'] = sheet1['building'][i]

            # description set to a string
            temp_dict['description'] = ""

            # Vereified set to true
            temp_dict['verified'] = True

            # Floors set to a list
            temp_dict['floors'] = []

            # set ip address as a string
            temp_dict['ip_address'] = ""

            # serial  set to a string
            temp_dict['serial'] = ""

            data['data'].append(temp_dict)


jsonfile2 = open('file2.json', 'w')
json.dump(data, jsonfile2, indent=4)