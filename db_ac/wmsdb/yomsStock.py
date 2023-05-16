# from mysql_connect import connect_db
from db_ac.modular.mapper import connect_DB

# import pymysql

wms_db = "ods_mysql"
wsp_db = "wsp_mysql"
# sr_type= 2为调拨入库， 5为退件入库
sr_type = 2

inserSql_in_storage_request = """INSERT INTO in_storage_request (id, in_storage_request_no, customer_order_no, owner_id, manager_id,
                                    processcenter_id, target_processcenter_id, global_order_code, package_quantity,
                                    goods_quantity, all_weight, all_volume, pickup_way, pickup_adress, pickup_date,
                                    pickup_time, delivery_channels, shipment_number, sr_type, sr_status,
                                    is_stick_label, ship_type, bol_Number, cabinet_Number, remark,
                                    origin_system_type, origin_type, create_date, create_user_id, create_user_name,
                                    modify_user_id, modify_user_name, modify_date, lock_version, modify_time_stamp,
                                    is_deleted, delete_user_id, delete_user_name, delete_date, lcl_limit_level,
                                    storage_code, is_charged, is_liquid, is_powder_past, delivery_product_code,
                                    amazon_shop, goods_type, sign_user_id, sign_date, related_code, trace_code,
                                    is_customs, audit_status, is_drowback, store_type, is_vacuum_packing,
                                    is_shift_costing, goods_size, owner_name, shipment_id)
VALUES ({0}, '{1}', '{4}', 1418043601762304000, 1418043601762304000, 50018, 50018,
        'G-20210630-0000002O', 1, 1, 0.00000, 0.3750000000, 1, '', '2021-06-30', '12:00~16:00', '', '', {2}, 1, 0, 1, '',
        '', '{3}', 1, 4, '2021-06-30 10:43:14', 704992510400925696, 'zhuzhiliang@banggood.com', 704992510400925696,
        'zhuzhiliang@banggood.com', '2021-06-30 10:43:37', 1, '2021-06-30 10:43:36', 0, 0, '', '1970-01-01 00:00:00', 0,
        '0', 0, 0, 0, '', '', -1, 0, '1970-01-01 00:00:00', '', '', 0, 1, 0, 0, 0, 0, 0, '', '')
        """

inserSql_in_storage_request_box = """
INSERT INTO in_storage_request_box (id, in_storage_request_id, box_code, weight, length, width, height, sort,
                                    create_date, create_user_id, create_user_name, modify_user_id,
                                    modify_user_name, modify_date, is_deleted, lock_version, modify_time_stamp,
                                    status, complete_date, is_full)
VALUES ({0}, {1}, '{2}', 0.00000, 150.00000, 50.00000, 50.00000, 1,
        '2021-06-30 10:43:14', 704992510400925696, 'zhuzhiliang@banggood.com', 704992510400925696,
        'zhuzhiliang@banggood.com', '2021-06-30 10:43:38', 0, 0, '2021-06-30 10:43:36', 0, '1970-01-01 00:00:00', 0);
        """

inserSql_in_storage_request_box_item = """INSERT INTO in_storage_request_box_item (id, isr_box_id, goods_id, produce_info_id, batch_code, generate_date,
                                         effective_date, plan_receipt_quantity, pending_receipt_quantity,
                                         received_receipt_quantity, is_new, sampling_ratio,
                                         is_quality_inspection, inspection_remark, sort, create_date,
                                         create_user_id, create_user_name, modify_date, modify_user_id,
                                         modify_user_name, is_deleted, lock_version, modify_time_stamp,
                                         exception_quantity, is_abnormal, origin_code, external_code)
VALUES ({0}, {1}, {2}, '', '', '1970-01-01', '1970-01-01', 100, 100, 0, 0,
        0, 0, '', 1, '2021-06-30 10:43:15', 704992510400925696, 'zhuzhiliang@banggood.com', '1970-01-01 00:00:00', 0,
        '', 0, 0, '2021-06-30 10:43:14', 0, 0, '', '');"""


