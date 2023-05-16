import flask
import json
server=flask.Flask(__name__)


@server.route('/openApi/query_product',methods=['post'])
def index():
    # res={'msg':'cccccc','msg_code':0}
    res={ "result":
        {
            "products": [
                {
                    "foreignTitle": "foreignTitle1",
                    "id": 0,
                    "longDescription": "string",
                    "managerId": 0,
                    "managerName": "string",
                    "parentSellerSku": "string",
                    "productCode": "string",
                    "platformSiteCode":"6938718318657",
                    "productId": 0,
                    "sellerId": 0,
                    "sellerUser": "string",
                    "shopId": 0,
                    "shortDescription": "string",
                    "url": "stringurl",
                    "properties": [
                        {
                            "id": 0,
                            "listingId": 0,
                            "marketPrice": 0,
                            "onlineStock": 100,
                            "platformStock": 110,
                            "propertyCode": "string",
                            "propertyId": 0,
                            "salePrice": 15,
                            "sellerSku": "234ccd",
                            "barcode":"SKU489560",
                            "platformProductName": "string",
                            "platformProductCode":"6938718318657"
                        }
                    ]
                },
                {
                    "foreignTitle": "foreignTitle1",
                    "id": 0,
                    "longDescription": "string",
                    "managerId": 0,
                    "managerName": "string",
                    "parentSellerSku": "string",
                    "productCode": "string",
                    "platformSiteCode": "7793120427910",
                    "productId": 0,
                    "sellerId": 0,
                    "sellerUser": "string",
                    "shopId": 0,
                    "shortDescription": "string",
                    "url": "stringurl",
                    "properties": [
                        {
                            "id": 0,
                            "listingId": 0,
                            "marketPrice": 0,
                            "onlineStock": 89,
                            "platformStock":101,
                            "propertyCode": "string",
                            "propertyId": 0,
                            "salePrice": 15,
                            "sellerSku": "234ccd",
                            "barcode": "SKU901415",
                            "platformProductName": "string",
                            "platformProductCode": "7793120427910"
                        }
                    ]
                }
            ],
            "totalSize": 1
        },
        "success": "true"
        }

    return json.dumps(res,ensure_ascii=False)


if __name__=="__main__":
    server.run(port=7777, debug=True, host='0.0.0.0')

    # "http://api.dev.sellercube.com/sp_api/listing"
    # "http://127.0.0.1:7777"