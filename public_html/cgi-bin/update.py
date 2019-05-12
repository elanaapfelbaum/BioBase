#!/usr/bin/python3                                                                           
import cgi, cgitb
import mysql.connector

form = cgi.FieldStorage()
update_table = form.getvalue('update_table')
update_condition = form.getvalue('update_condition')

cnx = mysql.connector.connect(user='eapfelba', database='eapfelba1', password='chumash1000')
cursor = cnx.cursor()
 
if update_table and update_condition:
    query = ("update " + update_table + " where " + update_condition)

cursor.close()
cnx.close()

