#!/usr/bin/python3                                     
                                
import cgi
import mysql.connector
from html import beghtml, endhtml

# getting the values from the html form
form = cgi.FieldStorage()
insert_table = form.getvalue('insert_table')
values       = form.getvalue('values')


if values:   # make sure not empty to split and then split on the comma
    values = values.split(', ')

svalues = ""
if values:
    for value in values:
        # concatenate them into the appropriate syntax, removing any unnecessary whitespace
        svalues += "'%s', " % value.strip()
    svalues = svalues[:-2]

# mysql connection
cnx = mysql.connector.connect(user='eapfelba', host = 'localhost', database='eapfelba2', password='chumash1000')
query=""  # intialized as empty to prevent errors
cursor = cnx.cursor()

# creating the query based on the user input
if insert_table and values:
    query = "insert into %s values (%s)" % (insert_table, svalues)

# checking for errors
hasError = False
if not query:  # empty form
    beghtml()
    print("<h3>You didn't fill anything out! :/</h3>")
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/insert.html">Back</a></b>')
    print('<br><b><a href = "http://ada.sterncs.net/~eapfelbaum/biobase.html">Home</a></b>')
    endhtml()
    hasError = True
    
if query:
    try: # try to execute the query, otherwise print out the issue on an html page and give the user options to go back
        cursor.execute(query)
        cnx.commit()   
    except mysql.connector.Error as err:
        beghtml()
        print("Something went wrong: {}".format(err) + "<br><br>")
        print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/insert.html">Back</a></b>')
        endhtml()
        hasError = True

# if there is no error, print out the results!
if hasError == False:
    beghtml()
    print("<h3>")
    temps = svalues.split(", ")
    for s in temps:
        print("<b> | " + s[1:-1])
    print(" | </b></h3>")
    print("<h3>is now in the table %s!</h3>" % insert_table)
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/cgi-bin/showdb.py">Current Database</a></b><br><br>')
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/biobase.html">Try Something Else!</a></b><br><br>')
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/insert.html">Back</a></b>')
    endhtml()
    
cursor.close()
cnx.close()
