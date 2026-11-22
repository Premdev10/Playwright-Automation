Feature: Home page Functionality

  Scenario Outline: verify the shop section is visible under ecommerce section
    Given the user navigates to the login page
    When the user enters credentials from sheet "LoginData" with ID "<tc_id>"
    And clicks the login button
    Then the user should be redirected to the dashboard
    And user clicks on ecommerce tab
    Then validate user navigated in to the shop section

    Examples:
      | tc_id |
      | TC_01 |

  Scenario Outline: verify the add to cart functionality for a specific product
    Given the user navigates to the login page
    When the user enters credentials from sheet "LoginData" with ID "<tc_id>"
    And clicks the login button
    Then the user should be redirected to the dashboard
    And user clicks on ecommerce tab
    Then validate user navigated in to the shop section
    Then validate user able to add the product "<productname>" in to the cart

    Examples:
      | tc_id |productname|
      | TC_01 |Mechanical Keyboard|

  