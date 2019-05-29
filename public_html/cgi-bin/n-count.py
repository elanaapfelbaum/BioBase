#!/usr/bin/python                                                                                                                                                     

# Import modules for CGI handling                                                                                                                                     
import cgi, cgitb

# Create instance of FieldStorage                                                                                                                                     
form = cgi.FieldStorage()

# Get data from fields                                                                                                                                                
n_count = form.getvalue('n_count')

# Print out the HTML page                                                                                                                                             
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Star Counter</title>"
print "</head>"
print "<body>"

# if n_count is set (e.g. if this is a response to the form), print                                                                                                   
# out the right number of stars.  n_count is a string, handle that                                                                                                    
# appropriately.  We could do better here, if n_count is filled in but                                                                                                
# not an integer, this will get an error.                                                                                                                             

if n_count:
    print "Displaying " + n_count + " stars: "
    for i in range(int(n_count)):
        print "*",
    print "<br />"

# Display the form to the user.  If a value is filled in, include it                                                                                                  
# in the form.                                                                                                                                                        

print "<form action='n-count.py' method='get'>"
print "Enter Star Count: "

print "<input type='text' name='n_count'",
if n_count:
    print " value='" + n_count + "'",
print "/> <br />"

print "<input type='submit' value='Submit' />"
print "</form>"
print "</body>"
print "</html>"
