edit   httpd.conf file
==============
uncomment 
AddHandler cgi-script .cgi
<Directory />
    #Options FollowSymLinks ExecCGI Indexes
    #AllowOverride None
    #Order deny,allow
    #Deny from all
    #Satisfy all
	Options +ExecCGI
	AddHandler cgi-script .cgi .py
	Order allow,deny
	Allow from all
</Directory>

001) Introduction to CGI
002) using get/post  method




