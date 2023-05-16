import time

from db_ac.modular.mapper import connect_DB



# wms_db = "ods_mysql"
wsp_db = "wsp_mysql"


def largeGoodsBoxInsertByWsp(id,shift_id,shift_code,box_code):
    cursor1 = connect_DB(wsp_db)

    insertSql="""INSERT INTO wsp.large_goods_box (id, product_shift_id, product_shift_code, product_shift_box_code,
                                 origin_process_center_id, target_process_center_id, ship_type, length, width, height,
                                 weight, status, serial_number, priority_level, create_user_id, create_date,
                                 create_user_name, modify_date, modify_user_id, modify_user_name, is_deleted)
VALUES ({0}, {1}, '{2}', '{3}', 7, 1078, 4, 42.500,
        23.700, 12.500, 12.500, 0, 0, 0, 45712, '2021-10-25 11:03:21', '李丹坡（X）', '2021-10-25 11:03:21', 45712, '李丹坡（X）',
        0);"""

    cursor1.execute(insertSql.format(id, shift_id,shift_code,box_code))
    cursor1.commitAndClose()
if __name__=="__main__":
    id = 2150335246327921
    shift_id=5625936129872414521
    shift_code="SFT-A1-20210322-5002A"
    box_code="Fbox-20210623-"
    for i in range(50,100):
        box_code = "Fbox-20210623-"
        id+=i
        shift_id+=i
        box_code=box_code + str(1008+i)
        print(box_code)
        largeGoodsBoxInsertByWsp(id,shift_id,shift_code,box_code)
        time.sleep(0.5)
