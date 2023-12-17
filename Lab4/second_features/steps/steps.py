from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('I open the Fuel Cost Calculator page')
def step_open_fuel_cost_calculator(context):
    context.driver = webdriver.Chrome()  # You can choose the browser of your choice
    context.driver.get("https://www.calculator.net/fuel-cost-calculator.html")

@when('I set the trip distance to {distance} km')
def step_set_trip_distance(context, distance):
    trip_distance = context.driver.find_element(By.NAME, "tripdistance")
    trip_distance.clear()
    trip_distance.send_keys(distance)
    print(f"Trip Distance set to {distance} km")

@when('I set the fuel efficiency to {fuel_efficiency}')
def step_set_fuel_efficiency(context, fuel_efficiency):
    fuel_efficiency_input = context.driver.find_element(By.NAME, "fuelefficiency")
    fuel_efficiency_input.clear()
    fuel_efficiency_input.send_keys(fuel_efficiency)
    print(f"Fuel Efficiency set to {fuel_efficiency}")

@when('I set the gas/fuel price to ${price}')
def step_set_gas_price(context, price):
    gas_price_input = context.driver.find_element(By.NAME, "gasprice")
    gas_price_input.clear()
    gas_price_input.send_keys(price)
    print(f"Gas/Fuel Price set to ${price}")

@when('I calculate the trip data')
def step_calculate_trip_data(context):
    context.driver.find_element(By.NAME, "x").click()
    print("Calculating trip data")
    time.sleep(3)

@then('the result should be "{expected_result}"')
def step_check_result(context, expected_result):
    result = context.driver.find_element(By.CLASS_NAME, "verybigtext").text
    print(result)
    assert result == expected_result, "Calculation unsuccessful."

@then('I close the browser')
def step_close_browser(context):
    context.driver.quit()
