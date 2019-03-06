from flask import Flask, render_template
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()

#Mysql configurations
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='admin'
app.config['MYSQL_DATABASE_DB']='yuanshop'
app.config['MYSQL_DATABASE_HOST']='localhost'
mysql.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def user_route(username):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * from USERTABLE")
    data = cursor.fetchone()
    return render_template('index.html',username=username);

if __name__ == '__main__':
    app.run()
