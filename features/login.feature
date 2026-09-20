Feature: User Login Functionality

  Scenario Outline: verify the login functionality
    Given the user navigates to the login page
    When the user enters credentials from sheet "LoginData" with ID "<tc_id>"
    And clicks the login button
    Then the user should be redirected to the dashboard

    Examples:
      | tc_id |
      | TC_01 |
