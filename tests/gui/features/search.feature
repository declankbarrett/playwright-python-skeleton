Feature: Test Kainos search feature

  Scenario: Test search functionality on Kainos homepage works as expected
    Given I navigate to the Kainos homepage
    When I accept cookies
    Then I should have a valid title for homepage
    And I search for test in the search bar
    Then I should have a valid title for search results page
