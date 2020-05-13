import json
import requests
import platform
if platform.system() == "Windows":
    from Windows_Log import Log
else:
    from Unix_Log import Log
from Base import Sign
from config import config

class Curl():

    def request_json(self,
                     method,
                     url,
                     headers=None,
                     data=None,
                     params=None,
                     sign=True):
        i = 0
        while True:
            i += 1
            if i >= 10:
                    Log.warning(url)
            try:
                if method == "GET":
                    if sign == True:
                        params = Sign(params)
                    r = requests.get(url,headers=headers,params=params)
                    return json.loads(r.text)
                elif method == "POST":
                    if sign == True:
                        data = Sign(data)
                    r = requests.post(url,headers=headers,data=data)
                    return json.loads(r.text)
            except:
                continue