import flask
import json
server=flask.Flask(__name__)


@server.route('/ewms-api-server/api/ewms-goods/labelPrint',methods=['post'])
def index():
    # res={'msg':'cccccc','msg_code':0}
    res={ "result":
        {
                    "foreignTitle": "foreignTitle1",
                    "id": 0,
                    "longDescription": "string",
                    "managerId": 0,
                    "managerName": "string",
                    "parentSellerSku": "string",
                    "productCode": "string",
                    "productId": 0,
                    "sellerId": 0,
                    "sellerUser": "string",
                    "shopId": 0,
                    "shortDescription": "string",
                    "url": "stringurl",

        }
        }

    return json.dumps(res,ensure_ascii=False)


if __name__=="__main__":
    server.run(port=8812, debug=True, host='0.0.0.0')