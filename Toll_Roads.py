from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import common

import re
from time import sleep
import SMS

driver = webdriver.Chrome("C:/Users/Arian/AppData/Local/Programs/Python/Python37-32/Scripts/chromedriver")  # Optional argument, if not specified will search path.

def valid_license():
    while True:
        plate = input("Enter License plate (with no spaces")
        if re.match("^[a-zA-Z0-9]+$",plate) is not None:
            break
        print('\n Invalid, try again')
    return plate




def enter_site(plate):

    driver.get("https://secure.thetollroads.com/violation/payTolls.do")
    driver.find_element_by_name("vehPlateNum").send_keys(plate)
    driver.find_element_by_name("vehPlateNumReenter").send_keys(plate)
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div[6]/button").send_keys(Keys.ENTER)
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div[3]/form/div[1]/div[1]/div/div/div/div/button").send_keys(Keys.ENTER)
    actions = webdriver.ActionChains(driver)
    sleep(2)
    actions.key_down(Keys.TAB)
    sleep(2)
    actions.key_up(Keys.TAB)
    actions.key_down(Keys.TAB)
    actions.key_up(Keys.TAB)
    # sleep(10)
    actions.key_down(Keys.ENTER)
    actions.key_up(Keys.ENTER)
    actions.perform()


    # Now I need to find a way to get the text of that part
    # After that I should be good.
    # Time to move onto learning how to do the constant check part
    try:
        c = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[2]/div[3]/form/div[1]/div/div/div/div[3]/div/h5").text
        if c == "You're quick! We haven't processed any tolls for this license plate yet - sometimes it takes up to 48 hours. For your convenience, you can provide your payment information now and we'll charge your tolls once they are processed.":
            print("Good, No toll fines")

            SMS.send_email("Ok, no fines bruv")

    except common.exceptions.NoSuchElementException:
        SMS.send_email("Check your toll roads fines.")


# license = valid_license()


enter_site(_Enter SOme number_asSTRING_)
sleep(10)
driver.quit()
