#!/usr/bin/python3                                                                           

import cgi
import mysql.connector

#form = cgi.FieldStorage()
#enzyme_name = form.getvalue('enzyme_name')
#product_name = form.getvalue('product_name')
#enzyme_name2 = form.getvalue('enzyme_name2')
#mechanism_name = form.getvalue('mechanism_name')
#process_name = form.getvalue('process_name')
#concentration = form.getvalue('concentration')
#compound_name = form.getvalue('compound_name')

cnx = mysql.connector.connect(user='eapfelba', database='eapfelba1', host='localhost', password='chumash1000')
query = ""
cursor = cnx.cursor()
query = "select * from enzyme"

#if enzyme_name and product_name:
#    query = ('update converts set product_name = "' + product_name + '" where enzyme_name = "' + enzyme_name + '"')

#if enzyme_name2 and mechanism_name:
#    query = ('update enzyme set mechanism = "' + mechanism_name + '" where enzyme_name = "' + enzyme_name2 + '"')

#if process_name and concentration and compound_name:
#    query = ('update operates_under set concentration = "' + concentration + '" and compound_name = "' + compound_name + '" where process_name = "' + process_name + '"')


cursor.execute(query)
data = cursor.fetchall()

# html with the response from the update                   
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
print("<h3>Deleted!</h3>")
#print(query)
print(data)
#print("<h3>with "  + " error<h3>") 
print("</center>")
print("</body>")
print("</html>")

cursor.close()
cnx.close()

