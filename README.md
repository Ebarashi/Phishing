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





## DNS Tunneling

The attack - 

**1 ->** Get the password file, current username, IP, available languages, OS version.

**2 ->** Send data through DNS queries to a local server.

Implementation :

**1 ->** write the data to a txt file we We extracted the information from the shadaw file and the rest of the information using the cmd commands.

**2 ->** we use nslookup to generate DNS queries and send to the DNS server. 
         Nslookup (stands for “Name Server Lookup”) is a useful command for getting information from the DNS server. It is a network administration tool for querying            the Domain Name System (DNS) to obtain domain name or IP address mapping or any other specific DNS record.
     
 ![1](https://user-images.githubusercontent.com/86716307/205024668-3b3ed7fc-c5b5-4299-b10f-be71f4c923f9.jpg)
 
The attacker acquires a domain, for example, evilsite.com.
The attacker configures the domain’s name servers to his own DNS server.
The attacker delegates a subdomain, such as “tun.evilsite.com” and configures his machine as the subdomain’s authoritative DNS server.
Any DNS request made by the victim to “{data}.tun.evilsite.com” will end up reaching the attacker’s machine.
The attacker’s machine encodes a response that will get routed back to the victim’s machine.
A bidirectional data transfer channel is achieved using a DNS tunneling tool.

In this task we havn't acquire a domain and a DNS server but we simulate it like we have [{data}.127.0.0.1].
And as you can see below we succeed to see the DNS traffic with the data in our local net.[The server in our local net 10.0.0.138]

Tools: DNS Tunneling & DNS server

DNScat2

Most of the other DNS Tunneling tools focus on tunneling TCP traffic using DNS, but this tool is different. DNScat2 is designed to create an encrypted command and control channel over the DNS. It borrows some concepts from Metasploit’s handler and is made with ease of use in mind.

Iodine

Iodine lets you tunnel IPv4 data through a DNS server. It creates a network interface on each of the clients and connects them together as if they shared the same network. This feature is unique to Iodine since other DNS tunneling tools focus on tunneling specific ports, and not the entire IPv4 traffic. This allows computers to ping each other, access all UDP/TCP ports and all other protocols that are encapsulated by an IP header.

Heyoka

Heyoka is an exfiltration tool that uses spoofed DNS requests to create a bidirectional tunnel. The tool is not under active development anymore and according to its authors, is up to 60% faster than other tools by using binary encoding and NULL records. Heyoka also focuses on stealth by sending spoofed DNS traffic from other hosts in the network. This makes detection by a firewall and locating the machine that’s tunneling much harder. With that said, it currently works only on Windows.

DNSteal - https://pythonforcybersecurity.com/lessons/lab-1data-exfiltration-using-dnssteal/



***traffic documentation in Wireshark***

<img src = https://user-images.githubusercontent.com/92265738/204931996-71458311-813b-42b4-a43f-5d3c944980c7.png width="700" height="300">
