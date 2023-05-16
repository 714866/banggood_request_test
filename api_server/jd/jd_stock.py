import flask
import json
server=flask.Flask(__name__)


@server.route('/jd',methods=['post'])
def index():
    # res={'msg':'cccccc','msg_code':0}
    res={
    "response":{
        "content":{
            "data":{
                "page":1,
                "pageSize":10000,
                "pages":0,
                "rows":[
                    {
                        "batchNo":"1_1_C0000000065_FG0000009837_20201230_1609315990447",
                        "batchType":-1,
                        "batchTypeName":"非指定批次类型",
                        "cargoOwnerId":7744,
                        "cargoOwnerName":"欧洲测试商家GDPR-FOP",
                        "createTime":1609316151000,
                        "createUser":"jdhk_VNWhuidwHRAX",
                        "customerCode":"KH20000000202",
                        "goodsCode":"FG0000009837",
                        "id":223,
                        "level":100,
                        "levelName":"良品 - Good",
                        "lockNum":0,
                        "preemptNum":0,
                        "sku":"POA1811899",
                        "skuName":"真京东仓下发有库存产品",
                        "stockNum":202,
                        "tenantCode":"",
                        "updateUser":"jdhk_VNWhuidwHRAX",
                        "warehouseCode":"WMS0001",
                        "warehouseName":"C0000000065"
                    },{
                        "batchNo":"1_1_C0000000065_FG0000009837_20201230_1609315990447",
                        "batchType":-1,
                        "batchTypeName":"非指定批次类型",
                        "cargoOwnerId":7744,
                        "cargoOwnerName":"欧洲测试商家GDPR-FOP",
                        "createTime":1609316151000,
                        "createUser":"jdhk_VNWhuidwHRAX",
                        "customerCode":"KH20000000202",
                        "goodsCode":"FG0000009837",
                        "id":223,
                        "level":210,
                        "levelName":"残品- Good",
                        "lockNum":0,
                        "preemptNum":0,
                        "sku":"POA1811899",
                        "skuName":"真京东仓下发有库存产品",
                        "stockNum":300,
                        "tenantCode":"",
                        "updateUser":"jdhk_VNWhuidwHRAX",
                        "warehouseCode":"WMS0001",
                        "warehouseName":"C0000000065"
                    }
                ],
                "total":2
            },
            "errorCode":200,
            "errorMsg":"操作成功",
            "failed":False,
            "success":True
        },
        "code":0
    }
}
    return json.dumps(res,ensure_ascii=False), 200, {'Content-Type': 'application/json; charset=utf-8'}


if __name__=="__main__":
    server.run(port=9779, debug=True, host='0.0.0.0')