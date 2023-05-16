
import pymssql

from db_ac.modular.mapper import connect_sqlserve


def sqlServerConnect():
    server='sqltest.banggood.cn'
    database = 'SellerCube'
    user='skb-test'
    password='banggood!@#123'
    conn = pymssql.connect(server, user, password, database)
    cursor = conn.cursor(as_dict=True)
    cursor.execute('select top 1 * from ProductPriceInProcessCenter order by id desc ;')
    row = cursor.fetchone()
    while row:
        print("ID=%d, Name=%s" % (row[0], row[1]))
        row = cursor.fetchone()

def mapperConnect():
    a=connect_sqlserve('sql_servetest')
    row=a.fetchone('select top 1 * from ProductPriceInProcessCenter order by id desc ;')
    # row = connect_sqlserve.fetchone()
    while row:
        print("ID=%d, Name=%s" % (row[0], row[1]))
        # row = cursor.fetchone()




if __name__ == "__main__":
    sqlServerConnect()