import json

def __malevisitorLogin__():

    from app import mysql
    print("this is the main about get male login user data")
    conn = mysql.connect()
    cur = conn.cursor()

    # cur.execute("create view LoginVisDetails AS Select USERTABLE.userid,USERTABLE.username,USERTABLE.gender,TIMESTAMPDIFF(YEAR, USERTABLE.birthday, CURDATE()) as age from USERTABLE,loginvisitor where USERTABLE.userid=loginvisitor.UserId and loginvisitor.visitordate=date_sub(curdate(),interval 1 day)")
    # cur.execute("create view LoginVisDetailsMale AS Select USERTABLE.userid,USERTABLE.username,USERTABLE.gender,TIMESTAMPDIFF(YEAR, USERTABLE.birthday, CURDATE()) as age from USERTABLE,loginvisitor where USERTABLE.userid=loginvisitor.UserId and	USERTABLE.gender='male' and loginvisitor.visitordate=date_sub(curdate(),interval 1 day)")
    # cur.execute("create view LoginVisDetailsFeMale AS Select USERTABLE.userid,USERTABLE.username,USERTABLE.gender,TIMESTAMPDIFF(YEAR, USERTABLE.birthday, CURDATE()) as age from USERTABLE,loginvisitor where USERTABLE.userid=loginvisitor.UserId and	USERTABLE.gender='female' and loginvisitor.visitordate=date_sub(curdate(),interval 1 day)")
    cur.execute("select * from LoginVisDetailsMale")
    result = cur.fetchall()
    conn.close()
    jsonData = []
    count1 = 0
    count2 = 0
    count3 = 0
    for row in result:
        if row[3] < 20:
            count1 += 1
        if (row[3] <= 25 and row[3] >= 20):
            count2 += 1
        if (row[3] > 25):
            count3 += 1

    data1 = {}
    data2 = {}
    data3 = {}

    data1['name'] = 'less20'
    data1['num'] = count1
    data2['name'] = 'great20less25'
    data2['num'] = count2
    data3['name'] = 'great25'
    data3['num'] = count3
    jsonData.append(data1)
    jsonData.append(data2)
    jsonData.append(data3)

    return json.dumps(jsonData)


def __femalevisitorLogin__():
    from app import mysql
    print("this is the main about get female login user data")
    conn = mysql.connect()
    cur = conn.cursor()
    cur.execute("select * from LoginVisDetailsFeMale")
    result = cur.fetchall()
    conn.close()
    jsonData = []
    count1 = 0
    count2 = 0
    count3 = 0
    for row in result:
        if row[3] < 20:
            count1 +=1
        if (row[3]<=25 and row[3]>=20):
            count2 += 1
        if (row[3]>25):
            count3 +=1

    data1 = {}
    data2 = {}
    data3 = {}

    data1['name'] = 'less20'
    data1['num'] = count1
    data2['name'] = 'great20less25'
    data2['num'] = count2
    data3['name'] = 'great25'
    data3['num'] = count3
    jsonData.append(data1)
    jsonData.append(data2)
    jsonData.append(data3)

    return json.dumps(jsonData)