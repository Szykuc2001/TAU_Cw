Feature: Amazon Login
  Scenario: Login to Amazon
    Given I open the Amazon login page
    When I enter the username "sss@gmail.com" and submit
    And I enter the password "VeryStronkPassword" and submit
    Then I should see a successful login message
