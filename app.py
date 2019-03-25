
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
app.config['MYSQL_DATABASE_PORT']=3307
mysql.init_app(app)

@app.route('/loginsuccess')
def index():
    if 'username' is session:
        username_session = escape(session['username']).capitalise()
        return render_template('cart.html',session_user_name=username_session)
    return redirect(url_for('login.html'))

@app.route('/user/<name>')
def user_route(name):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * from User")
    data=cursor.fetchone()
    return render_template('index.html',name=name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")
    conn = mysql.connect()
    error = None
    if 'username' in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        username_form = request.form['name']
        password_form = request.form['password']
        conn.execute("SELECT COUNT(1) FROM user WHERE username = %s;", [username_form])
        if conn.fetchall():
            conn.execute("SELECT password FROM user WHERE username = %s;", [username_form])
            if password_form == row[0]:
                session['username'] = request.form["username"]
                return redirect(url_for('index'))
            raise SyntaxError('invalid Password')
    else:
       error = "Invalid Credential"
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run()
