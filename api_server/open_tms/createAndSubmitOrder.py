import flaskimport jsonfrom  flask import requestserver=flask.Flask(__name__)@server.route('/createAndSubmitOrder',methods=['post'])def index():    res={"code":200,"msg":"服务错误:创建并提交物流单异常：未找到物流产品信息,请检查服务代码!!!","data":{        "itemArr":[{            "traceId":123,            "labelUrl":"www.baidu.com",            "labelType":'2',            "mainNumber":777        }],        "totalFreight":222,        "freightCurrency":56456    },"success":True}    return json.dumps(res,ensure_ascii=False)@server.route('/lbs/delivery/baseCos',methods=['post'])def order():    res={    "code": 200,    "msg": "成功",    "data": {        "orderId": "A0005619110100QV",        "currencyType": "CNY",        "shortening": "RU",        "countryId": "18S6",        "postTypeFeeslist": [            {                "postTypeName": "无忧物流（带电）",                "postType": "275",                "message": None,                "packageType": "Package",                "fees": 1311.3268,                "originFees": 1311.3268,                "originCurrency": "CNY",                "sortCode": 0,                "feesBigTypeDetails": [                    {                        "feesBigType": 1,                        "feesBigTypeName": "运费",                        "fees": 1311.3268                    }                ],                "carrierCostPrice": 1311.3268,                "versionCode": "275-V89",                "chargeType": None,                "chargeTypeName": None,                "pass": True            },{                "postTypeName": "DHL特价",                "postType": "276",                "message": None,                "packageType": "Package",                "fees": 49.3268,                "originFees": 1311.3268,                "originCurrency": "CNY",                "sortCode": 0,                "feesBigTypeDetails": [                    {                        "feesBigType": 1,                        "feesBigTypeName": "运费",                        "fees": 50.3268                    }                ],                "carrierCostPrice": 1311.3268,                "versionCode": "275-V89",                "chargeType": None,                "chargeTypeName": None,                "pass": False            },{                "postTypeName": "2号France Express(colissimo)",                "postType": "277",                "message": None,                "packageType": "Package",                "fees": 50.3268,                "originFees": 1311.3268,                "originCurrency": "CNY",                "sortCode": 0,                "feesBigTypeDetails": [                    {                        "feesBigType": 1,                        "feesBigTypeName": "运费",                        "fees": 50.3268                    }                ],                "carrierCostPrice": 1311.3268,                "versionCode": "275-V89",                "chargeType": None,                "chargeTypeName": None,                "pass": True            },         {                "postTypeName": "无忧物流（带电）",                "postType": "275",                "message": "国家限制通邮表中,渠道限制该国家通邮",                "packageType": "Package",                "fees": 0,                "originFees": 0,                "originCurrency": None,                "sortCode": 0,                "feesBigTypeDetails": None,                "carrierCostPrice": 0,                "feesDetails": None,                "versionCode": None,                "chargeType": None,                "chargeTypeName": None,                "pass": False            }        ],        "postLimitInfo": None    },    "success": True}    return json.dumps(res,ensure_ascii=False)if __name__ == "__main__":    server.run(port=9902, debug=True, host='0.0.0.0')    # 需要代替的接口 http://openapi.sandbox.winit.com.cn/openapi/service    # "http://127.0.0.1:9900/test"