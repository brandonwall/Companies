#!/usr/bin/env python
import sys
import os

x = input('Enter Graph Number:')
path = '~/Documents/GitHub/Companies/spiders/Webscrapers/'
file = "json_to_table.py"


os.system("python " + path +file +" %d" %x)

