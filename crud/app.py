from flask import *
import sqlite3

app=Flask(__name__) 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create_',methods=['post','get'])
def create_():
    try:
        con=sqlite3.connect('e:/contact.sqlite')
        con.execute('create table contact(id integer primary key,name,email,cell,designation,web)')
        con.commit()
        con.close()
    except:
        return render_template('create_no.html')
    return render_template('create_yes.html')


@app.route('/insert')
def insert():
    return render_template('insert.html')

@app.route('/insert_',methods=['post','get'])
def insert_():
    if request.method=='POST':
        try:
            p_name=request.form['h_name']
            p_email=request.form['h_email']
            p_cell=request.form['h_cell']
            p_designation=request.form['h_designation']
            p_web=request.form['h_web']
            with sqlite3.connect('e:/contact.sqlite') as con:
                cur=con.cursor()
                cur.execute('insert into contact(name,email,cell,designation,web) values(?,?,?,?,?)',(p_name,p_email,p_cell,p_designation,p_web))
                con.commit() 
                cur.close()
        except sqlite3.error as error:
            con.rollback()
            return render_template('insert_no.html')
        finally:
            if con: con.close()
        return render_template('insert_yes.html')
        
@app.route('/select')
def select():
    try:
       with sqlite3.connect('e:/contact.sqlite') as con:
        con.row_factory = sqlite3.Row
        cur=con.cursor()
        cur.execute('select*from contact')
        p_rows=cur.fetchall()
        cur.close()
    except sqlite3.error as error:
        print(error)
    finally:
        if con:
            con.close()
    return render_template('select.html',h_rows=p_rows)  

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')



if __name__=='__main__':
    app.run()
