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

"""

data = {}
data['key'] = 'value'
json_data = json.dumps(data)

"""

tm_aps = {}
data = {}


for i in range(0, 478):

    temp_dict = {}
    temp_dict2 = {}


    if pd.notna(bssids['name'][i]):  # check to see if you have an item in the row.

        # per name of bssid dictioinary put all the mac addresses as a list in the new dictionary
        # match the name and add all mac addresses to the dictionary already created

        temp_dict = {}

        # created timestamp
        temp_dict['created_timestamp'] = 0

        # add ssid
        temp_dict['ssid'] bssids['ap_name'][i]

        # add  addresses
        temp_dict['mac_addresses'] = []
        temp_dict['mac_addresses'].append(bssids['mac'][i])
        # print(bssids['room'][i])

        # add mac address
        temp_dict['mac'] = sheet1['mac'][i]
        # print(bssids['mac'][i])

        # building
        temp_dict['building'] = sheet1['ssid'][i]

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

        temp_dict['mac_addresses'] = bssid_list

        data['data'] = tm_aps[name] = temp_dict

# print(tm_aps)
# print(temp_dict)

tm_ap_json = json.dumps(tm_aps)
# print(tm_ap_json)

jsonfile = open('file.json', 'w')

# json.dump(dictionary, file_to_write_to, indent=4)

json.dump(tm_aps, jsonfile, indent=4)

"""---------------- next shhet "sheet 1 " -----------------"""

sheet1.columns = ['ap_name', 'ssid', 'mac', 'site', 'building', 'room']

data = {}
data['data'] = []

for i in range(0, 206):

    if i < 73 or i > 99:

        if pd.notna(sheet1['ap_name'][i]):  # check to see if you have an item in the row.

            temp_dict = {}

            # created timestamp
            temp_dict['created_timestamp'] = 0

            # add ssid
            temp_dict['ssid'] = sheet1['ap_name'][i]

            # add  addresses
            temp_dict['mac_addresses'] = [sheet1['mac'][i]]
            # print(bssids['room'][i])

            # add mac address
            temp_dict['mac'] = sheet1['mac'][i]
            # print(bssids['mac'][i])

            # building
            temp_dict['building'] = sheet1['ssid'][i]

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


# jsonfile2 = open('file2.json', 'w')
#
# json.dump(data, jsonfile2, indent=4)