# Overview

This project include ansible playbook that configure rsyslog to deliver auditd log to a collector server.
The playbook support both Redhat7 & Redhat 8


## How  to run it
1. Make sure you have server running installed with ansible 
2. Copy audit.yml file to master server under /TBD_location 
3. copy the host-audit file to /TBD_location
  A.Edit the file and include the ip address of the servers you wish to install the audit service
  B.save the file
4. copy the "audispd-plugins-3.0-0.17.20191104git1c2f876.el8.x86_64.rpm" /TBD_location ; this file is required only for RedHat 8 distribution
5. browse to /TBD_location
6. run ansible-playbook -i hosts-audit audit.yml --ask-pass --ask-become-pass
  A. On the first prompt enter the password of the remose server user that is required for the ssh connection 
  B. On the second prompt enter the remote server root user password 


## Update 
In the audit.yml playbook new rules can be added under "set auditd rules" block
