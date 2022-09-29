#!/usr/bin/env python3

#used the code that was displayed in the lab

import os 
import json

#create an empty directory 
env = {}

for env_key, env_value in os.environ.items():
    env[env_key] = env_value


print ("Content Type: application/json")
print()
print(json.dumps(env))