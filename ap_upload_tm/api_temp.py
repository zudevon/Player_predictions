# adding in Urls
import requests
import simplejson as json
import base64
from typing import List, Dict, Any
from ap_upload_tm import apUploadTMDevon
from ap_upload_tm import APs


class API(object):
    def __init__(self, username, password, keyspace="devkeyspace", base_url="https://dev-api.degreeanalytics.com"):
        self.username = username
        self.password = password
        self.keyspace = keyspace
        self.base_url = base_url

    def _basic_auth(self):
        return "Basic " + base64.b64encode(("%s:%s" % (self.username, self.password)).encode("latin1")).strip().decode(
            "latin1")

    @property
    def headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": self._basic_auth()
        }

    @classmethod
    def _response(cls, out):
        if out.status_code == 200:
            return (out.json() or {}).get("data")
        raise Exception("{}: {}".format(out.status_code, out.text))

    def _build_url(self, url: str) -> str:
        return self.base_url + url

    def get(self, url: str, params: dict = {}):
        url = self._build_url(url=url)
        return self._response(requests.get(url=url, headers=self.headers, params=params))

    def post(self, url: str, body: Dict[str, Any], params: Dict[str, Any] = None):
        url = self._build_url(url=url)
        return self._response(requests.post(url=url, data=json.dumps(body), params=params, headers=self.headers))

    def put(self, url: str, body: Dict[str, Any], params: Dict[str, Any] = None):
        url = self._build_url(url=url)
        return self._response(requests.put(url=url, data=json.dumps(body), params=params, headers=self.headers))

    def delete(self, url: str):
        url = self._build_url(url=url)
        return self._resonse(requests.delete(url=url, headers=self.headers))


myapi = API(username="devon.rasch@degreeanalytics.com", password="123.Devon")

school_id = "d22a7e00-dca9-4d02-84f6-6d52f73ecd18"
dictionary = apUploadTMDevon.data

for i in apUploadTMDevon.data:

    my_new_ap = myapi.post(url="/api/v1.0/schools/{}/access_points/".format(school_id), body=i)

