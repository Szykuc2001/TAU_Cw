**Testing Scenario 1:**
1. Open Amazon website for login
2. Fill e-mail field with some placeholder data, press ENTER and wait 3 seconds for the site to process the request
3. After 3 seconds, fill the password field, press ENTER and wait 3 seconds for the site to process the request
4. If the following string: 'Wystąpił błąd' is found in the page source, then the test is successful and Login Error. message should be displayed, otherwise test is unsuccessful and Login successful message is displayed

**Testing Scenario 2:**
1. Open the fuel cost calculator website and wait 3 seconds
2. Fill tripdistance field with value of 300
3. Fill fuelefficiency field with value of 4
4. Fill gasprice field with value of 6 and wait 1 second
5. Find element called x and click it
6. Wait 3 seconds for the site to process the request.
7. Find verybigtext field.
8. If the field equals to This trip will require 12 liters of fuel, which amounts to a fuel cost of $72. then the test was successful and Calculation successful. message should be displayed, otherwise message Calculation unsuccessful. is displayed.