import time

from db_ac.modular.mapper import connect_DB


wms_db = "ods_mysql"
wsp_db = "wsp_mysql"


pckInfo="""INSERT INTO ews.package_info (id, package_id, order_id, overall_code, pck_type, outbound_type, outbound_date, status,
                              handle_programme, process_prescription, manager_id, owner_id, priority, surplus_date,
                              remark, exception_type, is_stockout, is_track, is_since, process_center_id, platform_name,
                              platform_id, store_id, store_name, delivery_type, order_type, detail_type, package_type,
                              batch_processing_id, pck_state, change_state_time, in_ods_date_time, in_wsp_datetime,
                              in_system_datetime, freight, total_price, actual_weight, goods_pck_weight, volume_weight,
                              package_length, package_width, package_height, post_id, post_type_options,
                              online_psot_type, trace_id, way_bill_no, delivery_date, delivery_user_id, delivery_user,
                              receive_name, phone, country_id, country, county, city, buyer_address1, buyer_address2,
                              zip, belonging, pck_remarks, platform_order_id, master_post_no_jump, is_part_delivery,
                              is_gift_lack_delivery, processing_scheme, processing_scheme_remark, return_reason_name,
                              return_reason_remark, ods_site_server, create_date, create_user_id, create_user_name,
                              modify_date, modify_user_id, modify_user_name, is_deleted, delete_date, delete_user_id,
                              delete_user_name, modify_time_stamp, lock_version, create_timestamp,
                              target_processcenter_id, ship_type, stock_type, origin_type, container_code, supplier_id,
                              lcl_limit_level, is_charged, is_liquid, is_powder_past, sync_status_ods, is_full,
                              store_type, return_type, is_drowback, exception_reason, goods_type, owner_name,
                              goods_size)
VALUES ({0}, '{1}', '{2}', 'G-20210128-0000003', {5}, {4},
        '{3}', 0, -1, 0, 705014544711557120, 705014544711557120, 0, '{3}', '', -1, 0,
        1, false, 1138, '', '', '', '', '', '', 0, 0, '', 1, '1970-01-01 00:00:00', '1970-01-01 00:00:00',
        '1970-01-01 00:00:00', '{3}', 0.000, 0.000, 0.010, 0.010, 0.010, 10.00, 10.00, 10.00, '', '',
        '', '', '', '1970-01-01 00:00:00', 0, '', 'ZZR', '123456', '13', '澳大利亚', 'ZZR', 'ZZR', 'ZZR', '', 'ZZR', 'open',
        '', '', 0, 0, 0, '', '', '', '', '', '{3}', 704992510400925696, 'zhuzhiliang@banggood.com',
        '{3}', 704992510400925696, 'zhuzhiliang@banggood.com', 0, '1970-01-01 00:00:00', 0, '',
        '{3}', 0, '{3}', 0, 0, 0, 3, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, '树青', 0);"""
# goods_id=705017168479260672
pckItem1="""INSERT INTO ews.package_item (id, package_id, goods_id, goods_name, goods_spec, base_product_code, external_code,
                              produce_id, produce_code, produce_date, valid_date, is_stockout, manager_id, owner_id,
                              processcenter_id, outbound_strategy, sale_price, actual_quantity, quantity, length, width,
                              height, goods_attachment_id, item_delivery_weight, goods_manager_name, sales_user_name,
                              platform_order_id, os_detail_id, transaction_id, create_date, create_user_id,
                              create_user_name, modify_date, modify_user_id, modify_user_name, is_deleted, delete_date,
                              delete_user_id, delete_user_name, modify_time_stamp, lock_version, stockout_quantity,
                              separate_quantity, original_order, loss_quantity, source_order, relation_code)
VALUES ({0}, '{1}', 705017168479260672, '测试个人商品A', '', 'PBU0100750', 'SKUZ202024', '', '',
        '1970-01-01 00:00:00', '1970-01-01 00:00:00', 0, 705014544711557120, 705014544711557120, 1138, 0, 0.0000, 0, '{3}',
        0.00, 0.00, 0.00, 0, 0.00, '', '', '', '', 0, '{2}', 704992510400925696,
        'zhuzhiliang@banggood.com', '1970-01-01 00:00:00', 0, '', 0, '1970-01-01 00:00:00', 0, '',
        '{2}', 0, 0, 0, '', 0, '', '');"""
 # goods_id=705440039588466688
pckItem2="""INSERT INTO ews.package_item (id, package_id, goods_id, goods_name, goods_spec, base_product_code, external_code,
                              produce_id, produce_code, produce_date, valid_date, is_stockout, manager_id, owner_id,
                              processcenter_id, outbound_strategy, sale_price, actual_quantity, quantity, length, width,
                              height, goods_attachment_id, item_delivery_weight, goods_manager_name, sales_user_name,
                              platform_order_id, os_detail_id, transaction_id, create_date, create_user_id,
                              create_user_name, modify_date, modify_user_id, modify_user_name, is_deleted, delete_date,
                              delete_user_id, delete_user_name, modify_time_stamp, lock_version, stockout_quantity,
                              separate_quantity, original_order, loss_quantity, source_order, relation_code)
VALUES ({0}, '{1}', 705440039588466688, 'xxx', '', 'PBU0100754', 'SKU20200430', '', '',
        '1970-01-01 00:00:00', '1970-01-01 00:00:00', 0, 705014544711557120, 705014544711557120, 1138, 0, 0.0000, 0, '{3}',
        0.00, 0.00, 0.00, 0, 0.00, '', '', '', '', 0, '2021-01-28 16:04:22', 704992510400925696,
        'zhuzhiliang@banggood.com', '1970-01-01 00:00:00', 0, '', 0, '1970-01-01 00:00:00', 0, '',
        '{2}', 0, 0, 0, '', 0, '', '');
"""

