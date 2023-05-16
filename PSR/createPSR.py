import requestsimport PSR.FBCshiftTypeData as shiftTypeDataglobal oa_urloa_url='http://apiewms-dev.banggood.cn'# oa_url='http://172.16.6.203:8092/'# oa_url='http://172.16.6.32:8092/'class MultipartFormData(object):    """multipart/form-data格式转化"""    @staticmethod    def format(data, boundary="----WebKitFormBoundarywNtULNA8KNlc46BV", headers={}):        """        form data        :param: data:  {"req":{"cno":"18990876","flag":"Y"}}        :param: boundary: "----WebKitFormBoundary7MA4YWxkTrZu0gW"        :param: headers: 包含boundary的头信息；如果boundary与headers同时存在以headers为准        :return: str        :rtype: str        """        # 从headers中提取boundary信息        if "content-type" in headers:            fd_val = str(headers["content-type"])            if "boundary" in fd_val:                fd_val = fd_val.split(";")[1].strip()                boundary = fd_val.split("=")[1].strip()            else:                raise Exception("multipart/form-data头信息错误，请检查content-type key是否包含boundary")        # form-data格式定式        jion_str = '--{}\r\nContent-Disposition: form-data; name="{}"\r\n\r\n{}\r\n'        end_str = "--{}--".format(boundary)        args_str = ""        if not isinstance(data, dict):            raise Exception("multipart/form-data参数错误，data参数应为dict类型")        for key, value in data.items():            args_str = args_str + jion_str.format(boundary, key, value)        args_str = args_str + end_str.format(boundary)        args_str = args_str.replace("\'", "\"")        return args_strheaders = {    "Host": "172.16.6.203:8092",    "Proxy-Connection": "keep-alive",    "Content-Length": "764",    "Accept": "application/json, text/plain, */*",    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",    "Origin": oa_url,    "Referer": oa_url,    "Accept-Encoding": "gzip, deflate",    "Accept-Language": "zh-CN,zh;q=0.9",    "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarywNtULNA8KNlc46BV",    "Cookie": 'Authorization="Bearer AT-6483-gDgmF2wjLf97pfl6Xasqop6MZ3xcpxSx"'}# shiftType=0 普通调拨data = {    "productShiftRequestCreateVOS": [{"shiftType": "0", "priorityLevel": "0", "shipType": "3", "processCenterId": "934",                                    "sourceProcessCenterId": "1040", "remark": "POA4235465",                                    "sourceProcessCenterName": "香港处理中心", "processCenterName": "东莞处理中心",                                    "salePlatform": "", "currentPostMoney": "", "linkUrl": "", "orderNum": "",                                    "salePrice": "", "grossMoney": "", "currentPostMoneyCurrency": "",                                    "salePriceCurrency": "", "quantity": "10", "productId": 1589175,                                    "propertyId": 4245101, "storageQuantity": 3482, "originStorageId": 370,                                    "originStorageName": "香港发货仓库", "productCode": "SKUB16136", "productName": "xxx",                                    "propertyCode": "POA4235465", "transferPrice": 18}]}# shiftType=4 FBA调拨FBA_data = {    "productShiftRequestCreateVOS": [{"shiftType": "4", "priorityLevel": "0", "shipType": "3", "processCenterId": "903",                                    "sourceProcessCenterId": "1040", "remark": "POA4235465",                                    "sourceProcessCenterName": "香港处理中心", "processCenterName": "法国FBA处理中心",                                    "salePlatform": "", "currentPostMoney": "", "linkUrl": "", "orderNum": "",                                    "salePrice": "", "grossMoney": "", "currentPostMoneyCurrency": "",                                    "salePriceCurrency": "", "quantity": "10", "productId": 1589175,                                    "propertyId": 4245101, "storageQuantity": 3482, "originStorageId": 370,                                    "originStorageName": "香港发货仓库", "productCode": "SKUB16136", "productName": "xxx",                                    "propertyCode": "POA4235465", "transferPrice": 18}]}FBC_data=shiftTypeData.return_api_FBC_data(is_poa=False)mh = MultipartFormData.format(data=FBC_data, headers=headers)print(mh)if __name__=="__main__":    isThird=True    res = requests.request("POST", data=mh.encode('utf-8'), headers=headers,                           url=oa_url + '/warehouse/product/shift/request/createProductShiftRequestEwmsOnly?userId=33970&hostUrl=ewms-dev.banggood.cn')    print(res)    print(oa_url + '/warehouse/product/shift/request/createProductShiftRequestEwmsOnly?userId=33970&hostUrl=ewms-dev.banggood.cn')    # for i in range(5):    #     if isThird:    #         res=requests.request("POST",data=mh.encode('utf-8'),headers=headers,url=oa_url+'/warehouse/product/shift/request/createProductShiftRequestEwmsOnly?userId=33970&hostUrl=172.16.6.203:4600')    #     else:    #         res=requests.request("POST",data=mh.encode('utf-8'),headers=headers,url=oa_url+'warehouse/product/shift/request/createProductShiftRequest?userId=15182&hostUrl=172.16.6.203:4600')    #     print(oa_url+'warehouse/product/shift/requ')    #     print(res.text)