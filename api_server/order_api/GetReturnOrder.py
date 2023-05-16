import flask
import json

from flask import request

server=flask.Flask(__name__)


@server.route('/OrderService/orderservice.svc/GetReturnOrder',methods=['get'])
def index():
    # res={'msg':'cccccc','msg_code':0}
    order_id = request.values.get('orderId')
    res={
  "AffectRow": 1,
  "Message":
      [
          {
              "OrderId": order_id,
              "TraceId": "JD0002258959561607",
              "ProcessCenterID": "1040",
              "PostTypeId": "726",
              "PostType": "Whistl Packet 挂号",
              "ProcessCenterName": "英国诺丁汉2号处理中心",
              "SalesUserId": "40251",
              "SalesUserName": "陈杰聪",
              "OrderDetail": [
                  {
                      "OrderDetailID": 0,
                      "ProductCode": "SKU002295",
            "PropertyCode": "POA000023",
                      "ItemName": "xxx",
                      "Num": "4",
                      "SalePrice": None,
                      "ColorSel": None,

                      "ProcessceStatus": 0
                  }
                  # ,                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKUB69715",
                  #     "PropertyCode": "POA4527805",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKUB18617",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKU933505",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKUA82822",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKU746639",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKU404718",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKU588515",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKU949529",
                  #     "ItemName": "xxx",
                  #     "Num": "3",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKU554234",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKUB47013",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKUB06934",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKU763011",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKUB69715",
                  #     "PropertyCode": "POA4527805",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKUB18617",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKU933505",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKUA82822",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKU746639",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKU404718",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKU588515",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKU949529",
                  #     "ItemName": "xxx",
                  #     "Num": "3",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKU554234",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKUB47013",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # },                  {
                  #     "OrderDetailID": 0,
                  #     "ProductCode": "SKUB06934",
                  #     "ItemName": "xxx",
                  #     "Num": "1",
                  #     "SalePrice": None,
                  #     "ColorSel": None,
                  #     "PropertyCode": "",
                  #     "ProcessceStatus": 0
                  # }

              ],
              "ReturnStepId": "A0000219102502MD1",
              "ReturnType": "Return",
              "KeyId": "ZR241577399GB",
              "OrderType": "normal",
              "PlatformName": "eBay",
              "ReturnStyle": ""
          }
      ]
  ,
  "IsSuccess": True,
}
    return json.dumps(res,ensure_ascii=False)


if __name__=="__main__":
    server.run(port=8017, debug=True, host='172.16.7.4')
    # http://172.16.7.4:8017/OrderService/orderservice.svc/GetReturnOrder?orderId=A000332209050006