import random
import string
import time

import flask
import json
from flask import request

server = flask.Flask(__name__)


@server.route('/lbs/delivery/baseCost', methods=['post'])
def index():
    res = {"code": 200, "msg": "成功",
           "data": {"orderId": "A000092108180003", "currencyType": "CNY", "shortening": "AO", "countryId": "5",
                    "postTypeFeeslist": [  {
        "postTypeName": "ZY美国专线",
        "postType": "112",
        "message": None,
        "packageType": "Package",
        "fees": 204.12,
        "sortCode": 0,
        "formular": "(4.536*45.0) + 0=204.12",
        "maxWeight": "",
        "entype": "ZY-US",
        "hasSignForFeedback": "1",
        "hasTrackingChannelTrader": "1",
        "ageValue": "",
        "zoneName": "美国",
        "ageName": "",
        "logisticsChanneltype": "专线",
        "feesDetails": [
          {
            "feesName": "基础运费",
            "iscost": True,
            "remark": None,
            "price": 204.12,
            "proportion": 1,
            "formular": "(4.536*45.0)",
            "defaultChargeArea": False,
            "computeType": 1,
            "currency": "CNY",
            "postTraderId": None,
            "weight": 4.536,
            "discount": False,
            "zoneName": "美国",
            "countThrow": True,
            "countThrowScale": 6000
          },
          {
            "feesName": "挂号费",
            "iscost": False,
            "remark": "计重区间有重复或未设置价格，请检查:挂号费",
            "price": 0,
            "proportion": 1,
            "formular": "0",
            "defaultChargeArea": False,
            "computeType": 0,
            "currency": None,
            "postTraderId": None,
            "weight": 4.536,
            "discount": False,
            "zoneName": "美国",
            "countThrow": True,
            "countThrowScale": 6000
          }
        ],
        "postTypeLongWideHeightLimitMeter": "方形:长≤120,方形:(宽+高)*2+长≤274,",
        "pass": True
      }], "postLimitInfo": None}, "success": True}

    # return json.dumps(res, ensure_ascii=False)
    # print(1)
    # return json.dumps(res, ensure_ascii=False), 200, {'Content-Type': 'application/json; charset=utf-8'}

    return json.dumps(res, ensure_ascii=False)

@server.route('/express/carrier/newCreateOrder', methods=['post'])
def post_label():
    # res = {
    #     "createTime":time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),
    #     "updateTime":time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),
    #     "trackNo":''.join(random.choices(string.ascii_uppercase+string.digits,k=6)),
    #     "postId":112,
    #     "expressURL":"",
    #     "specialLableUrl":"",
    #     "invoiceUrl":"http://gzfastdfs.banggood.cn/fast/download?fileUrl=2023-05-09/c4f2e2ef-c632-4bd6-ab30-0eeb431e3c89.pdf",
    #     "expressSize":1,
    #     "wayBillNo":''.join(random.choices(string.ascii_uppercase+string.digits,k=7)),
    #     "orderId":"A000092108180003",
    #     "weight":"3",
    #     "weight":"3",
    # }
    res = {
        "msg": "成功",
        "code": 200,
        "data": {
            "id": 114918621,
            "trackNo": "LXBTH000116140702",
            "postId": "1015",
            "expressURL": "http://gzfastdfs.banggood.cn/fast/download?fileUrl=2023-05-10/02b59383-75e9-4872-a0a8-43878305b9fb.pdf",
            "expressType": 1,
            "message": "null-&gt;Lazada-泰国陆运st（特）:Lazada-泰国陆运st（特）",
            "orderId": "A000092108180003",
            "weight": "0.428",
            "shipmentId": "FP001712100067989",
            "hasDb": False,
            "pushType": "tms",
            "notUpload": False,
            "carrierNo": "697823711488945"

        }
    }



    # return json.dumps(res, ensure_ascii=False)
    # print(1)
    # return json.dumps(res, ensure_ascii=False), 200, {'Content-Type': 'application/json; charset=utf-8'}

    return json.dumps(res, ensure_ascii=False),200,{'Content-Type': 'application/json; charset=utf-8'}



if __name__ == "__main__":
    server.run(port=8081, debug=True, host='172.16.6.203')
    # 需要代替的接口 http://lbs.banggood.cn/api/billbing/postBilling
    #http://172.16.6.203:8081/lbs/delivery/baseCost
