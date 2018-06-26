import pandas as pd
import json


def create(output_filename="aps.json"):
    bssids = pd.read_csv("APs/BSSIDs-Table 1.csv")
    sheet1 = pd.read_csv("APs/Sheet1-Table 1.csv")

    bssids.columns = ['room', 'name', 'mac', 'bssids', 'del']
    del bssids['del']

    # get rid of empty rows
    bssids = bssids[pd.notnull(bssids.bssids)]

    # format values
    bssids.name = bssids.name.str.replace("id=", "")
    bssids.bssids = bssids.bssids.str.replace("bssid=", "")
    bssids.mac = bssids.mac.str.replace("base=", "")

    # forward fill so mac address and ap names match up
    bssids = bssids.fillna(method="ffill")

    # combine mac address and ap names to one row
    bssids = bssids.groupby("name", 0).apply(lambda x: list(set(list(x.mac) + list(x.bssids)))).reset_index(name="mac_addresses")

    bssids = bssids.rename(columns={"name": "ap_name"})

    sheet1.columns = ['ap_name', 'ssid', 'mac', 'site', 'building', 'room']

    # get rid of emtpy rows
    sheet1 = sheet1[sheet1.mac.notnull()]
    sheet1 = sheet1[sheet1.mac != "**future"]

    # merge two sheets together
    df_merged = pd.merge(sheet1, bssids, on="ap_name", how="outer")

    # prepare to join mac and mac address to one column
    df_merged.loc[df_merged.mac.isnull(), "mac"] = None
    df_merged.loc[df_merged.mac_addresses.isnull(), "mac_addresses"] = None

    # join and get unique mac addresses
    df_merged.mac_addresses = df_merged.mac.apply(lambda x: [x] if x else []) + df_merged.mac_addresses.apply(lambda x: x if x else [])
    df_merged.mac_addresses = df_merged.mac_addresses.apply(lambda x: list(set(x)))

    df_final = df_merged[["ap_name", "building", "mac_addresses"]]
    df_final = df_final.rename(columns={"ap_name": "ssid"})
    df_final.loc[df_merged.building.isnull(), "building"] = None

    final_json = df_final.to_dict("records")

    json_file = open(output_filename, 'w')
    json.dump(final_json, json_file, indent=4)
    return output_filename

