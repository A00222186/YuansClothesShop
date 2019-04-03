# -*- coding: UTF-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib



def _format_addr(s):


    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = 'ianwu0326@163.com'
password = 'wuyuxin123'
to_addr = "ianwu0326@163.com"
smtp_server = 'smtp.163.com'





def send():

    from app import cursor
    cursor.execute('''SELECT productid,name,stock from Product where stock <50 ''')
    stock = cursor.fetchall()
    print stock

    if len(stock) > 0:
       while True:

         msg = MIMEText('we need order somthing,pls contact us!', 'plain','utf-8')
         msg['From'] = _format_addr('YuanClothShop <%s>' % from_addr)
         msg['Subject'] = Header('OrderList', 'utf-8').encode()

         with open("emails.txt","r") as f:
           emails = f.readlines()


         for to_addr in emails:
          msg['To'] = _format_addr('Supplier<%s>' % to_addr)
          server = smtplib.SMTP(smtp_server, 25)
          server.set_debuglevel(1)
          server.ehlo()
          server.starttls()
          server.login(from_addr, password)
          server.sendmail(from_addr, [to_addr], msg.as_string())
          server.quit()

         break

if __name__ == '__checkstock__':

   send()