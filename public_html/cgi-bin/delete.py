#!/usr/bin/python3

import cgi
import mysql.connector

form = cgi.FieldStorage()
enzyme_name = form.getvalue('enzyme_name')
process_name = form.getvalue('process_name')
enzyme_name2 = form.getvalue('enzyme_name2')
process_name2 = form.getvalue('process_name2')
enzyme_name3 = form.getvalue('enzyme_name3')

cnx = mysql.connector.connect(user='eapfelba', database='eapfelba2', host='localhost', password='chumash1000')
query = ""
cursor = cnx.cursor()

if enzyme_name:
    query = "delete from converts where enzyme_name = '" + enzyme_name.strip() + "'"

if enzyme_name3:
    query = "delete from enzyme where enzyme_name = '" + enzyme_name3.strip() + "'"
    
if process_name:
    query = "delete from process where process_name = '" + process_name.strip() + "'"

if process_name2 and enzyme_name2:
    query = "delete from uses where process_name = '" + process_name2.strip() + "' and enzyme_name = '" + enzyme_name2.strip() + "'"

hasError = False
try:
    cursor.execute(query)
    cnx.commit()
except mysql.connector.Error as err:
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
    print("Something went wrong: {}".format(err) + "<br><br>")
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/delete.html">Back</a></b>')
    print("</center>")
    print("</body>")
    print("</html>")
    hasError = True

if hasError == False:
    # html with the response from the delete 
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
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/biobase.html">Try Something Else!</a></b>')
    print("</center>")
    print("</body>")
    print("</html>")

cursor.close()
cnx.close()
