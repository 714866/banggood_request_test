import  requests


class LoginRequst(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        # 类对象唯一
        if cls.__instance is None:
            cls.__instance = super(LoginRequst, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.session = requests.session()
        self.header = {"Content-Type":"application/json;charset=UTF-8"}
        login_url = 'http://172.16.7.4:18201/own-wms-api/pda/sys-user/login'
        d = {
            "language": 0,
            "password": "123456",
            "username": "zhuzhiliang@banggood.com"
        }
        login_result = self.session.post(url=login_url, json=d, headers=self.header)

    def _lognin(self):
        pass
    def post(self,url,data,header=None):
        if header is None:
            header = self.header

        result = self.session.post(url=url,json=data,headers=header)
        if result.status_code == 401:
            login_url = 'http://172.16.7.4:18201/own-wms-api/pda/sys-user/login'
            d = {
                "language": 0,
                "password": "123456",
                "username": "zhuzhiliang@banggood.com"
            }
            result = self.session.post(url=url, json=data, headers=header)
        return result








if __name__ =='__main__':
    request = LoginRequst()

    # login_url = 'http://172.16.7.4:18201/own-wms-api/pda/sys-user/login'
    # d = {
    #   "language": 0,
    #   "password": "123456",
    #   "username": "zhuzhiliang@banggood.com"
    # }
    # login_result =request.post(login_url,d)

    instorange_url = 'http://172.16.7.4:18201/own-wms-api/pda/inStorage/saveInStorage'
    i =  {"receiptNo":"RC2022112300003A"}

    instorage_result = request.post(instorange_url,i)
    print(instorage_result)

