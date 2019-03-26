from flask import Flask,render_template,request
import traceback
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

#Mysql configurations
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='admin'
app.config['MYSQL_DATABASE_DB']='yuanshop'
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_CHARSET']='utf8'
app.config['MYSQL_USE_UNICODE']= True
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

def findID(id):
    id = request.values.get(id)
    return id

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/product/<id>')
def getPro(id):
    ID = findID(id)
    cursor.execute('''SELECT * from Product where productid like %s''' % id)
    productid = cursor.fetchone()

    print (productid[0])
    print (productid[1])
    print (productid[2])
    print (productid[3])
    print (productid[4])
    print (productid[5])
    print (productid[6])
    print (productid[7])

    return render_template('product-details.html', ID=ID, productid=productid)

@app.route('/registuser')
def register():
    return render_template('login.html')
def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/register')
def getRigistRequest():
    print("Establishing Connection")
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
