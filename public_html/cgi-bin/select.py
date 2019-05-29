#!/usr/bin/python3                                                                           
import cgi
import mysql.connector
from html import beghtml, endhtml

# getting values from the form
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

# establishing sql connection
cnx = mysql.connector.connect(user='eapfelba', database='eapfelba2', host='localhost', password='chumash1000')
cursor = cnx.cursor()
query = ""
key = ""

# different options to select- assign query based on input
# the last text box to be filled in on the form will be executed
# the title helps with printing the result to the html
if search_enzyme:
    query = "select process_name from uses where enzyme_name = %s"
    title = "Processes"
    v = (search_enzyme,)
    
if search_process1:
    query = "select enzyme_name from uses where process_name = %s"
    title = "Enzymes"
    v = (search_process1,)
    
if search_process2:
    query = "select distinct organelle from uses natural join located_in where process_name = %s"
    title = "Organelles"
    v = (search_process2,)
    
if search_enzyme2:
    query = "select ligand_mechanism from enzyme where enzyme_name = %s"
    title = "Ligand Mechanisms"
    v = (search_enzyme2,)
    
if search_process3:
    query = "select goal_product from process where process_name = %s"
    title = "Goal Products"
    v = (search_process3,) 
    
if sub:
    query = "select organelle from location where substructure = %s"
    title = "Organelles"
    v = (sub,)
    
if inter:
    query = "select concentration from conds where compound = %s"
    title = "Concentrations"
    v = (inter,)

# keep track of an extra variable so that it will know to print an extra line of results (onyl query with a tuple result)
if search_process5: 
    query = "select concentration, compound from operates_under where process_name = %s"
    title = "Conditions"
    key = 'one'
    v = (search_process5,)
    
if search_enzyme3 and reac:
    query = "select product_name from converts where enzyme_name = %s and reactant_name = %s"
    title = "Products"
    v = (search_enzyme3, reac)
    
if search_enzyme4:
    query = "select organelle from located_in where enzyme_name = %s" 
    title = "Organelles"
    v = (search_enzyme4,)
    
if inter2:
    query = "select concenration from intermediate where intermediate_name = %s"
    title = "Concentrations"
    v = (inter2,)

# avoid error with empty form- give the user option to fill in information or go back to home page
if not query:
    beghtml()
    print("<h3>You didn't fill anything out! :/</h3>")
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/select.html">Back</a></b>')
    print('<br><b><a href = "http://ada.sterncs.net/~eapfelbaum/biobase.html">Home</a></b>')
    endhtml()
    
# catching errors- blank form, wrong syntax, etc
# try executing query and spit back error to the screen if there is a problem
hasError = False
if query:
    try:
        cursor.execute(query, v)        
    except mysql.connector.Error as err:
        print("<b>Something went wrong:</b> {}".format(err) + "<br><br>")
        print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/select.html">Back</a></b>')
        endhtml()
        hasError = True

# otherwise, print out the response with links back and to home
if hasError == False:
    response = cursor.fetchall()
    beghtml()
    if not response:                                                                                     
        print("<h3>no results found</h3>")
    else:
        print("<h3>Results!</h3>")
        print("<h3>%s</h3>" % title) 
        for r in response:
            print("<b> %s" % r[0])
            if key:  # if there was a second value of the data like (concentration, compound)
                print("%s</br>" % r[1])
            print("<br>")
    print("</b><br>")
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/biobase.html">Try Something Else!</a></b><br><br>')
    print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/select.html">Back</a></b><br><br>')
    endhtml()

cursor.close()
cnx.close()
