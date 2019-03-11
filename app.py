from flask import Flask,render_template
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql=MySQL()

#Mysql configurations
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='admin'
app.config['MYSQL_DATABASE_DB']='test'
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_PORT']=3307
mysql.init_app(app)

@app.route('/')
def hello_world():
   return 'Hello World!'

@app.route('/user/<name>')
def user_route(name):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * from UserName")
    data=cursor.fetchone()
    print (data)
    #return "data"
    return render_template('index.html',name=name);

if __name__ == '__main__':
    app.run()
