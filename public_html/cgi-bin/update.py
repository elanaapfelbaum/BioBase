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
process_name2  = form.getvalue('process_name2')
goal           = form.getvalue('goal')
inter          = form.getvalue('inter')
conc           = form.getvalue('conc')
process_name3  = form.getvalue('process_name3')
enzyme_name3   = form.getvalue('enzyme_name3')
enzyme_name4   = form.getvalue('enzyme_name4')
organelle      = form.getvalue('organelle')
sub            = form.getvalue('sub')
organelle2     = form.getvalue('organelle2')
sub2           = form.getvalue('sub2')
conc2          = form.getvalue('conc2')
comp           = form.getvalue('comp')
loc            = form.getvalue('loc')
sub3           = form.getvalue('sub3')
sub4           = form.getvalue('sub4')

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

if process_name2 and goal:
    query = "update process set goal_product = '" + goal + "' where process_name = '" + process_name2 + "'"
    query2 = "select * from process where process_name = '" + process_name2 + "'"

if inter and conc:
    query = "update intermediate set concenration = '" + conc + "' where intermediate_name = '" + inter + "'"
    query2 = "select * from intermediate where intermediate_name = '" + inter + "'"

if process_name3 and enzyme_name3:
    query = "update uses set enzyme_name = '" + enzyme_name3 + "' where process_name = '" + process_name3 + "'"
    query2 = "select * from uses where process_name = '" + process_name3 + "' and enzyme_name = '" + enzyme_name3 + "'"

if enzyme_name4 and organelle and sub and sub4:
    query = "update located_in set organelle = '" + organelle + "' and substructure = '" + sub + "' where enzyme_name = '" + enzyme_name4 + "' and substructure = '" + sub4 + "'"
    query2 = "select * from located_in where enzyme_name = '" + enzyme_name4 + "'"
    
if organelle2 and sub2:
    query = "update location set substructure = '" + sub2 + "' where organelle = '" + organelle2 + "' and substructure = '" + sub3 + "'"
    query2 = "select * from location where organelle = '" + organelle2 + "' and substructure = '" + sub2 + "'"

if conc2 and comp and loc:
    query = "update conds set prime_location = '" + loc + "' where concentration = '" + conc2 + "' and compound = '" + comp + "'"
    query2 = "select * from conds where concentration = '" + conc2 +"' and compound = '" + comp + "' and prime_location = '" + loc + "'"


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
