
# pip install mysql.connector.python
# pip install pywhatkit
import os
import datetime
import mysql.connector
# import pywhatkit

now = str(datetime.date.today())
if now[8] == "0" :
    today = now[9:10] + "-" + now[5:7]
else :
    today = now[8:10] + "-" + now[5:7]
# today = now[8:10] + "-" + now[5:7]
print(today)

con = mysql.connector.connect(host="localhost", user="root", password="", database="autowisher")
cur = con.cursor()
cur.execute(f"select * from data where Birthday = {today}")
list1 = cur.fetchall()

for i in list1 :
    print(i)

for i in list1 :
    os.system("start https://web.whatsapp.com/send?phone=+91{i[2]}^&text=Happy%20Birthday%20to%20you%20{i[0]}")

# for i in list1 :
#     pywhatkit.sendwhatmsg("+91{i[2]}", "Happy Birthday to you {i[0]}", 19, 32)
