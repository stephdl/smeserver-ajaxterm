For the most actual version please see 

http://wiki.contribs.org/Ajaxterm

Usage: https://yourdomain.com/ajaxterm/index.html

Configuration
1) To allow only local login on localhost:
config setprop Ajaxterm allowOnlyLocalhost yes
service ajaxterm restart

2) To allow ssh login on all hosts:
config setprop Ajaxterm allowOnlyLocalhost no
service ajaxterm restart

3) Terminal size (default is 80 x 25)
config setprop Ajaxterm width NEWWIDTH
config setprop Ajaxterm height NEWHEIGHT
service ajaxterm restart

4) Basic Auth Users (Browser login)
config setprop Ajaxterm basicAuthUsers "user [user] ..."
expand-template /etc/httpd/conf/httpd.conf
service httpd-e-smith restart

5) Web alias (default: ajaxterm)
config setprop Ajaxterm webAlias NEWALIAS
expand-template /etc/httpd/conf/httpd.conf
service httpd-e-smith restart

6) Changing the ajaxterm service port (default is 8022):
config setprop Ajaxterm servicePort NEWPORT
expand-template /etc/httpd/conf/httpd.conf
service httpd-e-smith restart
service ajaxterm restart

