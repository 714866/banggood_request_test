import time

from db_ac.modular.mapper import connect_DB

pckInf = """INSERT INTO twms.ods_pck_info (id, package_id, order_id, batchgridorderdata_id, process_center_id, delivery_type,
                               order_type, detail_type, package_type, batch_processing_id, pck_state, change_state_time,
                               in_ods_date_time, in_wsp_datetime, in_system_datetime, freight, total_price,
                               actual_weight, goods_pck_weight, volume_weight, package_length, package_width,
                               package_height, post_id, post_type_options, online_psot_type, trace_id, way_bill_no,
                               delivery_date, delivery_user_id, delivery_user, receive_name, phone, country_id, country,
                               county, city, buyer_address1, buyer_address2, zip, belonging, belonging_id, pck_remarks,
                               platform_order_id, master_post_no_jump, is_part_delivery, is_gift_lack_delivery,
                               processing_scheme, processing_scheme_remark, return_reason_name, return_reason_remark,
                               create_date, create_user_id, create_user_name, modify_date, modify_user_id,
                               modify_user_name, is_deleted, delete_date, delete_user_id, delete_user_name,
                               modify_time_stamp, lock_version, ods_site_server, init_pck_volume, address, email,
                               in_ods_date_new, real_post_id, payment_type, user_trace_id, cabinet_number,
                               earliest_delivery_date, is_list_scan, deliver_goods_id, order_info_json)
VALUES ({0}, '{1}', '{2}', '', {3}, ',1,2,3,', 'normal', 3, 3, null, 1,
        '2022-01-13 16:56:44', '2020-07-24 15:25:58', '2020-07-24 15:25:56', '2020-07-21 11:01:22', 23.648, 17.727,
        1.357, 0.571, 0.000, 27.00, 7.50, 7.50, '1756', '873|0,870|0,872|0,871|1', 'AU_StandardDelivery', null, '',
        '2022-01-13 16:56:44', null, null, 'Andrea Formston', '0422634606', '13', 'AU', 'Victoria', 'Croydon North',
        '4 Hurst Court', '', '3136', '516925542164078592', 0,
        'TWMS交寄发货主流程错误信息: 订单在第三方异常或作废：，尝试取消第三方出库单，取消第三方出库单成功，<a href="http://twms-test.banggood.cn/#/pages/content/contactRecord/orderRecord?id=A000022007210352" target="_blank">查看三方仓交互信息</a>',
        '24-05439-22494', 0, null, null, '', '', '', '', '2020-07-24 15:25:56', 1, '初始化服务', null, 0, '', false,
        '2021-12-17 16:58:03', 1, 'admin', '{4}', 19, '', 1518.750, '4 Hurst Court
Croydon North
Victoria
3136', 'ange.formston@gmail.com', '2020-07-24 15:25:58', '', 1, '', '', '1970-01-01 00:00:00', 0, '',
        '');"""

pckDetail = """
    INSERT INTO twms.ods_pck_detail (id, package_id, item_id, item_name, base_product_name, base_packing_specification,
                                 sale_price, quantity, bar_code_id, sku, poa, bar_code, length, width, height,
                                 goods_spec, goods_attachment_id, item_delivery_weight, goods_manager_name,
                                 sales_user_name, platform_order_id, os_detail_id, transaction_id, create_date,
                                 create_user_id, create_user_name, modify_date, modify_user_id, modify_user_name,
                                 is_deleted, delete_date, delete_user_id, delete_user_name, modify_time_stamp,
                                 lock_version, row, rack, position, is_default, stock_quantity, order_detail_id,
                                 goods_id, bg_product_id, bg_property_id, adapter_num, is_get_rack, area, goods_label,
                                 order_detail_info_json)
VALUES ({0}, '{1}', '0',
        '❤ Drink Crystal Water Glass Bottle Natural Quartz Energy Point With Obelisk Wand',
        '❤ Drink Crystal Water Glass Bottle Natural Quartz Energy Point With Obelisk Wand', 3, 17.7265, 1, null,
        'SKUB35364', 'POA4329058', '', 27.00, 7.50, 7.50, '', 0, 0.000, '', '', '', '', null, '2020-07-24 15:25:56', 1,
        '初始化服务', null, 0, '', false, null, 0, '', '1970-01-02 00:00:00', 0, '', '', '', 0, 0, 549518946, 1964265,
        1964265, 6347253, 0, 1, '', '', '');
    """

pckAttached = """INSERT INTO twms.ods_pck_attached (id, package_id, order_id, is_repeat_send, is_replenishment, is_split, setting,
                                   original_currency, original_amount, original_ship_fee, original_total_fee,
                                   platform_id, platform_name, store_id, store_name, logistics_account,
                                   order_track_type, region, area, weight_level, is_multi_storage_delivery,
                                   pack_require_id, deficit_price, lights_goods_freight, loss_condition,
                                   jettison_condition, is_cost_control, max_feight, package_service_fee,
                                   package_material_fee, create_date, create_user_id, create_user_name, modify_date,
                                   modify_user_id, modify_user_name, is_deleted, delete_date, delete_user_id,
                                   delete_user_name, modify_time_stamp, lock_version, sales_user_id, sales_user_name,
                                   product_manager_name, product_manager_id, lable_types, requirement_types,
                                   jump_abroad_warehouse_status, is_fulfilled, stock_store_id, mobile_ids)
VALUES ({0}, '{1}', '{2}', false, null, false, '', 'AUD', null, null, null,
        '{3}', '', '3718', 'topestore48', '00002', 0, '4121132734789989177', '7220789956340638003', '0', false, null,
        0.000, 0.000, '', '', 0, 0.000, null, 0.000, '2020-07-24 15:25:56', 1, '初始化服务', null, 0, '', false, null, 0, '',
        '1970-01-02 00:00:00', 0, 0, '', '', 0, '', '', 0, 0, '1521', '');
"""

twms_db='twms_mysql'

def choose_goods(process):
    pass

def inser_pck(pck,order,process):

    cursor = connect_DB(twms_db)

    pckInfoId=str(time.time()).replace('.','')
    print(pckInf.format(pckInfoId, pck, order,process,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    cursor.execute(pckInf.format(pckInfoId, pck, order,process,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
    pckDetailId=str(time.time()).replace('.','')
    cursor.execute(pckDetail.format(pckDetailId, pck))

    platform_id='111'
    # 是否需要文件
    is_files= False
    if process==1211 and is_files is False:
        platform_id='766'
    pckAttachedId=str(time.time()).replace('.','',)
    cursor.execute(pckAttached.format(pckAttachedId, pck,order,platform_id))
    # ommOrderProcessId=str(time.time()).replace('.','')
    # cursor.execute(ommOrderProcess.format(ommOrderProcessId, pck,order))
    cursor.commitAndClose()


if __name__ == "__main__":

    pck='PCK1130200724G267'
    order='A000022007210367'
    # GC
    process=1205

    inser_pck(pck,order,process)






