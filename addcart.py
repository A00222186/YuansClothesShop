from app import render_template
import traceback



def add_to_cart():

 from app import cursor,conn
 # cursor.execute("create view yuxin_view as select productid,name,price,color from product where productid='1'")
 cursor.execute("select * from yuanshop.yuxin_view where productid=1")
 results = cursor.fetchone()
 cursor.execute("select round(sum(price), 2) as total from yuxin_view;")
 total = cursor.fetchone()

 try:

        w2=results[1]
        w3=results[3]
        w4=results[2]
        print(w2)

        t1=total[0]
        conn.commit()
        # conn.close()
        return render_template('cart.html',w2=w2,w3=w3,w4=w4,t1=t1)
 except:

    traceback.print_exc()

    conn.rollback()
    # conn.close()
    return "failed"





def login():
    return render_template('login.html', title="data")

from app import mysql,request,cursor
def check():

    conn = mysql.connect()
    cursor = conn.cursor()
    print "ddd"

    username = str(request.form["name"])


    userpassword = str(request.form["password"])

    cursor.execute("SELECT * FROM usertable WHERE username ='"+username+"' and userpassword = '"+userpassword+"'")

    username= cursor.fetchone()
    id = username[0]
    name=username[1]
    password=username[2]
    age=username[3]
    gender=username[4]
    permission=username[5]
    status=username[6]

    print(id)
    print(name)
    print(password)
    print(age)
    print(gender)
    print(permission)
    print(status)



    #print(username)
    if not username:

        return render_template("index.html")
    elif username and permission == "admin":


        return render_template("adminpage.html")
    elif username and permission == "user":
        return render_template("index.html")
    elif username and permission == "manager":
        return render_template("adminpage.html")

    cursor.execute('call add_loginvisitor(%s,%s)', (username, userpassword))




