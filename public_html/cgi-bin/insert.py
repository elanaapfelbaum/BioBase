#!/usr/bin/python3                                     
                                
import cgi
import mysql.connector
from html import beghtml, endhtml

form = cgi.FieldStorage()
insert_table = form.getvalue('insert_table')
values       = form.getvalue('values')


if values:   # make sure not empty to split
    values = values.split(',')

svalues = ""
if values:
    for value in values:
        # concatenate them into the appropriate syntax, removing any unnecessary whitespace
        svalues += "'" + value.strip() + "', "
    svalues = svalues[:-2]

cnx = mysql.connector.connect(user='eapfelba', host = 'localhost', database='eapfelba2', password='chumash1000')
query=""
cursor = cnx.cursor()

# inserting into a table
# need to also check if not the right form... right amount of attributes for that table
if insert_table and values:
    query = "insert into " + insert_table + " values (" + svalues + ")"

hasError = False
if not query:
    beghtml()
    print("<h3>You didn't fill anything out! :/</h3>")
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/insert.html">Back</a></b>')
    endhtml()
    hasError = True
    
if query:
    try:
        cursor.execute(query)
        cnx.commit()   
    except mysql.connector.Error as err:
        beghtml()
        print("Something went wrong: {}".format(err) + "<br><br>")
        print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/insert.html">Back</a></b>')
        endhtml()
        hasError = True
    
if hasError == False:
    # html with the response from the insert
    beghtml()
    print("<h3>Inserted " + svalues + " into " + insert_table + "!</h3>")
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/biobase.html">Try Something Else!</a></b><br><br>')
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/insert.html">Back</a></b>')
    endhtml()
    
cursor.close()
cnx.close()
