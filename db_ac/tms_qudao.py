from mysql_connect import connect_db

import pymysql


# 12348671f2ec850171f33b04840008
def t_package_inser(sql):
    db = connect_db('tms_mysql')

    cursor = db.cursor()



    id_num = "12348671f2ec850171f33b04841"
    # id_num = "12348673f2ec850171f33b04841"
    for i in range(1,200):
        num = str(id_num + str(i))
        if i % 1000 == 0:
            cursor.close()
            db.commit()
            cursor = db.cursor()
        cursor = db.cursor()
        try:
            cursor.execute(sql.format(num))
            print('执行个数{0}'.format(i))
        except pymysql.err.IntegrityError as e:
            print('已存在个数{0}'.format(e))
            pass


    cursor.close()
    db.commit()
    db.close()


if  __name__=="__main__":
    info_sql = "INSERT INTO tms.t_package (id,country,dispose_addr,package_code,pkg_code,send_name,weight,create_date,dispose_code,carrier_name,send_date,status,status_name,trace_id,freight,receive_name,carrier_code,country_code) VALUES \
    ('{0}','尼日利亚','华南服装处理中心','A0000519080600CE','PKG08997842','彭刚',1,'2020-05-08 15:41:03','1111','中外运-西邮经济小包','2020-03-18 15:51:12','4','已交寄','',105.174,'ashley hayland','642','NG')\
    ;\
        "
    delete_sql = "delete from tms.t_package  where  id={0}"

t_package_inser(delete_sql)
# t_package_inser(info_sql)