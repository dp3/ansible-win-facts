#!/usr/bin/env python
# orginal found at https://hindenes.com/trondsworking/2016/11/05/using-ansible-as-a-software-inventory-db-for-your-windows-nodes/

import os
import json

from os import listdir
from os.path import isfile, join

tempfolder = '../roles/facts/files/data/json/'


if not os.path.isdir(tempfolder):
    os.makedirs(tempfolder)

onlyfiles = [f for f in listdir(tempfolder) if isfile(join(tempfolder, f))]

for file in onlyfiles:
    host_name = str(file).replace('.json','') #str(file).split(".")[3] ##designed for hostnames too  I am using ips
    with open(os.path.join(tempfolder, file),'r+') as data_file:
        data = json.load(data_file)
        data['ansible_password'] = ''
        data['ansible_password_ad'] = ''
        data_file.close()
    with open(tempfolder+'/'+file, 'w+') as outfile:  
      json.dump(data, outfile, sort_keys=True, indent=2, separators=(',', ': '))
    outfile.close()
