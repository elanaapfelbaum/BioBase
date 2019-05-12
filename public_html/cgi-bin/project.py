#!/usr/bin/python3                                                                                                  
import cgi, cgitb
import mysql.connector

form = cgi.FieldStorage()
insert_table = form.getvalue('insert_table')
values = form.getvalue('values')

delete_table = form.getvalue('delete_table')
delete_condition = form.getvalue('delete_condition')

update_table = form.getvalue('update_table')
update_condition = form.getvalue('update_condition')

select_table = form.getvalue('select_table')
select_condition = form.getvalue('select_condition')
# select ____?

cnx = mysql.connector.connect(user='eapfelba', database='eapfelba1', password='chumash1000')
cursor = cnx.cursor()

# inserting into a table
# need to also check if not the right form... right amount of attributes for that table
if insert_table and values:
    query = ("insert into " + insert_table + " values (" + values + ")")

# delete from a table
if delete_table and delete_condition:
    query = ("delete from " + delte_table + " where " + delete_condition)

if update_table and update_condition:
    query = ("update " + update_table + " where " + update_condition)

if select_table and select_condition:
    query = ("select " + blank + " from " + select_table + " where " + select_condition)


cursor.execute(query)
response = data.fetchall()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Biochemical Processes</title>")
print("</head>")
print("<body>")
print("<center>")
print("<b>" + data + "</b>")
print("</center>")
print("</body>")
print("</html>")


cursor.close()
cnx.close()
