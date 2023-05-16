import flask
import json
server=flask.Flask(__name__)


@server.route('/index',methods=['post'])
def index():
    # res={'msg':'cccccc','msg_code':0}
    res={
  "targetUrl": "/ods-service/api/lable/postLable",
  "errorInfos": [
    {
      "code": 500,
      "msg": "Remote service error failed statusq2132",
      "details": [
        "com.banggood.ods.modular.channel.controller.LabelController : postLabel : 36",
        "com.banggood.ods.modular.channel.controller.LabelController$$FastClassBySpringCGLIB$$110ee9c9 : invoke : -1"
      ],
      "validationErrorInfos": None
    }
  ],
  "result": None,
  "success": False,
  "authorizedRequest": False
}
    return json.dumps(res,ensure_ascii=False)


if __name__=="__main__":
    server.run(port=7777, debug=True, host='0.0.0.0')