import flask
import json
from  flask import request
server=flask.Flask(__name__)

@server.route('/fpx',methods=['post'])
def index():
    res ={
    "result":"1",
    "msg":"系统处理成功",
    "data":{

        "consignment_no": "IC90027818050352",
        "4px_tracking_no": ""

    }
}
    return json.dumps(res, ensure_ascii=False), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == "__main__":
    server.run(port=9902, debug=True, host='0.0.0.0')
    # 需要代替的接口 "http://uat-us-api.jd.com/routerjson"
    # "http://127.0.0.1:9902/fpx"