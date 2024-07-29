Feature: Test Kainos industries page load

  Scenario: Testing accessibility on pages
    Given I navigate to the Kainos homepage
    When I accept cookies
    Then I should have a valid title for homepage
    And I check accessibility for the homepage
    And I click on the industries link
    Then I should have a valid title for industries page
    And I check accessibility for the industries page