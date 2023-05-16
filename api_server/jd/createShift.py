import flask
import json
server=flask.Flask(__name__)


@server.route('/jd',methods=['post'])
def index():
    # res={'msg':'cccccc','msg_code':0}
    res={
    "response":{
        "content":{
            "data":"FS20217L158709820781",
            "errorCode":200,
            "errorMsg":"操作成功",
            "failed":False,
            "success":True
        },
        "code":0
    }
    }
    # x = "some data you want to return"
    # return json.dumps(res,ensure_ascii=False), 200, {'Content-Type': 'text/css; charset=utf-8'}
    return json.dumps(res,ensure_ascii=False), 200, {'Content-Type': 'application/json; charset=utf-8'}
    # return json.dumps(res,ensure_ascii=False)


if __name__=="__main__":
    server.run(port=9777, debug=True, host='0.0.0.0')
    # "http://127.0.0.1:9777/jd"
    # http://uat-us-api.jd.com/routerjson