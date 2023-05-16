import time

from db_ac.modular.mapper import connect_DB


wms_db = "ods_mysql"
wsp_db = "wsp_mysql"


lossBillRequestSql="""INSERT INTO wsp.lost_bill_request (id, lost_bill_request_code, lost_bill_merge_code, old_mid, lost_mid, lost_id,
                                   from_processcenter_id, to_processcenter_id, from_storage_id, to_storage_id,
                                   product_id, product_stock_status, property_id, quantity, real_price, remark,
                                   lost_bill_request_status, lost_bill_type, origin_code, guid, origin_client,
                                   audit_state, audit_time, audit_user_name, audit_remark, next_audit_user_name,
                                   flow_apply_info, is_flow_checked, lost_type, duty_id, duty_name, duty_type,
                                   second_level_dept_id, lost_reason, category_id, category_name, file_url,
                                   total_cost_price, sys_ctime, create_user_id, create_user_name, modify_date,
                                   modify_user_id, modify_user_name, is_deleted, delete_date, delete_user_id,
                                   delete_user_name, sys_utime, lock_version)
VALUES ({0}, '{1}', '', 0, 0, 0, 1111, 1111, 0, 0, 1614872, '', 4399598, 3, 50021.16,
        '未知-货不对板-退件报损', 0, 0, '{2}', 'f997994d-88ab-46a1-ad33-3d8fab5d6b79', 'OA', 0,
        '1970-01-01 00:00:00', '', '', '', '', 0, {3}, '', '', {4}, '1a58297bcf64507f9b111473156e9594', 7, 400000611,
        '普通连衣裙',
        'http://gzfastdfs.banggood.cn/fast/download?fileUrl=2022-01-25/4e13712e-c4b1-4ac3-864d-37fbc222fc09.xlsx',
        0.00000, '2022-01-25 10:42:56', 33970, '欧阳杰铭', '1970-01-01 00:00:00', 0, '', 0, '1970-01-01 00:00:00', 0, '',
        '2022-01-25 11:41:26', 0);
"""
str(time.time()).replace('.', '')

class lossBillRequest():

    def __init__(self):
        self.cursor = connect_DB(wsp_db)

    def lossBillRequestInsert(self,id,lostBillRequestCode,orderCode,lostType,dutyType):
        self.cursor.execute(lossBillRequestSql.format(id, lostBillRequestCode, orderCode, lostType, dutyType))

    def commit(self):
        self.cursor.commit()




if __name__ == '__main__':

    lostBillRequestCode='LBR-A2-202201253-'
    orderCode='A0000419081400RY-'
    # '报损类型（对应枚举有0-调拨途损、1-退件途损、2-在库报损,3-发货途损）';
    lostType=0
    # 责任方类别(0 - 未知, 1 - 部门, 2 - 渠道商, 3 - 公司)
    dutyType=0
    # nowDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    nowDate = str(time.time()).replace('.', '')
    loss = lossBillRequest()
    for i in range(0, 100):
        # 订单枚举值  '0销售出库,1样品出库,2调拨出库,3清货出库,4盘损出库,5返修出库,6退件出库,7报损出库,8移库出库,9重构出库,10退货出库
        id=nowDate+str(i)
        code1 = lostBillRequestCode+str(i).zfill(5)
        code2 = orderCode+str(i).zfill(4)
        loss.lossBillRequestInsert(id,code1,code2,lostType,dutyType)
        print(id)

    loss.commit()



