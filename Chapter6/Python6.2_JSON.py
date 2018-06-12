import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('test')
log.info("init")

import json

data = {'name': 'eeeee', 'id': "rrer"}
jstr = json.dumps(data)
log.info(jstr)
data2 = json.loads(jstr)
log.info(data2)
# 写json数据
with open('data.json', 'w') as f:
    json.dump(data, f)
# 读json数据
with open('data.json', 'r') as f2:
    log.info(json.load(f2))

from urllib import request
from pprint import pprint

# import json
#
# req=request.Request('http://172.23.4.111:6385/v1/drivers')
req = request.Request('http://172.23.4.111:6385/v1/nodes/647156c2-092c-44af-a4c2-e300804d3722')
# http://172.23.4.111:6385/v1/nodes/647156c2-092c-44af-a4c2-e300804d3722
resp = request.urlopen(req)

s1 = resp.read().decode("utf-8")
# pprint(" re: "+s1)
print(type(s1))
d1 = json.loads(s1)
#pprint(d1)
print(type(d1))
# 写json数据
with open('data2.json', 'w') as f:
    json.dump(d1, f)
# 读json数据
with open('data2.json', 'r') as f2:
    log.info(json.load(f2))
if __name__ == "__main__":
    log.info("end")
