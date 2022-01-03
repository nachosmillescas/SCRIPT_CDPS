#!/usr/bin/python3
import json
import os
import logging
from os import close
import sys
from subprocess import call

def modifHTML():
  h=open("practica_creativa2/bookinfo/src/productpage/templates/productpage.html", "r")
  aux=open("practica_creativa2/bookinfo/src/productpage/templates/auxiliar.html", "w+")
  formato=os.environ.get('GROUP_NUMBER')
  blockTitle = "{% block title %}"
  endBlock = "{% endblock %}"
  for line in h:
    if "block title" in line:
     aux.write(blockTitle + "{}".format(formato) + endBlock "\n")
    else:
      aux.write(line)
  for line in aux:
    h.write(line)
  h.close()
  aux.close()
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
  os.system("pip3 install -r practica_creativa2/bookinfo/src/productpage/requirements.txt")
  modifHTML()
  os.system("python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py 9080")

funcion()

