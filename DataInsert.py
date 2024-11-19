import csv
import pymysql

# 主实例连接信息
host = "aurora-test.c16iw8gmmux2.us-east-2.rds.amazonaws.com"
port = 3306
user = "hauxleee"
password = "hauxleee"
db = "myfirstDB"

# table_name = "ModelData"  # 表1名称
table_name = "InputData2"  # 表2名称

# CSV 文件路径
# csv_file_path = 'data/InputData1.csv' # 表1路径
csv_file_path = 'data/InputData2.csv' # 表2路径


# 打开 CSV 文件并读取
with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    # 打印列名
    print(reader.fieldnames)

# with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row)  # 打印当前行的数据，以确认结构
#         # 以下是原有的插入操作代码


try:
    # 连接到数据库
    conn = pymysql.connect(host=host, user=user, passwd=password, db=db, port=port, charset='utf8')
    print("Connected successfully")

    # 创建一个cursor对象
    cursor = conn.cursor()

    # 打开 CSV 文件并读取
    with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)  # 使用DictReader读取，这样可以按列名访问每行的数据
        for row in reader:
            # 构造 INSERT 语句，%s 是参数占位符
            insert_query = f"INSERT INTO {table_name} (model_name, dataset, pred_len, MSE, MAE) VALUES (%s, %s, %s, %s, %s)"
            # 执行插入操作
            cursor.execute(insert_query, (row['model_name'], row['dataset'], row['pred_len'], row['MSE'], row['MAE']))

    # 提交事务
    conn.commit()
    print("data inserted successfully")
except pymysql.MySQLError as e:
    print("Error: ", e)
finally:
    if conn:
        # 关闭数据库连接
        conn.close()
