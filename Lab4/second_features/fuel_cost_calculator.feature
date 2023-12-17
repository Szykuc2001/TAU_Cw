Feature: Fuel Cost Calculator
  Scenario: Calculate fuel cost for a trip
    Given I open the Fuel Cost Calculator page
    When I set the trip distance to 300 km
    And I set the fuel efficiency to 4
    And I set the gas/fuel price to $6
    And I calculate the trip data
    Then the result should be "This trip will require 12 liters of fuel, which amounts to a fuel cost of $72."
