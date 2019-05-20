#! /usr/bin/python3
import cgi
import mysql.connector

form = cgi.FieldStorage()
cnx = mysql.connector.connect(user='eapfelba', host = 'localhost', database='eapfelba2', password='chumash1\
000')
cursor = cnx.cursor()

query1 = "select * from enzyme"

cursor.execute(query)
cnx.commit()
data1 = cursor.fetchall()


print("Content-type:text/html\r\n\r\n")
print("<html>")
print(" <style>")
print("body {")
print("background-image: url(../biochem.png);")
print("background-attachment: fixed;")
print("background-size: cover;")
print("background-position: center;")
print("}>")
print("</style>")
print("<body>")
print("<center>")
print("<h1>~BioBase~</h1>")
print("<h2>Home of Biochemical Processes</h2>")
print("<h3>Enzyme</h3>")
print(data1)
print("</center>")
print("</body>")
print("</html>")

cursor.close()
cnx.close()
