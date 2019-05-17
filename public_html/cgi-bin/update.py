#! /usr/bin/python3

import cgi
import mysql.connector

form = cgi.FieldStorage()
enzyme_name    = form.getvalue('enzyme_name')
product_name   = form.getvalue('product_name')
enzyme_name2   = form.getvalue('enzyme_name2')
mechanism_name = form.getvalue('mechanism_name')
process_name   = form.getvalue('process_name')
concentration  = form.getvalue('concentration')
compound_name  = form.getvalue('compound_name')


cnx = mysql.connector.connect(user='eapfelba', database='eapfelba2', host='localhost', password='chumash1000')
cursor = cnx.cursor(buffered=True)

if enzyme_name and product_name:
    query = "update converts set product_name = '" + product_name.strip() + "' where enzyme_name = '" + enzyme_name.strip() + "'"

if enzyme_name2 and mechanism_name:
    query = "update enzyme set ligand_mechanism = '" + mechanism_name.strip() + "' where enzyme_name = '" + enzyme_name2.strip() + "'"

if process_name and concentration and compound_name:
    query = "update operates_under set concentration = '" + concentration.strip() + "', compound = '" + compound_name.strip() + "' where process_name = '" + process_name.strip() + "'"
    
cursor.execute(query)
cnx.commit()

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
print("<h3>Updated!</h3>")
print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/biobase.html">Try Something Else!</a></b>')
print("</center>")
print("</body>")
print("</html>")

cursor.close()
cnx.close()
