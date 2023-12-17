from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given('I open the Amazon login page')
def step_open_amazon_login_page(context):
    context.driver = webdriver.Chrome()  # You can choose the browser of your choice
    context.driver.get("https://www.amazon.pl/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.pl%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=plflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

@when('I enter the username "{username}" and submit')
def step_enter_username(context, username):
    time.sleep(1)
    username_element = context.driver.find_element(By.ID, "ap_email")
    username_element.send_keys(username)
    username_element.send_keys(Keys.ENTER)
    time.sleep(3)

@when('I enter the password "{password}" and submit')
def step_enter_password(context, password):
    password_element = context.driver.find_element(By.ID, "ap_password")
    password_element.send_keys(password)
    password_element.send_keys(Keys.ENTER)
    time.sleep(3)

@then('I should see a successful login message')
def step_check_login_result(context):
    if "Wystąpił błąd" in context.driver.page_source:
        print("Login Error.")
    else:
        print("Login successful")
    context.driver.quit()
