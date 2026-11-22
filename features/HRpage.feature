Feature: Verify the HR page functionality

Scenario Outline: Verify the user is able to enters to the HR page
    Given the user navigates to the login page
    When the user enters credentials from sheet "LoginData" with ID "<tc_id>"
    And clicks the login button
    Then the user should be redirected to the dashboard
    And user clicks on HR tab
    Then verify user eneters in to the HR section

     Examples:
      | tc_id |
      | TC_01 |

Scenario Outline: Verify the total entries in the employee table
    Given the user navigates to the login page
    When the user enters credentials from sheet "LoginData" with ID "<tc_id>"
    And clicks the login button
    Then the user should be redirected to the dashboard
    And user clicks on HR tab
    Then verify user eneters in to the HR section
    Then verify the total entries in the table

     Examples:
      | tc_id |
      | TC_01 |