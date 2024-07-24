import sqlite3

from flask import Flask, redirect, render_template, request, url_for

app=Flask(__name__)
DATABASE='database.db'
TABLE_NAME='tasks'
def create_table(tasks):
    con=sqlite3.connect(DATABASE)
    z="""CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINNCREMENT,title TEXT NOT NULL, description TEXT,status INTEGER DEFAULT 0)"""
    con.execute(z)
create_table
@app.route('/')
def index():
    con=sqlite3.connect(DATABASE)
    cursor=con.cursor()
    cursor.execute(f'SELECT * FROM tasks ')
    tasks=cursor.fetchall()
    con.close()
    return render_template('index.html',tasks=tasks)
@app.route('/add',methods=['POST'])
def add():
    title=request.form['title']
    description=request.form["description"]
    con=sqlite3.connect(DATABASE)
    cursor=con.cursor()
    cursor.execute(f"INSERT INTO tasks (title,descrption) VALUES (?,?)",(title,description))
    con.commit()
    con.close()
    return redirect(url_for('index'))
@app.route("/update/<int:task_id>/<int:status>",methods=['GET'])
def update(task_id,status):
    con=sqlite3.connect(DATABASE)
    cursor=con.cursor()
    con.execute(f"UPDATE tasks SET status=? WHERE id=?",(status,task_id))
    con.commit()
    con.close()
    return redirect(url_for('index'))
@app.route('/delete/<int:task_id>',methods=['GET'])
def delete(task_id):
    con=sqlite3.connect(DATABASE)
    cursor=con.cursor()
    cursor.execute(f'DELETE FROM tasks WHERE id =?',(task_id))
    con.commit()
    con.close()
    return redirect(url_for('index'))
if __name__=='__main__':
    app.run(debug=True)