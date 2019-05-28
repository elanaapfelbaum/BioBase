#! /usr/bin/python3

import cgi
import mysql.connector
from html import beghtml, endhtml

cnx = mysql.connector.connect(user='eapfelba', host = 'localhost', database='eapfelba2', password='chumash1000')
cursor = cnx.cursor()   

# making tables from the results of the select statements
# this is to get the entire databse on one page of html
beghtml()
# link to home page
print('<b><a href = "http://ada.sterncs.net/~eapfelbaum/biobase.html">Back to Home</a></b><br><br>')

# processes
query = 'select * from process'
cursor.execute(query)

print("<table>")
print("<caption><b>Processes</b></caption>")
print("<tr>")
print("<th>Process</th>")
print("<th>Goal Product</th>")
print("</tr>")
for result in cursor:
    print("<tr>")
    print("<td>" + result[0] + "</td>")
    print("<td>" + result[1] + "</td>")
    print("</tr")
print("</table>")
print("<br>")


# enzymes
query = 'select * from enzyme'
cursor.execute(query)

print("<table>")
print("<caption><b>Enzymes</b></caption>")
print("<tr>")
print("<th>Enzyme</th>")
print("<th>Ligand Mechanism</th>")
print("</tr>")
for result in cursor:
    print("<tr>")
    print("<td>" + result[0] + "</td>")
    print("<td>" + result[1] + "</td>")
    print("</tr")
print("</table>")
print("<br>")


# compounds
query = 'select * from intermediate'
cursor.execute(query)

print("<table>")
print("<caption><b>Compounds</b></caption>")
print("<tr>")
print("<th>Compounds</th>")
print("<th>Ligand Mechanism</th>")
print("</tr>")
for result in cursor:
    print("<tr>")
    print("<td>" + result[0] + "</td>")
    print("<td>" + result[1] + "</td>")
    print("</tr")
print("</table>")
print("<br>")


# locations
query = 'select * from location'
cursor.execute(query)

print("<table>")
print("<caption><b>Locations</b></caption>")
print("<tr>")
print("<th>Organelle</th>")
print("<th>Substructure</th>")
print("</tr>")
for result in cursor:
    print("<tr>")
    print("<td>" + result[0] + "</td>")
    print("<td>" + result[1] + "</td>")
    print("</tr")
print("</table>")
print("<br>")

# conditions
query = 'select * from conds'
cursor.execute(query)

print("<table>")
print("<caption><b>Conditions</b></caption>")
print("<tr>")
print("<th>Concentration</th>")
print("<th>Compound</th>")
print("</tr>")
for result in cursor:
    print("<tr>")
    print("<td>" + result[0] + "</td>")
    print("<td>" + result[1] + "</td>")
    print("</tr")
print("</table>")
print("<br>")


# uses
query = 'select * from uses'
cursor.execute(query)

print("<table>")
print("<caption><b>Enzymes Used by Processes</b></caption>")
print("<tr>")
print("<th>Process</th>")
print("<th>Enzyme</th>")
print("</tr>")
for result in cursor:
    print("<tr>")
    print("<td>" + result[0] + "</td>")
    print("<td>" + result[1] + "</td>")
    print("</tr")
print("</table>")
print("<br>")

# operates_under
query = 'select * from operates_under'
cursor.execute(query)

print("<table>")
print("<caption><b>Conditions Under Which Processes Operate</b></caption>")
print("<tr>")
print("<th>Process</th>")
print("<th>Concentration</th>")
print("<th>Compound</th>")
print("</tr>")
for result in cursor:
    print("<tr>")
    print("<td>" + result[0] + "</td>")
    print("<td>" + result[1] + "</td>")
    print("<td>" + result[2] + "</td>")
    print("</tr")
print("</table>")
print("<br>")

# converts
query = 'select * from converts'
cursor.execute(query)

print("<table>")
print("<caption><b>Enzyme Reactions</b></caption>")
print("<tr>")
print("<th>Enzyme</th>")
print("<th>Reactant</th>")
print("<th>Product</th>")
print("<th>Energy Compounds</th>")
print("<th>Delta G</th>")
print("</tr>")
for result in cursor:
    print("<tr>")
    print("<td>" + result[0] + "</td>")
    print("<td>" + result[1] + "</td>")
    print("<td>" + result[2] + "</td>")
    print("<td>" + result[3] + "</td>")
    print("<td>" + result[4] + "</td>")
    print("</tr")
print("</table>")
print("<br>")

# located_in
query = 'select * from located_in'
cursor.execute(query)

print("<table>")
print("<caption><b>Locations of Enzymes</b></caption>")
print("<tr>")
print("<th>Enzyme</th>")
print("<th>Organelle</th>")
print("<th>Substructure</th>")
print("</tr>")
for result in cursor:
    print("<tr>")
    print("<td>" + result[0] + "</td>")
    print("<td>" + result[1] + "</td>")
    print("<td>" + result[2] + "</td>")
    print("</tr")
print("</table>")
print("<br>")

cursor.close()
cnx.close()
endhtml()
