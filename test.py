#!/usr/bin/python

import os
import sys
import hashlib
import requests

hash_object = hashlib.sha256()
hash_object.update(os.environ["UPLOAD_KEY"].encode('utf-8'))
hash_value = hash_object.hexdigest()

print( os.environ["UPLOAD_KEY"] )
print( hash_value )




# Einstellungen
url = 'https://uclibc-ng.tangotanzen.de/'
file_path = "test.py"
api_key = os.environ["UPLOAD_KEY"]

# Datei und Schlüssel als Daten für das Formular vorbereiten
files = {'file': (file_path, open(file_path, 'rb')), 'key': (None, api_key)}

# HTTP-POST-Anfrage senden
response = requests.post(url, files=files)

# Ausgabe der Serverantwort
print(response.text)

