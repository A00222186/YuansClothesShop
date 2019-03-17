from flask import Flask,render_template,request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

#Mysql configurations
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='admin'
app.config['MYSQL_DATABASE_DB']='yuanshop'
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config.setdefault('MYSQL_CHARSET','utf8')
app.config['MYSQL_USE_UNICODE']= True
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()


class product():

    def __init__(self,id,gender,age,producttype,productsize,price,stock):
        self.id = id
        self.gender = gender
        self.age = age
        self.producttype = producttype
        self.productsize = productsize
        self.price = price
        self.stock = stock

    def __repr__(self):
        return "%s" % self.producttype


def findID(id):
    id = request.values.get(id)
    return id


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/product/<id>')



def getPro(id):
    ID = findID(id)
    cursor.execute('''SELECT * from Product where productid like %s''' % id)
    productid = cursor.fetchone()
    cursor.execute('''SELECT name from Product where productid LIKE %s''' % id)
    name = cursor.fetchone()
    cursor.execute('''SELECT color from Product where productid LIKE %s''' % id)
    color = cursor.fetchone()
    cursor.execute('''SELECT overview from Product where productid LIKE %s''' % id)
    overview=cursor.fetchone()
    cursor.execute('''SELECT productsize from Product where productid LIKE %s''' % id)
    productsize = cursor.fetchone()
    cursor.execute('''SELECT price from Product where productid LIKE %s''' % id)
    price = cursor.fetchone()
    cursor.execute('''SELECT stock from Product where productid LIKE %s''' % id)
    stock = cursor.fetchone()
    cursor.execute('''SELECT description from Product where productid LIKE %s''' % id)
    description = cursor.fetchone()

    print productid
    print name
    print color
    print overview
    print productsize
    print price
    print stock
    print description
    return render_template('product-details.html', ID=ID, productid=productid,name=name,color=color,overview=overview,productsize=productsize,
                           price=price,stock=stock,description=description)



if __name__ == '__main__':
    app.run()
