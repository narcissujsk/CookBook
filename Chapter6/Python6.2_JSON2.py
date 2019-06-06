import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('test')
log.info("init")

import json

data = {'name': 'eeeee', 'id': "rrer","meta":{"admin_pass":"123456Pw"}}
jstr = json.dumps(data)
log.info(jstr)
log.info(data["name"])
meta=data["meta"]
log.info(meta["admin_pass"])

if __name__ == "__main__":
    log.info("end")
