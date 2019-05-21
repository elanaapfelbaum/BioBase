#! /usr/bin/python3

import cgi
import mysql.connector
from html import beghtml, endhtml

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
query = ""
query2 = ""


if enzyme_name and product_name:
    query = "update converts set product_name = '" + product_name.strip() + "' where enzyme_name = '" + enzyme_name.strip() + "'"
    query2 = "select * from converts where product_name = '" + product_name.strip() + "' and enzyme_name = '" + enzyme_name.strip() + "'"
    
if enzyme_name2 and mechanism_name:
    query = "update enzyme set ligand_mechanism = '" + mechanism_name.strip() + "' where enzyme_name = '" + enzyme_name2.strip() + "'"
    query2 = "select * from enzyme where enzyme_name = '" + enzyme_name2.strip() + "'"
    
if process_name and concentration and compound_name:
    query = "update operates_under set concentration = '" + concentration.strip() + "', compound = '" + compound_name.strip() + "' where process_name = '" + process_name.strip() + "'"
    query2 = "select * from operates_under where process_name = '" + process_name.strip() + "'"

# process
# intermediate
# uses
# located_in
# operates_under
# conds


hasError = False
if not query:
    beghtml()
    print("<h3>You didn't fill anything out! :/</h3>")
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/update.html">Back</a></b>')
    endhtml()
    hasError = True

if query:
    try:
        cursor.execute(query)
        cnx.commit()
    
    except mysql.connector.Error as err:
        beghtml()
        print("Something went wrong: {}".format(err) + "<br><br>")
        print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/update.html">Back</a></b>')
        endhtml()
        hasError = True

if hasError == False:
    cursor.execute(query2)
    data = cursor.fetchall()
    
    # html with the response from the update           
    beghtml()
    print("<h3>Updated!</h3>")
    print("The database now reads", data)
    print("<br><br>")
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/biobase.html">Try Something Else!</a></b><br><br>')
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/update.html">Back</a></b>')
    endhtml()


cursor.close()
cnx.close()
