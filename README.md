# Phishing by DNS tunneling
We send an email to the victim to entice him to download the attachment.  
Once the victim downloads the file, the file runs on his computer and steals important information such as username, IP, passwords, etc.  
The information is sent back to us via DNS queries. 
## How to run the script
In the cmd on Linux os run the line: python3 fake_mail.py [username] [mail service name] [title] [Job] [personal [status] [have kids (yes/no)] [Email content (optional)]  
where if the answer for kids is "yes" you can write their ages & the email content can come in a configuration of a txt file/URL/string.  
Note: the email is sent to [username]+[mail service name].

for example, python3 fake_mail.py shani @gmail.com Ms. student single no email.txt
in this case the email will send to shani@gmail.com  
