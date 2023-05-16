import flask
import json
server=flask.Flask(__name__)


@server.route('/index',methods=['post'])
def index():
    # res={'msg':'cccccc','msg_code':0}
    res={
  "targetUrl": "/ods-service/api/lable/postLable",
  "data":
    {
      "label_url": "http://gzfastdfs.banggood.cn/fast/download?fileUrl=group1/M00/73/B8/rB9kml8NWhmAbz5hAAEdcNv5_iU122.pdf"
    }
  ,
  "result": 1,
  "status": "U",
  "msg": "系统处理成功"
}
    return json.dumps(res,ensure_ascii=False)


if __name__=="__main__":
    server.run(port=7777, debug=True, host='0.0.0.0')