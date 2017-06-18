#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
myserial = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

# On crée une application Twitter depuis https://apps.twitter.com
# puis ci dessous on tape les clés récupérées sur l'application Twitter.
CONSUMER_KEY = 'xxx'  # A ADAPTER
CONSUMER_SECRET = 'xxx'  # A ADAPTER
ACCESS_KEY = 'xxx'  # A ADAPTER
ACCESS_SECRET = 'xxx'  # A ADAPTER
# Pour utiliser Twython, il faut installer (sudo apt-get install) :
# sous Python 2.7 : python-twython / python-oauth / python-oauth2client / python-oauthlib / python-requests-oauthlib
# sous Python 3 : python3-twython / python3-oauth / python3-oauth2client / python3-oauthlib / python3-requests-oauthlib
from twython import Twython ,TwythonError
twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

nomFichier = '/home/pi/3615/minitel.txt'

########################################################################

def ajoutDansFichier(data):
    try:
        objetFichier = open(nomFichier,'a')
        objetFichier.write(data+"\n")
        objetFichier.close()
    except:
        return 0

########################################################################

try:
    myserial.open()
except serial.SerialException as e:
    print (e)

try:
    while True:
        data = myserial.readline()
        data = data[0:len(data)-2]  # Pour enlever le retour chariot
        data = data.decode('latin_1')
        if data != '':
            try:
                ajoutDansFichier(data)
                twitter.update_status(status=data)
            except TwythonError as e:
                print (e)
except KeyboardInterrupt:
    myserial.close()

########################################################################
