import flaskimport jsonfrom  flask import requestserver=flask.Flask(__name__)@server.route('/api/asn/v1/batchQuery',methods=['post'])def index():    res ={    "success":True,    "code":0,    "message":"成功",    "data":[        {            "warehouseCode":"42",            "asnNumber":"67",            "asnType":"elit ad do",            "status":"Closed",            "receiveTime":"1978-08-04 06:30:34",            "containerNumber":"6",            "carrier":"ullamco laboris ex",            "warehouseNotes":"voluptate",            "trackingNumber":"86",            "remark":"nulla dolor occaecat",            "sealNumber":"16",            "extAsnNumber":"27",            "refNumber":"54",            "items":[                           {                               "sku": "GLG-AAAB-000036",                               "quantity": 100,                               "sort": 1,                               "putawayedQuantity": 100,                               "expectedQuantity": 100,                               "actualQuantity": 100                           },                           {                               "sku": "GLG-AAAB-000035",                               "quantity": 210,                               "sort": 2,                               "putawayedQuantity": 210,                               "expectedQuantity": 210,                               "actualQuantity":210                           }                ,                           {                               "sku": "GLG-AAAB-000036",                               "quantity": 20,                               "sort": 3,                               "putawayedQuantity": 20,                               "expectedQuantity": 20,                               "actualQuantity":20                           }                       ]        }    ]}    return json.dumps(res, ensure_ascii=False), 200, {'Content-Type': 'application/json; charset=utf-8'}if __name__ == "__main__":    server.run(port=9902, debug=True, host='0.0.0.0')    # 需要代替的接口 "http://uat-us-api.jd.com/routerjson"    # "http://127.0.0.1:9902/fpx"