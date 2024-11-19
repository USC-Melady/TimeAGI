from flask import Flask, jsonify, send_from_directory, render_template
from flask_frozen import Freezer
import sqlite3

app = Flask(__name__)
freezer = Freezer(app)  # 初始化静态化工具

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data-show.html')
def datashow():
    data_container = []
    con = sqlite3.connect('datashow.db')
    cur = con.cursor()
    data_cur = cur.execute('select * from inputdata1')
    for rows in data_cur:
        data_container.append(rows)

    cur.close()
    con.close()
    return render_template('data-show.html', data_container=data_container)

@app.route('/document.html')
def document():
    return render_template('document.html')

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "freeze":
        # 执行静态化
        freezer.freeze()
    else:
        # 启动开发服务器
        app.run(host="127.0.0.1", port=8848, debug=True)
