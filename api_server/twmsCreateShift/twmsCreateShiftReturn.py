import flask
import json
from  flask import request
server=flask.Flask(__name__)


@server.route('/ewms-api-server/api/ewms-goods-shift/doDepotIn',methods=['post'])
def index():
    print('请求参数{0}'.format(request.json))
    data=request.json
    sft=data['shiftCode']
    res={
    "targetUrl": None,
    "errorInfos": None,
    "result": {
        "success": True,
        "result":
            {
                "shipmentId": "RVG1149-210424-0013",
                "shiftCode": sft
            }
        ,
        "code": 0,
        "message": None
    },
    "success": True,
    "authorizedRequest": False
}

    # return json.dumps(res, ensure_ascii=False)
    return json.dumps(res, ensure_ascii=False),200, {'Content-Type': 'application/json; charset=UTF-8'}

if __name__=='__main__':
    server.run(port=9097, debug=True, host='0.0.0.0')

