#!/usr/bin/env python3

import redis
import json

r = redis.StrictRedis(host='localhost', port=6379, db=0)
key = 'ansible_facts' + 'ansible1' # ansible1 is a hostname
val = r.get(key)

data = json.loads(val)
print (data['ansible_memfree_mb'])
