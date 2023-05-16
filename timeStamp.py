import time, datetime



tss1 = '2022-02-10 22:00:10'
 # 转为时间数组
timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
# dt_new = datetime.datetime.strptime(tss1, '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M:%S.%f')
dt_new = datetime.datetime(2022,2,10,22,00,10,11)

print(dt_new)
 # timeArray可以调用tm_year等
 # 转为时间戳
stamp = int(time.mktime(timeArray))

print(stamp)
