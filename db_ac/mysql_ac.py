from mysql_connect import connect_db

import pymysql


def usdb_inser():
    info_sql = "    INSERT\
    INTO\
    `ews`.\
    `ods_pck_info`(`id`, `package_id`, `order_id`, `batchgridorderdata_id`, `process_center_id`, `delivery_type`,\
                   `order_type`, `detail_type`, `package_type`, `batch_processing_id`, `pck_state`, `change_state_time`,\
                   `in_ods_date_time`, `in_wsp_datetime`, `in_system_datetime`, `freight`, `total_price`,\
                   `actual_weight`, `goods_pck_weight`, `volume_weight`, `package_length`, `package_width`,\
                   `package_height`, `post_id`, `post_type_options`, `online_psot_type`, `trace_id`, `way_bill_no`,\
                   `delivery_date`, `delivery_user_id`, `delivery_user`, `receive_name`, `phone`, `country_id`,\
                   `country`, `county`, `city`, `buyer_address1`, `buyer_address2`, `zip`, `belonging`, `belonging_id`,\
                   `pck_remarks`, `platform_order_id`, `master_post_no_jump`, `is_part_delivery`,\
                   `is_gift_lack_delivery`, `processing_scheme`, `processing_scheme_remark`, `return_reason_name`,\
                   `return_reason_remark`, `create_date`, `create_user_id`, `create_user_name`, `modify_date`,\
                   `modify_user_id`, `modify_user_name`, `is_deleted`, `delete_date`, `delete_user_id`,\
                   `delete_user_name`, `modify_time_stamp`, `lock_version`, `ods_site_server`, `init_pck_volume`,\
                   `address`, `email`)\
    VALUES('{0}', '{1}', '{2}', '', '9', ',1,2,3,', 'normal', '1', '3',\
           'P17201911189009', '2', '2020-01-15 09:43:11', '2020-03-09 11:19:26', '2019-08-06 05:26:54',\
           '2019-08-06 04:40:03', '0.000', '142.100', '23.000', '5.820', '0.000', '112.00', '12.00', '11.00', '467',\
           '467', 'Post', 'UE102299418SH', NULL, '2020-01-15 16:43:11', '50561', '朱志亮', 'Sandra Hamilton', '', '164',\
           'NZ', 'NEW ZEALAND', 'Putaruru', '3 Grey Street', '3 Grey Street', '3411', '512271458702204928', '0', '',\
           'SO3718', NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2019-09-30 11:59:38', '1', '初始化服务',\
           '2020-01-15 09:43:11', '50561', '朱志亮', '\0', '2019-10-17 14:44:56', '39213', '彭刚', '2020-03-09 11:19:26',\
           '0', '', '30520.000', '', '');\
"
    attent_sql = "INSERT INTO `ews`.`ods_pck_attached` (`id`, `package_id`, `order_id`, `is_repeat_send`, `is_replenishment`, `is_split`, `setting`, `original_currency`, `original_amount`, `original_ship_fee`, `original_total_fee`, `platform_id`, `platform_name`, `store_id`, `store_name`, `logistics_account`, `order_track_type`, `region`, `area`, `weight_level`, `is_multi_storage_delivery`, `pack_require_id`, `deficit_price`, `lights_goods_freight`, `loss_condition`, `jettison_condition`, `is_cost_control`, `max_feight`, `package_service_fee`, `package_material_fee`, `create_date`, `create_user_id`, `create_user_name`, `modify_date`, `modify_user_id`, `modify_user_name`, `is_deleted`, `delete_date`, `delete_user_id`, `delete_user_name`, `modify_time_stamp`, `lock_version`, `sales_user_id`, `sales_user_name`, `product_manager_name`, `product_manager_id`, `lable_types`, `requirement_types`, `jump_abroad_warehouse_status`, `is_fulfilled`)" \
                 " VALUES " \
                 "('{0}', '{1}', '{2}', '\0', '\0', '\0', '', 'NZD', '218.080', '0.000', '218.080', '60', 'TradeMe', '7005', 'INSMA(TradeMe)', '00120', NULL, '中国大区', '华南区域', '0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '0.500', '2019-09-30 11:59:38', '1', '初始化服务', NULL, '0', '', '\0', NULL, '0', '', '1970-01-02 00:00:00', '0', '0', NULL, NULL, '43941', '', '10,11', '0', '0');\
"

    detail_sql = "INSERT INTO `ews`.`ods_pck_detail` (`id`, `package_id`, `item_id`, `item_name`, `base_product_name`, `base_packing_specification`, `sale_price`, `quantity`, `bar_code_id`, `sku`, `poa`, `bar_code`, `length`, `width`, `height`, `goods_spec`, `goods_attachment_id`, `item_delivery_weight`, `goods_manager_name`, `sales_user_name`, `platform_order_id`, `os_detail_id`, `transaction_id`, `create_date`, `create_user_id`, `create_user_name`, `modify_date`, `modify_user_id`, `modify_user_name`, `is_deleted`, `delete_date`, `delete_user_id`, `delete_user_name`, `modify_time_stamp`, `lock_version`, `order_detail_id`, `goods_id`, `bg_product_id`, `bg_property_id`, `adapter_num`, `is_get_rack`, `area`, `row`, `rack`, `position`, `is_default`, `stock_quantity`)\
                 VALUES ('{0}', '{1}', '0', '42\" Inch 1400W 5D Curved LED Work Light Bar Combo Offroad Lamp Car Truck +Wiring', 'xxx', '3', '0.0000', '1', NULL, 'SKU831415', '', NULL, '112.00', '12.00', '11.00', '', NULL, '2.900', NULL, NULL, '3700631183396502969', '1403114', NULL, '2019-09-30 11:59:37', '1', '初始化服务', NULL, '0', '', '\0', NULL, '0', '', '2019-10-10 14:28:58', '0', '471678158', '513598496801300480', '1226587', '0', '0', '1', '', '', '', '', '0', '0');\
"

    deliver_sql = "INSERT INTO `ews`.`pck_back_deliverycharge` (`id`, `package_id`, `delivery_id`, `unique_code`, `order_id`, `post_id`, `process_center_id`, `operation_type`, `fee_big_category`, `fee_small_category`, `amount`, `run_count`, `is_sync`, `is_delete`, `post_trader_id`, `weight`, `volume`, `charge_weight`, `currency`, `origin_amount`, `origin_currency`, `exchange_rate`, `belonging_id`, `create_date`, `create_user_id`, `create_user_name`, `modify_date`, `modify_user_id`, `modify_user_name`, `is_deleted`, `delete_date`, `delete_user_id`, `delete_user_name`, `modify_time_stamp`, `lock_version`)\
         VALUES \
         ('1{0}', '{1}', '646058483401367552', '0eae8b2e-ae87-4a86-aff6-275946f83d42', '{2}', '149', '7', '交寄', '运费', '基础运费', '83.757', '0', '\0', '\0', '18', '1.580', '0.000', '1.580', 'CNY', '16.274', 'SGD', '5.147', '0', '2019-11-18 18:45:46', '39213', '彭刚', '2020-01-15 09:43:11', '0', '', '\0', NULL, '0', '', '2020-01-15 15:06:50', '0'),\
('2{0}', '{1}', '646058483401367552', '634439b1-618b-4a71-b37b-3933be89d2e7', '{2}', '149', '7', '交寄', '运费', '处理费', '6.691', '0', '\0', '\0', '18', '1.580', '0.000', '1.580', 'CNY', '1.300', 'SGD', '5.147', '0', '2019-11-18 18:45:46', '39213', '彭刚', '2020-01-15 09:43:11', '0', '', '\0', NULL, '0', '', '2020-01-15 15:06:51', '0'),\
('3{0}', '{1}', '646058483401367552', 'bca6deeb-0153-45eb-8738-050f5f3e5a41', '{2}', '149', '7', '交寄', '运费', '空运费', '31.600', '0', '\0', '\0', '156', '1.580', '0.000', '1.580', 'CNY', '31.600', 'CNY', '1.000', '0', '2019-11-18 18:45:46', '39213', '彭刚', '2020-01-15 09:43:11', '0', '', '\0', NULL, '0', '', '2020-01-15 15:06:52', '0'),\
('4{0}', '{1}', '646058483401367552', '41ead6ee-8fd6-4416-8382-2ee5931ba7b6', '{2}', '149', '7', '交寄', '运费', '清关手续费', '3.160', '0', '\0', '\0', '17', '1.580', '0.000', '1.580', 'CNY', '3.160', 'CNY', '1.000', '0', '2019-11-18 18:45:46', '39213', '彭刚', '2020-01-15 09:43:11', '0', '', '\0', NULL, '0', '', '2020-01-15 15:06:53', '0'),\
('5{0}', '{1}', '646058483401367552', 'd342e9da-9512-4cb4-a909-af9c86200112', '{2}', '149', '7', '交寄', '运费', '燃油附加费', '2.513', '0', '\0', '\0', '17', '1.580', '0.000', '1.580', 'CNY', '0.488', 'SGD', '5.147', '0', '2019-11-18 18:45:46', '39213', '彭刚', '2020-01-15 09:43:11', '0', '', '\0', NULL, '0', '', '2020-01-15 15:06:54', '0'),\
('6{0}', '{1}', '646058483401367552', '904b16cb-6e71-4ba8-9d1b-8ba31e36b61e', '{2}', '149', '7', '交寄', '运费', '打包服务费', '0.201', '0', '\0', '\0', '17', '1.580', '0.000', '1.580', 'CNY', '0.039', 'SGD', '5.147', '0', '2019-11-18 18:45:46', '39213', '彭刚', '2020-01-15 09:43:11', '0', '', '\0', NULL, '0', '', '2020-01-15 15:17:49', '0'),\
('7{0}', '{1}', '646058483401367552', '28e5395a-8e54-4704-9a8f-3f0e05aa9048', '{2}', '149', '7', '交寄', '包装材料费', '包装材料费', '0.500', '0', '\0', '\0', '', '0.000', '0.000', '0.000', 'CNY', '0.500', 'CNY', '1.000', '0', '2019-11-18 18:45:46', '39213', '彭刚', '2020-01-15 09:43:11', '0', '', '\0', NULL, '0', '', '2020-01-15 15:06:55', '0'),\
('8{0}', '{1}', '666940437211815936', '6032b059-07a2-43f8-98b1-c4bfdc8f4324', '{2}', '467', '9', '还原交寄', '全部费用', '全部费用', '-128.422', '0', '\0', '\0', '', '0.000', '0.000', '0.000', 'CNY', '0.000', '', '0.000', '0', '2020-01-15 09:43:11', '50561', '朱志亮', '2020-01-15 09:43:11', '0', '', '\0', NULL, '0', '', '2020-01-15 15:06:57', '0');\
"

    id_num = "20200310"
    pck = "UPCK00"
    ord = "uA00"
    db = connect_db('ods_mydb')

    cursor = db.cursor()
    for i in range(1, 2):
        num = str(id_num + str(i))
        print(deliver_sql.format(num, pck + num,ord+num))
        if i % 1000 == 0:
            cursor.close()
            db.commit()
            cursor = db.cursor()
        cursor = db.cursor()
        # try:
        #     cursor.execute(info_sql.format(num, pck+num, ord+num))
        # except pymysql.err.IntegrityError:
        #     print('已存在个数{0}'.format(num))
        #     pass
        # try:
        #     cursor.execute(attent_sql.format(num, pck+num, ord+num))
        # except pymysql.err.IntegrityError:
        #     print('已存在个数{0}'.format(num))
        #     pass
        # try:
        #     cursor.execute(detail_sql.format(num, pck + num))
        # except pymysql.err.IntegrityError:
        #     print('已存在个数{0}'.format(num))
        #     pass
        try:
            cursor.execute(deliver_sql.format(num, pck + num,ord+num))
        except pymysql.err.IntegrityError:
            print('已存在个数{0}'.format(num,pck+num,ord+num))
            pass

    cursor.close()
    db.commit()
    db.close()

