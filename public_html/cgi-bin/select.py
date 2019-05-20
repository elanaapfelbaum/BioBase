#!/usr/bin/python3                                                                           
import cgi
import mysql.connector

form = cgi.FieldStorage()
search_enzyme = form.getvalue('search_enzyme')
search_process1 = form.getvalue('search_process1')
search_process2 = form.getvalue('search_process2')


cnx = mysql.connector.connect(user='eapfelba', database='eapfelba2', host='localhost', password='chumash1000')
cursor = cnx.cursor()

# different options to select
if search_enzyme:
    query = ("select process_name from uses where enzyme_name = '" + search_enzyme + "'") 

if search_process1:
    query = ("select enzyme_name from uses where process_name = '" + search_process1 + "'")

if search_process2:
    query = ("select distinct organelle from uses, located_in where process_name = '" + search_process2 + "'")

    
# catching errors
hasError = False
try:
    cursor.execute(query)

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
    print("<b>Something went wrong:</b> {}".format(err) + "<br><br>")
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/select.html">Back</a></b>')
    print("</center>")
    print("</body>")
    print("</html>")
    hasError = True

if hasError == False:
    response = cursor.fetchall()
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
    if not response:                                                                                                                         
        print("<h3>no results found</h3>")
    else:
        print("<h3>Results!</h3>")
        for result in response:
            print("<b>" + result[0] + "</b><br>")
    print("<br>")
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/biobase.html">Try Something Else!</a></b><br><br>')
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/select.html">Back</a></b><br><br>')
    print("</center>")
    print("</body>")
    print("</html>")

cursor.close()
cnx.close()
