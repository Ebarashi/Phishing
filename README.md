# Phishing by DNS tunneling
We send an email to the victim to entice him to download the attachment.  
Once the victim downloads the file, the file runs on his computer and steals important information such as username, IP, passwords, etc.  
The information is sent back to us via DNS queries. 
## How to run the script
In the cmd on Linux os run the line: python3 phishing.py [username] [mail service name] [title] [Job] [personal [status] [have kids (yes/no)] [Email content (optional)]  
where if the answer for kids is "yes" you can write their ages & the email content can come in a configuration of a txt file/URL/string.  
Note: the email is sent to [username]+[mail service name].

for example, python3 phishing.py shani @gmail.com Ms. student single no
in this case the email will send to shani@gmail.com  

## Special modules we used
phishing.py:  
import validators -> to check the validation of url
import requests -> to read the url

attach_create.py:  
from email.message import EmailMessage -> template that is suitable for email  
import ssl -> to send secure email  
import smtplib  -> to send the mail  
from email.mime.application import MIMEApplication -> to add a file to the email  
from os.path import basename -> suffixes of the attached file 

# The attack
<img src = https://user-images.githubusercontent.com/92265738/204932664-e4af7f73-5b0f-499d-8221-7ec0dd33c977.png width="300" height="500">

## DNS traffic documentation in Wireshark
<img src = https://user-images.githubusercontent.com/92265738/204931996-71458311-813b-42b4-a43f-5d3c944980c7.png width="700" height="300">
