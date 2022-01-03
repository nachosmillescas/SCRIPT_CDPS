#!/usr/bin/python3
import json
import os
import logging
from os import close
import sys
from subprocess import call


def funcion(): 
  
  #set GROUP_NUMBER="Equipo 33" 
  #os.system( """export GROUP_NUMBER="33"""")
  os.environ['GROUP_NUMBER']="33"
  os.system("printenv GROUP_NUMBER")
  call(["sudo", "rm", "-r", "CDPS_P2"] )
  call(["git", "clone", "https://github.com/CDPS-ETSIT/practica_creativa2.git"] )
  call(["sudo", "apt-get", "install", "python"] )
  call(["sudo", "apt-get", "update"] )
  call(["sudo", "apt-get", "install", "python3-pip"] )
  os.system("pip3 install -r CDPS_P2/bookinfo/src/productpage/requirements.txt")
  modifHTML()
  os.system("python3 CDPS_P2/bookinfo/src/productpage/productpage_monolith.py 9080")

funcion()
def modifHTML():
  h=open("CDPS_P2/bookinfo/src/productpage/templates/productpage.html", "r")
  aux=open("CDPS_P2/bookinfo/src/productpage/templates/auxiliar.html", "w+")
  for line in h:
    if "{% block title %}Simple Bookstore App{% endblock %}" in line:
     aux.write("{% block title %}{}{% endblock %}".format(os.environ.get('GROUP_NUMBER')))
    else:
      aux.write(line)
  for line in aux:
    h.write(line)
  h.close()
  aux.close()
