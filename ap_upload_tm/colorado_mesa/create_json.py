import pandas as pd
import json


def create(output_filename="aps.json"):
    aps = pd.read_csv("cmu_aps.csv")
    aps.columns = ['name', 'model', 'part', 'phy', 'ch', 'xmit_dbm', 'ga_in_dbm', 'mac', 'switch', 'port']
    df_final = aps[['name', 'mac']]
    df_final = df_final.rename(columns={"name": "ssid"})
    final_json = df_final.to_dict("records")

    json_file = open(output_filename, 'w')
    json.dump(final_json, json_file, indent=4)
    return output_filename



