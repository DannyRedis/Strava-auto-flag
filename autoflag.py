# -*- coding: cp1252 -*-
from splinter import Browser
import time
import random

URL_login = "https://www.strava.com/login"
URL_target = ["https://www.strava.com/activities/xxxxxxxx",
              "https://www.strava.com/activities/xxxxxxxx",
              "https://www.strava.com/activities/xxxxxxxx"];
EMAIL = "example@example.com"
PASSWORD = "example"

CATEGORY = ['flag_category_1', 'flag_category_2',
            'flag_category_3', 'flag_category_0']
CAUSE = ["This activity was held in a motor vehicle",
          "This activity is incorrect",
          "GPS data is corrupted",
          "This activity was manipulated through digital EPO"]

with Browser() as browser:
    browser.visit(URL_login)
    if browser.is_element_present_by_id('email'):
        browser.fill('email', EMAIL)
        browser.fill('password', PASSWORD)
        browser.find_by_id('login-button').first.click()

    else:
        refresh()


    for i in URL_target:
        r = random.randint(0,3)
        browser.visit(i+"/flags/new")    
        browser.find_by_id(CATEGORY[r]).first.click()
        browser.fill("flag[comment]", CAUSE[r])
        browser.find_by_css('.reverse').click()
                        
    time.sleep(5)

