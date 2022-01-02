#!/usr/bin/python3
import json
import os
import logging
from os import close
import sys
from subprocess import call

	
os.system("export GROUP_NUMBER=33")
call(["sudo", "rm", "-r", "CDPS_P2"] )
call(["git", "clone", "https://github.com/nachosmillescas/CDPS_P2"] )
call(["sudo", "apt-get", "install", "python"] )
call(["sudo", "apt-get", "update"] )
call(["sudo", "apt-get", "install", "python3-pip"] )
#os.system("cd CDPS_P2/bookinfo/src/productpage")
os.system("pip3 install -r CDPS_P2/bookinfo/src/productpage/requirements.txt")
os.system("python3 CDPS_P2/bookinfo/src/productpage/productpage_monolith.py 9080")