ommOrderProcess="""INSERT INTO ews.omm_order_process (id, package_id, order_id, main_post_id, post_id, is_delivery, is_preset, retry_num,
                                   trace_id, link, invoice_url, special_lable_url, waybill_no, freight, weight,
                                   package_type, is_loss, loss_interception_amount, no_loss_interception_amount,
                                   loss_interception_type, loss_factor, loss_value, bargain_interception_type,
                                   has_size_limit, replace_flag, shape, has_master, no_count_limit_post_id, error_msg,
                                   create_date, create_user_id, create_user_name, modify_date, modify_user_id,
                                   modify_user_name, is_deleted, delete_date, delete_user_id, delete_user_name,
                                   modify_time_stamp, lock_version, real_post_id)
VALUES ({0}, '{1}', '{2}', '', '', false, false, 5, '',
        'https://hkfile.e-withouse.com/file/download?fileUrl=/20210128/5a97155c23e147209fb84e1d63b160c5.pdf', '', '',
        null, null, null, '', false, 0.00000, 0.00000, null, null, null, null, true, true, 0, true, null, '',
        '2021-01-28 16:04:22', 0, '', null, 0, '', false, null, 0, '', '{3}', 0, '');"""



odsDeliveryResult="""INSERT INTO ews.ods_delivery_result (id, package_id, order_id, oper_type, execute_state, state, belonging_id,
                                     batch_processing_id, trace_id, actual_weight, package_length, package_width,
                                     package_height, volume_weight, size_source, calculate_throw_coefficient,
                                     original_post_id, selection_post_id, selection_post_name, original_post_name,
                                     jj_date, jj_user_id, freight, currency, package_type, processCenter_id, run_time,
                                     run_error_msg, run_count, sync_state, create_date, create_user_id,
                                     create_user_name, modify_date, modify_user_id, modify_user_name, is_deleted,
                                     delete_date, delete_user_id, delete_user_name, modify_time_stamp, lock_version,
                                     whether_artificial, delivery_user_id, mac_address, seat_no, return_oa_state,
                                     return_stock_state, return_relieve_tms_state)
VALUES ({0}, '{1}', '{2}', 1, 5, 4, 0, 'TX20210313000036H',
        '9261290983208235637966', 1.056, 88.00, 8.00, 8.00, 0.256, 0, 7000.000, '1271', '1271', 'YH-自营美东经济专线st（电）',
        'YH-自营美东经济专线st（电）', '2021-03-15 15:01:04', 46503, 123.079, 'CNY', 3, 1138, '2021-07-19 16:32:49', '', 0, false,
        '2021-03-15 16:01:04', 46503, '唐典红', '2021-07-19 16:32:49', 46503, '甲队兼职1', false, null, 0, '',
        '2021-08-24 14:32:22', 2, 1, 732634196052549632, 'E0-D5-5E-00-F4-E4', '', 1, 1, 1);"""


def pckInsertWms(pck, orderid,outboutType,pckType):

    cursor = connect_DB(wms_db)
    global pckInfo
    global pckItem1
    global pckItem2
    global ommOrderProcess
    global odsDeliveryResult

    nowDate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    str(time.time()).replace('.', '')

    cursor.execute(pckInfo.format(str(time.time()).replace('.', ''), pck, orderid, nowDate, outboutType, pckType))
    cursor.execute(ommOrderProcess.format(str(time.time()).replace('.', ''), pck,  orderid,nowDate))
    quantity=1
    if pckType==1:
        quantity=3
    cursor.execute(pckItem1.format(str(time.time()).replace('.', ''), pck,  nowDate,quantity))
    if pckType==2:
        time.sleep(1)
        quantity=2
        cursor.execute(pckItem2.format(str(time.time()).replace('.', ''), pck,  nowDate,quantity))
      # 下面注释的是ods发货后才写的数据  模拟已交寄场景的才需要
    cursor.execute(odsDeliveryResult.format(str(time.time()).replace('.', ''), pck,  orderid))

    cursor.commitAndClose()
    # print(12)


if __name__=='__main__':

    oringe_pck='11382021119000'
    oringe_orderid='20211180000161'

    for i in range(200,300):

    # 订单枚举值  '0销售出库,1样品出库,2调拨出库,3清货出库,4盘损出库,5返修出库,6退件出库,7报损出库,8移库出库,9重构出库,10退货出库
        print("PCK"+str(int(oringe_pck)+i))
        pck="PCK"+str(int(oringe_pck)+i)
        orderid="CDK"+str(int(oringe_orderid)+i)
        outboutType=0
        # 订单类型  0：单条  1：单条多 2：多条
        pckType=0
        pckInsertWms(pck,orderid,outboutType,pckType)

# 705017168479260672