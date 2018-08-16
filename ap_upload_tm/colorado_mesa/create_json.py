import pandas as pd
import json


def create(output_filename="aps.json"):
    # Turn CSV's into Pandas DataFrames
    all_ap_names = pd.read_csv('aps.txt', header=None)
    aps = pd.read_csv("cmu_aps.csv")
    build_codes = pd.read_csv('colorado_mesa_building_names - Sheet3.csv')

    # Change column names
    all_ap_names.columns = ['name']
    aps.columns = ['name', 'model', 'part', 'phy', 'ch', 'xmit_dbm', 'ga_in_dbm', 'mac_addresses', 'switch', 'port']

    # Merge and create final data frame
    df_final = aps[['name', 'mac_addresses']]
    df_final = pd.merge(df_final, all_ap_names, on='name', how='outer')
    df_final['building'] = (df_final['name']).str.slice(4)

    # Filter ap_nicknames
    building = []
    for word in df_final['building']:
        for i, letter in enumerate(word):
            if letter.isdigit() or letter.isupper() or letter == "_":
                building.append(word[0:i])
                break
        else:
            building.append(word)
    df_final["building"] = building
    df_final = df_final.fillna(0)

    # Change all of the building name to match building codes
    for row in build_codes.iterrows():
        (df_final.building)[df_final['building'] == row[1][0]] = row[1][1]

    # Create JSON
    df_final = df_final.rename(columns={"name": "ssid"})
    final_json = df_final.to_dict("records")

    # delete keys that have no mac value
    for item in (d for d in final_json):
        if item['mac_addresses'] == 0:
            del item['mac_addresses']

    # turn every mac_addresses value into a list per format
    for i in range(0, len(final_json)):
        if final_json[i].get('mac_addresses'):
            final_json[i]['mac_addresses'] = [final_json[i]['mac_addresses']]

    json_file = open(output_filename, 'w')
    json.dump(final_json, json_file, indent=4)

    return output_filename




