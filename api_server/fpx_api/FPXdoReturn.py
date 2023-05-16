import flask
import json

server=flask.Flask(__name__)

@server.route('/fpx',methods=['post'])
def index():
    res ={
    "result":"1",
    "msg":"系统处理成功",
    "data":{
        "page_no":"1",
        "page_size":"1",
        "total":"1",
        "data": [{
            "consignment_no": "OC9163122111100484",
            "customer_code": "916312",
            "4px_tracking_no": "600973238324",
            "ref_no": "A00002190228000D",
            "from_warehouse_code": "CZPRGA",
            "status": "C",
            "sub_status": "",
            "consignment_type": "S",
            "logistics_product_code": "F152",
            "return_service": "N",
            "signature_service": "N",
            "shipping_no": "CQ324538530DE",
            "total_weight": 1534.0,
            "billing_weight": 1530.0,
            "shipping_weight": 1530.0,
            "total_volume": 8081.850,
            "billing_amount": 6.48000,
            "currency": "",
            "is_oda": "O",
            "sales_platform": "",
            "seller_id": "",
            "sales_no": "",
            "insure_services": "",
            "insure_value": 0.00000,
            "audit_user": "",
            "audit_time": 1636486903000,
            "create_time": 1636486902000,
            "create_user": "916312",
            "update_time": 1636539513000,
            "update_user": "13414856770",
            "complete_time": 1636539398000,
            "remark": "",
            "country": "SK",
            "state": "Nitranski",
            "city": "Kolarovo",
            "district": "",
            "post_code": "94603",
            "street": "Brnenske namestie",
            "house_number": "87",
            "company": "",
            "last_name": "",
            "first_name": "Volodymyr Chudnenko",
            "phone": "+421 919282593",
            "email": "1@web.de",
            "id_card": "",
            "outboundlist_sku": [{
                "consignment_no": "OC9163122111100484",
                "sku_code": "POA7523644",
                "product_code": "",
                "qty": 1,
                "stock_quality": "G",
                "sku_id": "921012835015",
                "sku_name": "新产品 按图拿货 12线 单电要求内置 布包 110~220",
                "batch_no": ""
            }]
        }]


    }
}
    return json.dumps(res, ensure_ascii=False), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == "__main__":
    server.run(port=9903, debug=True, host='172.16.6.203')
    # 需要代替的接口 "http://uat-us-api.jd.com/routerjson"
    # "http://127.0.0.1:9903/fpx"