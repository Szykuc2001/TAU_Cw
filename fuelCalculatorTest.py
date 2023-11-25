from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def Test(driver):
    link= "https://www.calculator.net/fuel-cost-calculator.html"
    driver.get(link)
    time.sleep(3)
    distance= driver.find_element(By.NAME, "tripdistance")
    distance.clear()
    distance.send_keys("300")
    print("Trip Distance set to 300 km")
    fuel= driver.find_element(By.NAME,"fuelefficiency")
    fuel.clear()
    fuel.send_keys("4")
    print("Fuel Efficiency set to 4")
    price= driver.find_element(By.NAME,"gasprice")
    price.clear()
    price.send_keys("6")
    print("Gas/Fuel Price set to $6")
    time.sleep(1)
    driver.find_element(By.NAME,"x").click()
    print("Calculating trip data")
    time.sleep(3)
    result = driver.find_element(By.CLASS_NAME, "verybigtext")
    print(result.text)
    if result.text == "This trip will require 12 liters of fuel, which amounts to a fuel cost of $72.":
        print("Calculation successful")
    else:
        print("Calculation unsuccessful")
    time.sleep(3)
    driver.quit()
Test(webdriver.Firefox())
Test(webdriver.Chrome())