#!/usr/bin/python3                                                                           
import cgi
import mysql.connector

form = cgi.FieldStorage()
search_enzyme = form.getvalue('search_enzyme')
search_process1 = form.getvalue('search_process1')
search_process2 = form.getvalue('search_process2')


cnx = mysql.connector.connect(user='eapfelba', database='eapfelba2', host='localhost', password='chumash1000')
cursor = cnx.cursor()
query = "select * from enzyme"

# different options to select
if search_enzyme:
    query = ("select process_name from uses where enzyme_name = '" + search_enzyme + "'") 

if search_process1:
    query = ("select enzyme_name from uses where process_name = '" + search_process1 + "'")

if search_process2:
    query = ("select organelle from process, enzyme, location where process_name = '" + search_process2 + "'")

cursor.execute(query)
#cnx.commit()
response = cursor.fetchall()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Biochemical Processes</title>")
print("</head>")
print("<body>")
print("<center>")
print("<b>" + reponse + "</b>")
print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/project.html">Try Something Else!</a></b>')
print("</center>")
print("</body>")
print("</html>")

cursor.close()
cnx.close()
