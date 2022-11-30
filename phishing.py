import os
import sys
from attach_create import send
import validators  # to check the validation of url
import requests



openingLine = ""
closingLine = ""

def readEamil(email,):

    if (os.path.exists(email)):  # txt file
        with open(email, 'r') as f:
            with open('emailFromJoseph.txt', 'w') as mail_from_j:
                mail_from_j.write(f.read())
                
    elif(isURL(email)):  # url
        url_content = requests.get(email)
        with open('emailFromJoseph.txt', 'w') as mail_from_j:
                mail_from_j.write(url_content.text)
                print(url_content.text)

    else:  #string
        with open('emailFromJoseph.txt', 'w') as mail_from_j:
                mail_from_j.write(email)

def isURL(_url):
    return validators.url(_url)



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
    print("We got an email from Joseph.\n")
    email = data[len(sys.argv) - 1]

    readEamil(email)

    # Find the opening line of the email
    with open('emailFromJoseph.txt', 'r') as f:
        # find() method returns -1 if the value is not found,
        # if found it returns index of the first occurrence of the substring
        lines = f.readlines()
        for row in lines:
            if row.find('Dear') != -1:
                openingLine = row
                if 'Mr.' or 'Ms.' in openingLine:
                    openingLine = openingLine.replace('Mr.', title)
                    openingLine = openingLine.replace('Ms.', title)

                    temp = openingLine.split(f'{title} ')
                    name_indx = temp[1].find(' ')  # the first word is the name that we want to replace
                    name = temp[1][:name_indx]
                    openingLine = openingLine.replace(name, username)  # replace the name of the emploee
                     

            if row.find('Joseph') != -1:
                closingLine = last_row
                # print(closingLine)
                break
            elif row != '\n':
                last_row = row

            if os.path.exists('emailFromJoseph.txt'):
                os.remove('emailFromJoseph.txt')
victom_email = username + mail_service_name
send(title, username, victom_email, openingLine, closingLine)
