#!/usr/bin/python

import os
import hashlib


hash_object = hashlib.sha256()
hash_object.update(os.environ["UPLOAD_KEY"].encode('utf-8'))
hash_value = hash_object.hexdigest()

print( os.environ["UPLOAD_KEY"] )
print( hash_value )
