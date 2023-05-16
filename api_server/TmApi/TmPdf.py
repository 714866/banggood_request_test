import flask
import json

import time

import requests
from  flask import request
server=flask.Flask(__name__)

@server.route('/test',methods=['POST'])
def index():
    raise requests.Timeout('Connection timed out.')

    time.sleep(60*3)

    res ={"response":{"content":1}}


    return json.dumps(res, ensure_ascii=False), 200, {'Content-Type': 'application/json; charset=utf-8'}


if __name__ == "__main__":
    server.run(port=9101, debug=True, host='0.0.0.0')
    # 需要代替的接口 "http://uat-us-api.jd.com/routerjson"
    # ""http://127.0.0.1:9101/test