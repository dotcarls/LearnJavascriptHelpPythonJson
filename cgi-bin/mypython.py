#!/usr/bin/env python3

import cgi
import json
import sys

form = cgi.FieldStorage()
result = {}
result['success'] = True
result['message'] = "It worked!"
result['keys'] = ','.join(form.keys())

data = {}
for key in form.keys():
	data[key] = form.getvalue(key)

result['data'] = data

sys.stdout.write("Content-Type: application/json\n\n")
sys.stdout.write(json.dumps(result, indent=1))
sys.stdout.write("\n")
sys.stdout.close()

