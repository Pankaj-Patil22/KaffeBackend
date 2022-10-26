Feature: Choose a table.
  As a user I should be able to choose the date and time and a table.

  Scenario: book table
    Given the account is logged in
    When i click tables tab, it should nagivate to tables page
    Then i choose the date and time 
    Then i choose the table i want to book 
    Then it should show me that total price