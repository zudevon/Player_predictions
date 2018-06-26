import simplejson as json
from datetime import datetime

from create_json import create
from api import API
from settings import USERNAME, PASSWORD, KEYSPACE, BASE_API_URL, SCHOOL_ID


if __name__ == "__main__":
    # create json
    ap_json_file = create()

    myapi = API(username=USERNAME, password=PASSWORD, keyspace=KEYSPACE, base_url=BASE_API_URL)

    with open(ap_json_file) as f:
        aps = json.load(f)

    start_time = datetime.utcnow()
    for index, i in enumerate(aps):
        if index % 25 == 0:

            print("Uploaded {0} APs Successfully. Total Time: {1}".format(index, datetime.utcnow() - start_time))

        try:
            if i["building"] is None:
                i.pop("building")

            my_new_ap = myapi.post(url="/api/v1.0/schools/{}/access_points/".format(SCHOOL_ID), body=i)
        except Exception as e:
            print("ERROR CODE: Index: {0} \t Failed with {1} \t Message: {2}".format(index, i, str(e)))

    print("All APs Uploaded. Total Time: {0}".format(datetime.utcnow() - start_time))

