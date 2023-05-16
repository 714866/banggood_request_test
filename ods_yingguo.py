import  requests

data_w={
      "address":"Kanamwar ward new colony road\nNorsholm\nNorsholm\n61792",
      "createTime": "2019-11-15 09:44:38",
      "hasMaster": "false",
      "hasMorePack": "false",
      "hasSizeLimit": "null",
      "height": 0,
      "length": 27,
      "noCountLimitPostId": "null",
      "optionsPostVersionId": "null",
      "orderId": "A0000919030503T1",
      "postTypeId":167,
      "posttypeOptions": 167,
      "processcenterid": "7",
      "remoteAddr": "172.31.100.180",
      "replaceFlag": r"true",
      "shape": "SQUARE",
      "shopID": 0,
      "shortName":"TR",
      "spendTime": 345,
      "type":"Package",
      "volume": 2457,
      "weight": 0.513,
      "width": 0,
      "zipCode": "26040"
    }
print(type(data_w))
header={"Host":"192.168.1.221:8087",
"Connection":"keep-alive",
"Content-Length":"715",
"accept":"application/json;charset=UTF-8",
"Origin":"http://192.168.1.221:8087",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
"Content-Type":"application/json",
"Referer":"http://192.168.1.221:8087/lbs/swagger-ui.html",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9",
}
# a = requests.post(r'http://192.168.1.221:8087/lbs/Charging/baseCost',headers=header,data=data_w)
# print(a)
# print(a.text)


data_b={"key": 2,
"orderId": "A0008019081200NC"
}
data_c=[{
      "height": 0,
      "length": 0,
      "orderIdOrTraceId": "A00042190727019H",
      "packageId": "",
      "volume": 0,
      "weight": 0.3,
      "width": 0.01
}]
import  json
data_c=json.dumps(data_c)
header1={
  "Accept": "*/*"
}
b = requests.post(r'http://172.16.5.73:8698/ods-service/api/ksFreightRecomputation?key=1',headers = header,data=data_c)
print(b)
print(b.text)