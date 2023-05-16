import flask
import json
from  flask import request

server = flask.Flask(__name__)


@server.route('/express/transfer/createTransfer', methods=['post'])
def index():
    res = {
  "code": 200,
  "msg": "成功",
  "data": [
    {
      "transferId": "SFT-A1-20201013-86884A",
      "boxId": "FBOX-20201021-18002",
      "label": None,
      "labelUrl": "https://yoms.lg2w.cn/file/download?fileUrl=/20210811/78e7f3f5f0ae4d3381d5b4018c79654d.pdf",
      "masterTrackingId": "1Z2V756Y6828692645",
      "traceId": "1Z2V756Y6828692645",
      "message": None
    },    {
      "transferId": "SFT-A1-20201013-86884A",
      "boxId": "FBOX-20201021-18004",
      "label": None,
      "labelUrl": "https://yoms.lg2w.cn/file/download?fileUrl=/20210811/78e7f3f5f0ae4d3381d5b4018c79654d.pdf",
      "masterTrackingId": "1Z2V756Y6828692645",
      "traceId": "1Z2V756Y68286926455!@$%%^&^&**())",
      "message": None
    }
  ]
}



    return json.dumps(res, ensure_ascii=False), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == "__main__":
    server.run(port=8881, debug=True, host='172.16.6.203')

