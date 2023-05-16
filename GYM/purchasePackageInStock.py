import flask
import json
server=flask.Flask(__name__)



@server.route('/purchasePackageList',methods=['post'])
def index():
    res={
        "code":200,
        "msg":"成功",
        "data":{
            "pageNum":1,
            "pageSize":50,
            "size":1,
            "startRow":1,
            "endRow":1,
            "total":1,
            "pages":1,
            "list":[
                {
                    "packageID":25902173,
                    # "packageCode":"PPL-20210702-902173",
                    "packageCode":"PPL-20220216-609062",
                    "purchaseItemID":"35292921",
                    "purchaseCode":"PON-6-20210702-686050",
                    "productID":2402506,
                    "propertyID":8725736,
                    "productCode":"POA8701175",
                    "purchaseCenterID":1150,
                    "processCenterID":1208,
                    "supplierID":315390,
                    "arrivalPrice":18,
                    "quantity":15,
                    "prePrice":18,
                    "preQuantity":1,
                    "printState":0,
                    "status":7,
                    "trackingNo":None,
                    "isDrawback":0,
                    "remark":"【OA-审单(手动审单以及自动审单-FBH代发自动生成PPL)】：    ",
                    "createUserID":9758,
                    "createTime":"2021-07-02 16:39:19",
                    "lastUpdateUserID":50561,
                    "lastUpdateTime":"2021-07-12 19:00:18",
                    "purchaseUser":51442,
                    "speed":1,
                    "inStorePrice":18,
                    "consignTime":"2021-07-09",
                    "logisticsCompany":None,
                    "waybillNumber":"不需要物流",
                    "addUser":50544,
                    "sku":"SKUH91711",
                    "poa":"POA8701175",
                    "zmgz":None
                },{
                    "packageID":186609061,
                    "packageCode":"PPL-20220215-609061",
                    "purchaseItemID":"296615106",
                    "purchaseCode":"PON-6-20210702-686050",
                    "productID":2402506,
                    "propertyID":8725736,
                    "productCode":"POA8701175",
                    "purchaseCenterID":1150,
                    "processCenterID":1208,
                    "supplierID":315390,
                    "arrivalPrice":18,
                    "quantity":15,
                    "prePrice":18,
                    "preQuantity":1,
                    "printState":0,
                    "status":7,
                    "trackingNo":None,
                    "isDrawback":0,
                    "remark":"【OA-审单(手动审单以及自动审单-FBH代发自动生成PPL)】：    ",
                    "createUserID":9758,
                    "createTime":"2021-07-02 16:39:19",
                    "lastUpdateUserID":50561,
                    "lastUpdateTime":"2021-07-12 19:00:18",
                    "purchaseUser":51442,
                    "speed":1,
                    "inStorePrice":18,
                    "consignTime":"2021-07-09",
                    "logisticsCompany":None,
                    "waybillNumber":"不需要物流",
                    "addUser":50544,
                    "sku":"SKUH91711",
                    "poa":"POA8701175",
                    "zmgz":None
                }
            ],
            "prePage":0,
            "nextPage":0,
            "isFirstPage":True,
            "isLastPage":True,
            "hasPreviousPage":False,
            "hasNextPage":False,
            "navigatePages":8,
            "navigatepageNums":[
                1
            ],
            "navigateFirstPage":1,
            "navigateLastPage":1,
            "firstPage":1,
            "lastPage":1
        }
    }


    return json.dumps(res, ensure_ascii=False), {'Content-Type': 'application/json; charset=utf-8'}
    # return json.dumps(res,ensure_ascii=False)


if __name__ == "__main__":
    server.run(port=9113, debug=True, host='0.0.0.0')
    # http://127.0.0.1:9113/