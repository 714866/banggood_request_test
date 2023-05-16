import string
import random

import flask
import json

from flask import request


from werkzeug.routing import BaseConverter


# 定义自己的转换器，继承于BaseConvert类
# class RegexConverter(BaseConverter):
#     def __init__(self, url_map, regex):
#         # 调用父类的构造方法
#         super().__init__(map=url_map)
#         # 将正则表达式的参数保存到对象的属性中，flask会去使用这个属性来进行路由的正则匹配
#         self.regex = regex


# 将自定义的转换器添加到flask的应用中
server = flask.Flask(__name__)
# server.url_map.converters['re'] = RegexConverter

@server.route('/fba/inbound/v0/plans', methods=['post'])
def index():
    # res={'msg':'cccccc','msg_code':0}
    order_id = request.values.get('orderId')
    id ="FBA"+''.join(random.choices(string.ascii_uppercase+string.digits,k=9))
    res = {
        "payload": {
            "InboundShipmentPlans": [
                {
                    "ShipmentId": id,
                    "DestinationFulfillmentCenterId": "BHX4",
                    "ShipToAddress": {
                        "Name": "AmazonFulfillmentCenter",
                        "AddressLine1": "Plot1,LyonsPark,",
                        "AddressLine2": "SayerDr",
                        "City": "Coventry",
                        "StateOrProvinceCode": "WestMidlands",
                        "CountryCode": "GB",
                        "PostalCode": "CV59PF"
                    },
                    "LabelPrepType": "SELLER_LABEL",
                    "Items": [
                        {
                            "SellerSKU": "Xzesode54724*",
                            "FulfillmentNetworkSKU": "X001OB2AKP",
                            "Quantity": 109
                        }

                        ,            {
                            "SellerSKU": "Xzesode54738*",
                            "FulfillmentNetworkSKU": "X001OB14RF",
                            "Quantity": 7
                        }
                    ],
                    "EstimatedBoxContentsFee": {
                        "TotalUnits": 20,
                        "FeePerUnit": {
                            "CurrencyCode": "GBP",
                            "Value": 0.12
                        },
                        "TotalFee": {
                            "CurrencyCode": "GBP",
                            "Value": 2.4
                        }
                    }
                }
            ]
        }
    }

#     res2  = {
#     "payload":{
#         "InboundShipmentPlans":[
#             {
#                 "ShipmentId":"FBA1749NBRPL",
#                 "DestinationFulfillmentCenterId":"MDW2",
#                 "ShipToAddress":{
#                     "Name":"MDW2",
#                     "AddressLine1":"250EMERALDDR",
#                     "City":"Joliet",
#                     "StateOrProvinceCode":"IL",
#                     "CountryCode":"US",
#                     "PostalCode":"60433-3280"
#                 },
#                 "LabelPrepType":"SELLER_LABEL",
#                 "Items":[
#                     {
#                         "SellerSKU":"Xzesoilen9082",
#                         "FulfillmentNetworkSKU":"X001MXFA5F",
#                         "Quantity":10
#                     }
#                 ],
#                 "EstimatedBoxContentsFee":{
#                     "TotalUnits":6,
#                     "FeePerUnit":{
#                         "CurrencyCode":"USD",
#                         "Value":0.15
#                     },
#                     "TotalFee":{
#                         "CurrencyCode":"USD",
#                         "Value":0.9
#                     }
#                 }
#             }
#         ]
#     }
# }

    return json.dumps(res, ensure_ascii=False)



@server.route('/fba/inbound/v0/shipments/<string:id>', methods=['post'])
def index2(id):
    res={"payload":{"ShipmentId":id}}
    return json.dumps(res, ensure_ascii=False)

if __name__ == "__main__":
    server.run(port=8017, debug=True, host='172.16.6.203')
    # http://172.16.6.203:8017/fba/inbound/v0/plans
