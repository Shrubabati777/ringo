#!/usr/bin/env python3
import os
import requests
from collections import OrderedDict
path = "/data/feedback"
for filenames in os.listdir("/data/feedback"):
        print(filenames)
        with open(os.path.join(path, filenames)) as myfile:
                content = myfile.read().splitlines( )
                dict1 = OrderedDict()
                dict1["title"] = content[0]
                dict1["name"] = content[1]
                dict1["date"] = content[2]
                dict1["feedback"] = content[3]
                #dict = {"title":title , "name":name , "date":date , "feedback":feedback}
                #my_dict = dict(dict1)
                print(dict1)
                response=requests.get("http://34.70.207.251/feedback" , stream=True)
                response=requests.post("http://35.226.200.59/feedback", data=dict1)


