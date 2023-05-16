import time

from db_ac.modular.mapper import connect_DB





class GoodsClass(object):
    def __init__(self):
        self.wms_db = "ods_mysql"
        self.wsp_db = "wsp_mysql"
        self.wms_cursor = connect_DB(self.wms_db)
        self.wsp_cursor = connect_DB(self.wsp_db)

        select_goods_external='select * from goods_bar_code order by id desc limit 1 '
        self.new_id = self.wsp_cursor.fetchone(select_goods_external)[0]
        self.new_id = int(self.new_id) + 1


    def find_goods(self,goods_ids):

        select_goods = """select *
        from goods_mapper_bg_product
        where id in ({0});
         """
        goods_info = self.wsp_cursor.fetchone(select_goods.format(goods_ids))
        goods_id=goods_info[1]
        sku_code=goods_info[4]
        poa_code=goods_info[5]
        goods_code=poa_code
        if goods_code=='':
            goods_code=sku_code
        print(goods_id,goods_code)

        self.insert_goods_extentd(goods_id,goods_code)
        pass

    def insert_goods_extentd(self,goods_id,goods_code):

        insert_goods_external="""
INSERT INTO goods_bar_code (id, goods_id, goods_code, is_default, external_code, master_id, create_user_id,
                                create_date, create_user_name, modify_user_id, modify_date, modify_user_name,
                                delete_user_id, delete_date, delete_user_name, is_deleted, delete_unique_key,
                                lock_version)
VALUES ({0}, {1}, '{2}', true, '{2}', 516925542164078592, 1,
        '{3}', 'admin', 0, '1970-01-01 00:00:00', '', 0, '1970-01-01 00:00:00', '', false, 0, 0);"""

        self.new_id = int(self.new_id) + 1
        now_date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(self.new_id)
        self.wsp_cursor.execute(insert_goods_external.format(self.new_id,goods_id,goods_code,now_date))




    def commit(self):
        self.wsp_cursor.commitAndClose()
        # cursor.commitAndClose()




if __name__ == "__main__":
    goods_ids = [51301812443048356,51301812529451008]
    goods_action = GoodsClass()
    for goods_id in goods_ids:
        goods_action.find_goods(goods_id)

    goods_action.commit()




    pass