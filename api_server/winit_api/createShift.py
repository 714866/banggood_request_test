import flask
import json
from  flask import request
server=flask.Flask(__name__)
#
# 移交邮局("HPO", "移交邮局"),
# 草稿("DR", "草稿"),
# 出库确认中("CFI", "出库确认中"),
# 出库确认("CF", "出库确认"),
# 拣选中("PKI", "拣选中"),
# 卖家确认处理方式("WSC", "卖家确认处理方式"),
# 作废处理中("VOI", "作废处理中"),
# 已作废("VO", "已作废"),
# 拣选完成("PKC", "拣选完成"),
# 打包中("PAI", "打包中"),
# 打包完成("PAC", "打包完成"),
# 费用确认中("FC", "费用确认中"),
# 派送中("DLI", "派送中"),
# 派送完成("DLC", "派送完成"),
# 异常("EX", "异常")


@server.route('/winit',methods=['post'])
def index():
    # print(request.)
    res={
    "code":"0",
    "msg":"操作成功",
    "data":{
        "total":1,
        "currentPageSize":10,
        "currentPageNum":1,
        "list":[
            {  "OrderNo":"OrderNo"
            }
        ]

    }
    }

    return json.dumps(res,ensure_ascii=False), 200, {'Content-Type': 'application/json; charset=utf-8'}


if __name__=="__main__":
    server.run(port=9778, debug=True, host='0.0.0.0')
# 需要代替的接口 http://openapi.sandbox.winit.com.cn/openapi/service
# "http://127.0.0.1:9778/winit"