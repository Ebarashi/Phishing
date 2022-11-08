import sys

data = sys.argv
username = data[1]
mail_service_name = data[2]  # like "@yahoo.com" or "@google.com" etc.
title = data[3]
job_title = data[4]
personal_status = data[5]
kids = data[6]

kid = []
try:
    if kids == 'yes':
        for kids in range(7, len(sys.argv)):
            kid.append(data[kids])

        int(data[len(sys.argv) - 1])  # if it works so there is no email from Joseph
        print("No email from Joseph.\n")

    else:
        # in case the last argument is an email from Joseph
        if data[len(sys.argv) - 1] == "no":
            print("No email from Joseph.\n")
        else:
            raise Exception("")


except:
    print("We got an email from Joseph:\n")
    email = data[len(sys.argv) - 1]
    print(email)


import smtplib, ssl

port = 465  # For SSL
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("my@gmail.com", password)
    # TODO: Send email here

print(f'username = {data[1]}\nmail_service_name = {data[2]}\ntitle = {data[3]}\njob_title = {data[4]}\n'
      f'personal_status = {data[5]}\nkids = {data[6]}')

for k in kid:
    print(k)