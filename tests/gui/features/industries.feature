Feature: Test Kainos industries page load

  Scenario: Test Kainos industries page loads as expected
    Given I navigate to the Kainos homepage
    When I accept cookies
    Then I should have a valid title for homepage
    And I click on the industries link
    Then I should have a valid title for industries page
