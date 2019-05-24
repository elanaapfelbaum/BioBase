#!/usr/bin/python3                                                                           
import cgi
import mysql.connector
from html import beghtml, endhtml


form = cgi.FieldStorage()
search_enzyme   = form.getvalue('search_enzyme')
search_process1 = form.getvalue('search_process1')
search_process2 = form.getvalue('search_process2')
search_enzyme2  = form.getvalue("search_enzyme2")
search_process3 = form.getvalue("search_process3")
sub             = form.getvalue("sub")
inter           = form.getvalue("inter")
search_process5 = form.getvalue("search_process5")
search_enzyme3  = form.getvalue("search_enzyme3")
reac            = form.getvalue("reac")
search_enzyme4  = form.getvalue("search_enzyme4")
inter2          = form.getvalue("inter2")

cnx = mysql.connector.connect(user='eapfelba', database='eapfelba2', host='localhost', password='chumash1000')
cursor = cnx.cursor()
query = ""
key = ""

# different options to select
if search_enzyme:
    query = "select process_name from uses where enzyme_name = '%s'"  % search_enzyme
    title = "Processes"
    
if search_process1:
    query = "select enzyme_name from uses where process_name = '%s'" % search_process1
    title = "Enzymes"
    
if search_process2:
    query = "select distinct organelle from uses, located_in where process_name = '%s'" % search_process2
    title = "Organelles"
    
if search_enzyme2:
    query = "select ligand_mechanism from enzyme where enzyme_name = '%s'" % search_enzyme2
    title = "Ligand Mechanisms"
    
if search_process3:
    query = "select goal_product from process where process_name = '%s'" % search_process3
    title = "Goal Products"
    
if sub:
    query = "select organelle from location where substructure = '%s'" % sub
    title = "Organelles"
    
if inter:
    query = "select concentration from conds where compound = '%s'" % inter
    title = "Concentrations"
    
if search_process5:
    query = "select concentration, compound from operates_under where process_name = '%s'" % search_process5
    title = "Conditions"
    key = 'one'
    
if search_enzyme3 and reac:
    query = "select product_name from converts where enzyme_name = '%s' and reactant_name = '%s'" % (search_enzyme3, reac)
    title = "Products"
    
if search_enzyme4:
    query = "select organelle from located_in where enzyme_name = '%s'" % search_enzyme4
    title = "Organelles"
    
if inter2:
    query = "select concenration from intermediate where intermediate_name = '%s'" % inter2
    title = "Concentrations"
    
if not query:
    beghtml()
    print("<h3>You didn't fill anything out! :/</h3>")
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/select.html">Back</a></b>')
    print('<br><b><a href = "http://ada.sterncs.net/~eapfelbaum/biobase.html">Home</a></b>')
    endhtml()
    
# catching errors
hasError = False

if query:
    try:
        cursor.execute(query)        
    except mysql.connector.Error as err:
        print("<b>Something went wrong:</b> {}".format(err) + "<br><br>")
        print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/select.html">Back</a></b>')
        endhtml()
        hasError = True

if hasError == False:
    response = cursor.fetchall()
    beghtml()
    if not response:                                                                                     
        print("<h3>no results found</h3>")
    else:
        print("<h3>Results!</h3>")
        print("<h3>" + title + "</h3>") 
        for r in response:
            print("<b>" + r[0])
            if key:
                print(r[1] + "</br>")
            print("<br>")
    print("</b><br>")
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/biobase.html">Try Something Else!</a></b><br><br>')
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/select.html">Back</a></b><br><br>')
    endhtml()

cursor.close()
cnx.close()