def db_inser(process):
    info_sql = "INSERT INTO `ews`.`ods_pck_info` (`id`,`package_id`, `order_id`, `batchgridorderdata_id`, `process_center_id`, `delivery_type`, `order_type`, `detail_type`, `package_type`, `batch_processing_id`, `pck_state`, `change_state_time`, `in_ods_date_time`, `in_wsp_datetime`, `in_system_datetime`, `freight`, `total_price`, `actual_weight`, `goods_pck_weight`, `volume_weight`, `package_length`, `package_width`, `package_height`, `post_id`, `post_type_options`, `online_psot_type`, `trace_id`, `way_bill_no`, `delivery_date`, `delivery_user_id`, `delivery_user`, `receive_name`, `phone`, `country_id`, `country`, `county`, `city`, `buyer_address1`, `buyer_address2`, `zip`, `belonging`, `belonging_id`, `pck_remarks`, `platform_order_id`, `master_post_no_jump`, `is_part_delivery`, `is_gift_lack_delivery`, `processing_scheme`, `processing_scheme_remark`, `return_reason_name`, `return_reason_remark`, `create_date`, `create_user_id`, `create_user_name`, `modify_date`, `modify_user_id`, `modify_user_name`, `is_deleted`, `delete_date`, `delete_user_id`, `delete_user_name`, `modify_time_stamp`, `lock_version`, `ods_site_server`, `init_pck_volume`, `address`, `email`) \
    VALUES\
    ( '{0}','{1}',\
     '{2}', '', '1022', ',1,2,3,', 'normal', '3', '3',\
    NULL, '1', '2019-11-22 17:27:09', '2020-03-04 11:30:51', '2019-11-21 15:35:07', '2019-11-21 14:56:51',\
    NULL, '11.800', NULL, '0.220', '0.000', '0.00', '0.00', '0.00', '726', '726|0,678|0,634|0,104|0,727|0,755|0,725|0',\
    '', NULL, NULL, NULL, NULL, NULL, 'Tanya Cajot', '07772 196980', '237', 'UNITED KINGDOM', 'UNITED KINGDOM', 'Swansea',\
    '12 Wern Fawr Road,  Port Tennant', '', 'SA1 8LQ', '516925542164078592', '0', '', '5dd5c14c44f59b48cd3889d9', '1'\
    , NULL, NULL, NULL, NULL, NULL, NULL, '2019-11-22 17:27:09', '1', '初始化服务', '2019-11-26 16:53:37', '1', 'ODS模拟交寄', '\0', NULL, '0', '', '2020-03-04 11:30:51', '0', '', '0.000', '', '');\
    "

    attent_sql = "INSERT INTO\
     `ews`.`ods_pck_attached` (`id`, `package_id`, `order_id`, `is_repeat_send`, `is_replenishment`, `is_split`, `setting`, `original_currency`, `original_amount`, `original_ship_fee`, `original_total_fee`, `platform_id`, `platform_name`, `store_id`, `store_name`, `logistics_account`, `order_track_type`, `region`, `area`, `weight_level`, `is_multi_storage_delivery`, `pack_require_id`, `deficit_price`, `lights_goods_freight`, `loss_condition`, `jettison_condition`, `is_cost_control`, `max_feight`, `package_service_fee`, `package_material_fee`, `create_date`, `create_user_id`, `create_user_name`, `modify_date`, `modify_user_id`, `modify_user_name`, `is_deleted`, `delete_date`, `delete_user_id`, `delete_user_name`, `modify_time_stamp`, `lock_version`, `sales_user_id`, `sales_user_name`, `product_manager_name`, `product_manager_id`, `lable_types`, `requirement_types`, `jump_abroad_warehouse_status`, `is_fulfilled`)\
     VALUES ('{0}', '{1}', '{2}', '\0', '\0', '\0', '', 'USD', '8.900', '2.900', '11.800', '17', 'Wish', '3988', 'vvfashion2016', '00034', NULL, '欧洲大区', '英国区域', '0', NULL, '10,32,639843222662946816,', NULL, NULL, NULL, NULL, NULL, NULL, '2.000', '0.500', '2019-11-22 17:27:09', '1', '初始化服务', NULL, '0', '', '\0', NULL, '0', '', '1970-01-02 00:00:00', '0', '9403', '邹虹', '张苏燕', '3132', '', '', '0', '0'\
    );\
    "

    detail_sql = "INSERT INTO `ews`.`ods_pck_detail` \
(`id`, `package_id`, `item_id`, `item_name`, `base_product_name`, `base_packing_specification`, `sale_price`, `quantity`, `bar_code_id`, `sku`, `poa`, `bar_code`, `length`, `width`, `height`, `goods_spec`, `goods_attachment_id`,\
 `item_delivery_weight`, `goods_manager_name`, `sales_user_name`, `platform_order_id`, `os_detail_id`, `transaction_id`, `create_date`, `create_user_id`, \
`create_user_name`, `modify_date`, `modify_user_id`, `modify_user_name`, `is_deleted`, `delete_date`, `delete_user_id`, `delete_user_name`, `modify_time_stamp`, `lock_version`,\
 `order_detail_id`, `goods_id`, `bg_product_id`, `bg_property_id`, `adapter_num`, `is_get_rack`, `area`, `row`, `rack`, `position`, `is_default`, `stock_quantity`)\
 VALUES ('{0}', '{1}', '0', 'Right Side Driver Tail Rear Light For Mitsubishi L200 Triton Fiat Strada 2015 On', 'xxx', '3', '0.0000', '1', \
NULL, 'SKU642785', '', NULL, '42.00', '31.00', '14.00', '', NULL, '1.400', NULL, NULL, '113602221517', NULL, NULL, '2019-11-22 17:27:07', '1', '初始化服务', NULL, '0', \
'', '\0', NULL, '0', '', '1970-01-02 00:00:00', '0', '496045364', '513388542458863616', '1344026', '0', '0', '1', '', '', '', '', '0', '0');\
                "

    deliver_sql = "INSERT INTO `ews`.`pck_back_deliverycharge` (`id`, `package_id`, `delivery_id`, `unique_code`, `order_id`, `post_id`, `process_center_id`, `operation_type`, `fee_big_category`, `fee_small_category`, `amount`, `run_count`, `is_sync`, `is_delete`, `post_trader_id`, `weight`, `volume`, `charge_weight`, `currency`, `origin_amount`, `origin_currency`, `exchange_rate`, `belonging_id`, `create_date`, `create_user_id`, `create_user_name`, `modify_date`, `modify_user_id`, `modify_user_name`, `is_deleted`, `delete_date`, `delete_user_id`, `delete_user_name`, `modify_time_stamp`, `lock_version`)\
             VALUES \
             ('1{0}', '{1}', '646058483401367552', '0eae8b2e-ae87-4a86-aff6-275946f83d42', '{2}', '149', '7', '交寄', '运费', '基础运费', '83.757', '0', '\0', '\0', '18', '1.580', '0.000', '1.580', 'CNY', '16.274', 'SGD', '5.147', '0', '2019-11-18 18:45:46', '39213', '彭刚', '2020-01-15 09:43:11', '0', '', '\0', NULL, '0', '', '2020-01-15 15:06:50', '0'),\
    ('2{0}', '{1}', '646058483401367552', '634439b1-618b-4a71-b37b-3933be89d2e7', '{2}', '149', '7', '交寄', '运费', '处理费', '6.691', '0', '\0', '\0', '18', '1.580', '0.000', '1.580', 'CNY', '1.300', 'SGD', '5.147', '0', '2019-11-18 18:45:46', '39213', '彭刚', '2020-01-15 09:43:11', '0', '', '\0', NULL, '0', '', '2020-01-15 15:06:51', '0'),\
    ('3{0}', '{1}', '646058483401367552', 'bca6deeb-0153-45eb-8738-050f5f3e5a41', '{2}', '149', '7', '交寄', '运费', '空运费', '31.600', '0', '\0', '\0', '156', '1.580', '0.000', '1.580', 'CNY', '31.600', 'CNY', '1.000', '0', '2019-11-18 18:45:46', '39213', '彭刚', '2020-01-15 09:43:11', '0', '', '\0', NULL, '0', '', '2020-01-15 15:06:52', '0'),\
    ('4{0}', '{1}', '646058483401367552', '41ead6ee-8fd6-4416-8382-2ee5931ba7b6', '{2}', '149', '7', '交寄', '运费', '清关手续费', '3.160', '0', '\0', '\0', '17', '1.580', '0.000', '1.580', 'CNY', '3.160', 'CNY', '1.000', '0', '2019-11-18 18:45:46', '39213', '彭刚', '2020-01-15 09:43:11', '0', '', '\0', NULL, '0', '', '2020-01-15 15:06:53', '0'),\
    ('5{0}', '{1}', '646058483401367552', 'd342e9da-9512-4cb4-a909-af9c86200112', '{2}', '149', '7', '交寄', '运费', '燃油附加费', '2.513', '0', '\0', '\0', '17', '1.580', '0.000', '1.580', 'CNY', '0.488', 'SGD', '5.147', '0', '2019-11-18 18:45:46', '39213', '彭刚', '2020-01-15 09:43:11', '0', '', '\0', NULL, '0', '', '2020-01-15 15:06:54', '0'),\
    ('6{0}', '{1}', '646058483401367552', '904b16cb-6e71-4ba8-9d1b-8ba31e36b61e', '{2}', '149', '7', '交寄', '运费', '打包服务费', '0.201', '0', '\0', '\0', '17', '1.580', '0.000', '1.580', 'CNY', '0.039', 'SGD', '5.147', '0', '2019-11-18 18:45:46', '39213', '彭刚', '2020-01-15 09:43:11', '0', '', '\0', NULL, '0', '', '2020-01-15 15:17:49', '0'),\
    ('7{0}', '{1}', '646058483401367552', '28e5395a-8e54-4704-9a8f-3f0e05aa9048', '{2}', '149', '7', '交寄', '包装材料费', '包装材料费', '0.500', '0', '\0', '\0', '', '0.000', '0.000', '0.000', 'CNY', '0.500', 'CNY', '1.000', '0', '2019-11-18 18:45:46', '39213', '彭刚', '2020-01-15 09:43:11', '0', '', '\0', NULL, '0', '', '2020-01-15 15:06:55', '0'),\
    ('8{0}', '{1}', '666940437211815936', '6032b059-07a2-43f8-98b1-c4bfdc8f4324', '{2}', '467', '9', '还原交寄', '全部费用', '全部费用', '-128.422', '0', '\0', '\0', '', '0.000', '0.000', '0.000', 'CNY', '0.000', '', '0.000', '0', '2020-01-15 09:43:11', '50561', '朱志亮', '2020-01-15 09:43:11', '0', '', '\0', NULL, '0', '', '2020-01-15 15:06:57', '0');\
    "

    id_num=""
    pck = ""
    ord = ""
    if process=='UK':
            id_num="20200309"
            pck="QPCK00"
            ord="QA00"
    elif process=='US':
            id_num = "120200309"
            pck = "usPCK00"
            ord = "usA00"

    db = connect_db('ods_mydb')
    db_list = []
    cursor = db.cursor()
    for i in range(10000,60000):
        num = str(id_num+str(i))
        # print(num)
        if i%1000==0:
            cursor.close()
            db.commit()
            cursor = db.cursor()

        # try:
        #     cursor.execute(info_sql.format(num, pck+num, ord+num))
        # except pymysql.err.IntegrityError:
        #     print('已存在个数{0}'.format(num))
        #     pass
        # try:
        #     cursor.execute(attent_sql.format(num, pck+num, ord+num))
        # except pymysql.err.IntegrityError:
        #     print('已存在个数{0}'.format(num))
        #     pass
        # try:
        #     cursor.execute(detail_sql.format(num,pck+num))
        # except pymysql.err.IntegrityError:
        #     print('已存在个数{0}'.format(num))
        #     pass
        try:
            cursor.execute(deliver_sql.format(num, pck + num,ord+num))
        except pymysql.err.IntegrityError:
            print('已存在个数{0}'.format(num,pck+num,ord+num))
            pass

    cursor.close()
    db.commit()
    db.close()
