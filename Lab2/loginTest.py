from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def Test(driver):
    link = "https://www.amazon.pl/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.pl%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=plflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
    driver.get(link)
    time.sleep(1)
    username = driver.find_element(By.ID, "ap_email")
    username.send_keys("sss@gmail.com")
    print("Login filled")
    username.send_keys(Keys.ENTER)
    time.sleep(3)
    password = driver.find_element(By.ID, "ap_password")
    password.send_keys("VeryStronkPassword")
    print("Password filled")
    password.send_keys(Keys.ENTER)

    time.sleep(3)
    if "Wystąpił błąd" in driver.page_source:
        print("Login Error.")
    else:
        print("Login successful")
    driver.quit()
Test(webdriver.Firefox())
Test(webdriver.Chrome())