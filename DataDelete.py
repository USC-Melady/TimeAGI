import pymysql

# 主实例连接信息
host = "aurora-test.c16iw8gmmux2.us-east-2.rds.amazonaws.com"
port = 3306
user = "hauxleee"
password = "hauxleee"
db = "myfirstDB"

try:
    # 使用pymysql连接到数据库
    conn = pymysql.connect(host=host, user=user, passwd=password, db=db, port=port)
    print("Connected successfully")

    # 创建一个cursor对象
    cursor = conn.cursor()

    # 删除users表中的所有数据的SQL语句
    delete_sql = "DELETE FROM users;"

    # 执行删除操作
    cursor.execute(delete_sql)

    # 提交到数据库执行
    conn.commit()
    print("All data deleted successfully")
except pymysql.MySQLError as e:
    print("Error: ", e)
finally:
    if conn:
        conn.close()
