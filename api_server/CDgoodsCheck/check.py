import flaskimport jsonfrom  flask import requestserver = flask.Flask(__name__)@server.route('/check', methods=['get'])def index():    res ='{"SKU":"7ncBVHa3hN","shopName":"CONVMEUBLE","EAN":"6898055957028","ValidateStatu":1,"ValidateMessage":"验证成功"}'    return json.dumps(res, ensure_ascii=False)    # return json.dumps(res, ensure_ascii=False), 200, {'Content-Type': 'application/json; charset=utf-8'}if __name__ == "__main__":    server.run(port=8082, debug=True, host='172.16.6.203')    # 需要代替的接口 http://openapi.sandbox.winit.com.cn/openapi/service    # "http://127.0.0.1:9900/test"