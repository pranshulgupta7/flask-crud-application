from flask import Flask, render_template, request, redirect, url_for
# import flask
import sqlite3 as lite
import sys
# from flask_mysqldb import MySQL

app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'flaskuser'
# app.config['MYSQL_PASSWORD'] = 'flask'
# app.config['MYSQL_DB'] = 'musicdb'

# mysql = MYSQL(app)

# con = None

@app.route('/')
def Index():
    con = lite.connect('music.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM music")
    data = cur.fetchall()
    # cur.close()
    # return render_template('index.html')
    return render_template('index.html', music = data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        name = request.form['name']
        composedBy = request.form['composedBy']
        singer = request.form['singer']

        con = lite.connect('music.db')
        with con:
            cur = con.cursor()
            # cur.execute("DROP TABLE IF EXISTS music")
            # cur.execute("CREATE TABLE music(id INTEGER PRIMARY KEY AUTOINCREMENT, musicName TEXT, composedBy TEXT, singer TEXT)")
            cur.execute("INSERT INTO music(id,musicName, composedBy, singer) VALUES(NULL,'"+name+"','"+ composedBy+"','"+ singer+"')")
            # con.close()
        return redirect(url_for('Index'))

@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        print(id)
        # id_data = id
        name = request.form['name']
        print(name)
        composedBy = request.form['composedBy']
        singer = request.form['singer']

        con = lite.connect('music.db')
        cur = con.cursor()


        print("**********update query**************")
        print("UPDATE music SET musicName='"+ name +"', composedby='"+composedBy+"', singer='"+singer+"' WHERE id="+id_data)


        cur.execute("UPDATE music SET musicName='"+ name +"', composedby='"+composedBy+"', singer='"+singer+"' WHERE id="+id_data)
        con.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<id_data>',methods=['GET'])
def delete(id_data):
    con = lite.connect('music.db')
    cur = con.cursor()
    cur.execute("DELETE FROM music WHERE id="+id_data)
    con.commit()
    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)