Feature: Test Kainos homepage load

  Scenario:
    Given I navigate to the Kainos homepage
    When I accept cookies
    Then I should have a valid title for homepage
