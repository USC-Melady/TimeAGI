from flask import Flask, jsonify, send_from_directory,render_template
import sqlite3
#import pymysql

app = Flask(__name__)
 



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/data-show')
def datashow():
    data_container=[]
    con = sqlite3.connect('datashow.db')
    cur = con.cursor()
    data_cur= cur.execute('select * from inputdata1')
    for rows in data_cur:
        data_container.append(rows)

    cur.close()
    con.close()
    return render_template('data-show.html', data_container=data_container)

@app.route('/other-data-show')
def otherdatashow():
    data_container=[]
    con = sqlite3.connect('datashow.db')
    cur = con.cursor()
    data_cur= cur.execute('select * from inputdata2')
    for rows in data_cur:
        data_container.append(rows)

    cur.close()
    con.close()
    return render_template('otherdatashow.html',data_container=data_container)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/document')
def document():
    return render_template('document.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog-grid')
def blog_grid():
    return render_template('blog-grid.html')

@app.route('/blog-single')
def blog_single():
    return render_template('blog-single.html')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8848, debug=True)
