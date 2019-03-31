
from flask import Flask,render_template,request,redirect,url_for,session,escape
from flaskext.mysql import MySQL
import pymysql

app = Flask(__name__)
mysql=MySQL()

#Mysql configurations
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='shwetank'
app.config['MYSQL_DATABASE_DB']='yuanshop'
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_PORT']=3306
mysql.init_app(app)

@app.route('/')
def index():
    return render_template("index.html", title= 'Login')


@app.route('/login')
def login():
    return render_template('login.html', title="data")

@app.route('/checkAdmin', methods=['POST'])
def check():
    conn = mysql.connect()
    cursor = conn.cursor()


    username = str(request.form["name"])


    userpassword = str(request.form["password"])

    name = cursor.execute("SELECT username FROM usertable WHERE username = '"+username+"' AND permission = 'admin'")


    #print(username)
    if not name:

        return render_template("login.html")
    else:

        return render_template("cart.html")



if __name__ == '__main__':
    app.run(debug=True)
