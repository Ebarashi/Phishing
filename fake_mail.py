import sys
import validators  # to check if URL is valid
# for HTML reading:
import pandas as pd
from pandas import read_html
import html5lib
from send_mail import send

data = sys.argv
username = data[1]  # the name of the victom in mail account
mail_service_name = data[2]  # like "@yahoo.com" or "@google.com" etc.
title = data[3]  # Ms./Mr.
job_title = data[4]  # student/emploee/managor
personal_status = data[5]  # single/married
kids = data[6]  #yes/no

kid = []  # if to the victom has kids he need to write their ages

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
    if (email[len(email)-4:len(email)] == '.txt'):  # txt file
        with open(email) as f:
            lines = f.readlines()
            [print(line.strip()) for line in lines]

    # else:  # (validators.url(email)):  # URL
    #     url_data = pd.io.html.read_html(email)
    #     print(url_data)
    
    print("\n The user insert: " + email)

    victom_email = username + mail_service_name

    send(title, username, victom_email)