def inserInstorageRequestbwms(instorageRequestID, instorageRequestCode, instorageRequestboxID, instorageRequestboxCode,
                              instorageRequestBoxItemID,goodsID,shiftCode,remark='手动添加',box_max=False):
    cursor = connect_DB(wms_db)
    global inserSql_in_storage_request
    global inserSql_in_storage_request_box
    global inserSql_in_storage_request_box_item

    if box_max is False:
        cursor.execute(inserSql_in_storage_request.format(instorageRequestID, instorageRequestCode, sr_type, remark,shiftCode))
    else:
        instorageRequestID=int(instorageRequestID)-1
    cursor.execute(
        inserSql_in_storage_request_box.format(instorageRequestboxID, instorageRequestID, instorageRequestboxCode))
    cursor.execute(inserSql_in_storage_request_box_item.format(instorageRequestBoxItemID, instorageRequestboxID,goodsID))

    cursor.commitAndClose()



def inserInstorageRequestbwsp(instorageRequestID, instorageRequestCode, instorageRequestboxID, instorageRequestboxCode,
                              instorageRequestBoxItemID,goodsID,shiftCode,remark='手动添加',box_max=False):
    cursor1 = connect_DB(wsp_db)
    global inserSql_in_storage_request
    global inserSql_in_storage_request_box
    global inserSql_in_storage_request_box_item
    # print(inserSql_in_storage_request.format(instorageRequestID, instorageRequestCode))
    # print(inserSql_in_storage_request_box.format(instorageRequestboxID, instorageRequestID,instorageRequestboxCode))
    # print(inserSql_in_storage_request_box_item.format(instorageRequestBoxItemID, instorageRequestboxID,goodsID))
    # 多分箱不添加主表了
    if box_max is False:
        cursor1.execute(inserSql_in_storage_request.format(instorageRequestID, instorageRequestCode, sr_type, remark,shiftCode))
    else:
        instorageRequestID=int(instorageRequestID)-1
    cursor1.execute(
        inserSql_in_storage_request_box.format(instorageRequestboxID, instorageRequestID, instorageRequestboxCode))
    cursor1.execute(inserSql_in_storage_request_box_item.format(instorageRequestBoxItemID, instorageRequestboxID,goodsID))

    cursor1.commitAndClose()


if __name__ == "__main__":
    # sr_type= 1为采购入库 2为调拨入库， 5为退件入库   ,9为盘点入库  10错货入库
    # global sr_type
    sr_type = 2

    #为True为多明细
    box_max=False
    # 设置处理中心
    # SFT - A1 - 20210407 - 5006A
    code="00102"
    shiftCode="SFT-B1-20830-003"+code
    # shiftCode="PPL-20830-003"+code
    instorageRequestID = "859745893883"+code
    instorageRequestCode = "IHP202106301"+code
    instorageRequestboxID = "8597458942178"+code
    instorageRequestboxCode = "Fbox-20210632-"+code
    instorageRequestBoxItemID = "8597458945533"+code
    # goodsID = 879781423619067904   # PBU00030DF5
    # goodsID = 896069986021425152   # PBU0378561
    # goodsID = 896070790795116544   # PBU0378563
    # goodsID = 896071316681146368   # PBU0378565
    goodsID = 896071772820094976   # PBU0378567


    remark = '测试：货损重新上架'
    # 设置销售类型

    # 插入wms
    inserInstorageRequestbwms(instorageRequestID, instorageRequestCode, instorageRequestboxID, instorageRequestboxCode,
                              instorageRequestBoxItemID,goodsID,shiftCode,remark,box_max)

    # 插入wsp
    # inserInstorageRequestbwsp(instorageRequestID, instorageRequestCode, instorageRequestboxID, instorageRequestboxCode,
    #                           instorageRequestBoxItemID,goodsID,shiftCode,remark,box_max)

    print(instorageRequestCode)
    print(instorageRequestboxCode)
    print(shiftCode)

