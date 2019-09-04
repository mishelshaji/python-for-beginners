#!c:/Python34/python
# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
# get/post method 
form = cgi.FieldStorage() 

# Get data from fields
name = form.getvalue('txt_Name')

print ("Content-type: text/html\n\n")
print ("<html><head>")
print ("</head><body>")

print ("<h1>Hello %s </h1>" % name)
print ("</body></html>")