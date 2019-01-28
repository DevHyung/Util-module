import pymysql.cursors
from openpyxl import  load_workbook
from datetime import datetime
# Assuming you have a cursor named cursor you want to exe
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='autoset',
                             db='psm',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


now = datetime.now()

try:
    tEx = load_workbook(filename='sample.xlsx')
    sheet1 = tEx.active
    data = []
    for i in sheet1.rows:
        num = i[0].value
        keyword = i[1].value
        domain = i[2].value
        address = i[3].value
        t = [num, keyword, domain, address]
        data.append(t)
    data = data[1:]
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `keyword`(`workNum`,`keyword`,`area`,`url`,`registerD`,`updateD`)  \
              VALUES (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE keyword=%s,area=%s,url=%s,updateD=%s;  "
        for d in data:
            cursor.execute(sql, (d[0],d[1],d[2],d[3],now,now,d[1],d[2],d[3],now))
    connection.commit()
    print(">>> 총 {} 개 데이터 입력완료".format(len(data)))
    _ = input(">>> 끝내려면 엔터를 눌러주세요 :")
finally:
    connection.close()

