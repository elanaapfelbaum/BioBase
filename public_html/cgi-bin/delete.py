#!/usr/bin/python3

import cgi
import mysql.connector
from html import beghtml, endhtml

form = cgi.FieldStorage()
enzyme_name   = form.getvalue('enzyme_name')
process_name  = form.getvalue('process_name')
enzyme_name2  = form.getvalue('enzyme_name2')
process_name2 = form.getvalue('process_name2')
enzyme_name3  = form.getvalue('enzyme_name3')
conc          = form.getvalue("conc")
compound      = form.getvalue("compound")
intermediate  = form.getvalue("inter")
sub           = form.getvalue("sub")
organelle     = form.getvalue("organelle")
enzyme_name3  = form.getvalue("enzyme_name3")
process_name3 = form.getvalue("process_name3")
organelle2    = form.getvalue("organelle2")
conc2         = form.getvalue("conc2")
compound2     = form.getvalue("compound2")


cnx = mysql.connector.connect(user='eapfelba', database='eapfelba2', host='localhost', password='chumash1000')
query = ""
cursor = cnx.cursor()

if enzyme_name:
    query = "delete from converts where enzyme_name = '%s'" % enzyme_name

if enzyme_name3:
    query = "delete from enzyme where enzyme_name = '%s'" % enzyme_name3
    
if process_name:
    query = "delete from process where process_name = '%s'" % process_name

if process_name2 and enzyme_name2:
    query = "delete from uses where process_name = '%s' and enzyme_name = '%s'" % (process_name2, enzyme_name2)

if conc and compound:
    query = "delete from conds where concentration = '%s' and compound = '%s'" % (conc, compound)

if intermediate:
    query = "delete from intermediate where intermediate_name = '%s'" % intermediate

if organelle and sub:
    query = "delete from location where organelle = '%s' and substructure = '%s'" % (organelle, sub)

if enzyme_name3 and organelle2:
    query = "delete from located_in where enzyme_name = '%s' and organelle = '%s'" % (enzyme_name3, organelle2)

if process_name3 and conc2 and compound2:
    query = "delete from operates_uner where process_name = '%s' and concentration = '%s' and compound = '%s'" % (process_name3, conc2, compound2)


hasError = False
if not query:
    beghtml()
    print("<h3>You didn't fill anything out! :/</h3>")
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/delete.html">Back</a></b>')
    endhtml()
    hasError = True
    
try:
    cursor.execute(query)
    cnx.commit()
    
except mysql.connector.Error as err:
    beghtml()
    print("Something went wrong: {}".format(err) + "<br><br>")
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/delete.html">Back</a></b>')
    endhtm()
    hasError = True

if hasError == False:
    # html with the response from the delete 
    beghtml()
    print("<h3>Deleted!</h3>")                                      
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/biobase.html">Try Something Else!</a></b><br><br>')
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/delete.html">Back</a></b>')
    endhtml()
    
cursor.close()
cnx.close()
