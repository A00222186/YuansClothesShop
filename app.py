from flask import Flask,render_template,request
import traceback
from flaskext.mysql import MySQL
from checkstock import send
import json



def outosend():
    print "sending"
    send()
    print "send"
#     global t    #Notice: use global variable!
#     t = threading.Timer(10.0, outosend)
#     t.start()

# while 1:
#     if time.localtime()[3] == 6:
#         t.start()
#         break

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
    outosend()
    return render_template('index.html')


@app.route('/Websitetraffic/update', methods=['GET', 'POST'])
def __visitorupdate__():
    conn = mysql.connect()
    cursor = conn.cursor()
    print("this is main update visitor")
    cursor.execute("call update_visitor()")
    conn.commit()
    conn.close()
    print("update success")

    return render_template('index.html')


@app.route('/visitor.html')
def __getvisitor__():
    return render_template('visitor.html')


@app.route('/Websitetraffic/read', methods=['GET'])
def __visitorweek__():
    # i = datetime.datetime.now()
    print("this is the main about read one week data")
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute('call get_week()')
    result = cur.fetchall()
    conn.close()
    jsonData = []

    for row in result:
        datajson = {}
        datajson['visitor'] = row[0]
        datajson['day'] = row[1]
        datajson['month'] = row[2]
        datajson['year'] = row[3]
        jsonData.append(datajson)

    return json.dumps(jsonData)

@app.route('/checkout.html')
def checkout():
    from checkout import register
    data = register()
    return render_template('checkout.html', data=data)


@app.route('/product/<id>')
def getPro(id):
    ID = findID(id)
    cursor.execute('''SELECT * from Product where productid like %s''' % id)
    productid = cursor.fetchone()
    id=productid[0]
    name=productid[1]
    color=productid[2]
    overview=productid[3]
    size=productid[4]
    price=productid[5]
    stock=productid[6]
    description=productid[7]


    print (id)
    print (name)
    print (color)
    print (overview)
    print (size)
    print (price)
    print (stock)
    print (description)

    return render_template('product-details.html', ID=ID, productid=productid,id=id,name=name,color=color,overview=overview,size=size,price=
                           price,stock=stock,description=description)

@app.route('/registuser')
def register():
    from addcart import check
    check()
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

@app.route("/cart/add", methods=['POST'])
def add_to_cart():
    from addcart import add_to_cart
    add_to_cart()
    return add_to_cart()


@app.route('/login.html')
def login():

    from addcart import login
    login()

    return login()


@app.route('/checkUser', methods=['POST'])
def check():
    from addcart import check
    check()

    return check()

# @app.route('/adminindex.html')
# def adminpage():
#     # from addcart import check
#     # check()
#     return render_template('adminindex.html')

if __name__ == '__main__':
    app.run()