# def db_dele DELETE FROM
    id_num = "20200310"
    db = connect_db('ods_mydb')
def db_delete():
    info_sql = "DELETE FROM `ews`.`ods_pck_info` WHERE id='{0}'"
    attent_sql = "DELETE FROM `ews`.`ods_pck_attached` WHERE id='{0}'"
    detail_sql = "DELETE FROM `ews`.`ods_pck_detail` WHERE id='{0}'"

    deliver_sql = "DELETE FROM `ews`.`pck_back_deliverycharge` WHERE id lkie '_{0}%"

    # id_num = "120200309"
    id_num = "20200309"

    db = connect_db('ods_mydb')
    db_list = []
    cursor = db.cursor()
    for i in range(1,148000):
        num = str(i)
        # print(num)
        if i % 1000 == 0:
            cursor.close()
            db.commit()
            cursor = db.cursor()
        # if i==20:
        #     break

        cursor = db.cursor()
        try:
            # try:
            #     cursor.execute(info_sql.format(id_num+num ))
            # except pymysql.err.IntegrityError:
            #     print('已存在个数{0}'.format(num))
            #     pass
            # try:
            #     cursor.execute(attent_sql.format(id_num+num))
            # except pymysql.err.IntegrityError:
            #     print('已存在个数{0}'.format(num))
            #     pass
            try:
                # cursor.execute(detail_sql.format(num))
                cursor.execute(detail_sql.format((id_num+num)))
            except pymysql.err.IntegrityError:
                print('已存在个数{0}'.format(num))
                pass
        except:
            cursor.close()
            db.commit()
            db.close()

    cursor.close()
    db.commit()
    db.close()

if __name__=="__main__":
    db_inser('UK')
    # db_delete()
    # usdb_inser()