import mysql.connector
import json
from mysql.connector import Error
from flask import render_template, Flask

app = Flask(__name__)

name2 = "shirt"
price2 = 99.99
color2 = "blue"



def register():
    try:
        mySQLconnection = mysql.connector.connect(host='localhost',
                                                  database='yuanshop',
                                                  user='root',
                                                  password='sarahaini')
        sql_select_Query = "select * from test_view"
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
        data = cursor.fetchall()
        print(data)
        print("Total number of rows is - ", cursor.rowcount)

        return data

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        if (mySQLconnection.is_connected()):
            mySQLconnection.close()
            print("MySQL connection is closed")


def PlaceOrder():
    try:
        mySQLconnection = mysql.connector.connect(host='localhost',
                                                  database='yuanshop',
                                                  user='root',
                                                  password='sarahaini')
        sql_insert_Query = "insert into soldproducts (select * from test_view)"
        cursor = mySQLconnection.cursor()
        print("Adding order to Products SOLD!!!")
        cursor.execute(sql_insert_Query)

        drop_view_query = "DROP VIEW test_view"
        cursor.execute(drop_view_query)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        if (mySQLconnection.is_connected()):
            mySQLconnection.close()
            print("MySQL connection is closed")

if __name__ == '__main__':
    app.run()
