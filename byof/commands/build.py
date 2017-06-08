import json
from types import SimpleNamespace as Namespace

data = None
with open('simple.json') as f:
    for line in f:
        data = (json.loads(line))

data = json.dumps(data)

x = json.loads(data, object_hook=lambda d: Namespace(**d))

print (x.hometown[1].name)