import sys
import validators  # to check if URL is valid
# for HTML reading:
import pandas as pd
from pandas import read_html
import html5lib

data = sys.argv
username = data[1]
mail_service_name = data[2]  # like "@yahoo.com" or "@gmail.com" etc.
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
    if (email[len(email)-4:len(email)] == '.txt'):  # txt file
        with open(email) as f:
            lines = f.readlines()
            [print(line.strip()) for line in lines]

    else:  # (validators.url(email)):  # URL
        from selenium import webdriver
        import pandas as pd
        driver = webdriver.Chrome(chromedriver)
        driver.implicitly_wait(30)

        driver.get('https://www.wunderground.com/personal-weather-station/dashboard?ID=KMAHADLE7#history/tdata/s20170201/e20170201/mcustom.html')
        df=pd.read_html(driver.find_element_by_id("history_table").get_attribute('outerHTML'))[0]





        # url_data = pd.io.html.read_html(email)
        # print(url_data)
    
    #print(email)