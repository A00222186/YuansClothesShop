from flask import Flask,render_template,request,redirect,url_for
from flaskext.mysql import MySQL
import traceback


app = Flask(__name__)
mysql=MySQL()

#Mysql configurations
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='admin'
app.config['MYSQL_DATABASE_DB']='yuanshop'
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_PORT']=3306
mysql.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def user_route(name):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * from User")
    data=cursor.fetchone()
    return render_template('index.html',name=name)

@app.route('/registuser')
def register():
    return render_template('login.html')
def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/register')
def getRigistRequest():
    conn = mysql.connect()
    cursor = conn.cursor()

    sql = "INSERT INTO usertable(username, userpassword,birthday,gender) VALUES (\'" + request.args.get('username') + "\',\'" + request.args.get('userpassword') + "\', \'" + request.args.get(
        'birthday') + "\',\'" + request.args.get('gender') + "\')"

    print (sql)

    try:

        cursor.execute(sql)

        conn.commit()
        conn.close()
        return render_template('login.html')
    except:

        traceback.print_exc()

        conn.rollback()
        return 'failed'
        conn.close()

if __name__ == '__main__':
    app.run()
