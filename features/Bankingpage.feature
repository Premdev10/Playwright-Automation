Feature:Verify the banking page functionality

  # Scenario Outline: verify the add to cart functionality for a specific product
  #   Given the user navigates to the login page
  #   When the user enters credentials from sheet "LoginData" with ID "<tc_id>"
  #   And clicks the login button
  #   Then the user should be redirected to the dashboard
  #   And user clicks on banking button
  #   Then user clicks on the transfer money link
  #   Then verify user should be able to transfer the money
  #   Examples:
  #     | tc_id |
  #     | TC_01 |

  # Scenario Outline: verify the transaction history in the banking page
  #   Given the user navigates to the login page
  #   When the user enters credentials from sheet "LoginData" with ID "<tc_id>"
  #   And clicks the login button
  #   Then the user should be redirected to the dashboard
  #   And user clicks on banking button
  #   Then user clicks on the transaction history tab
  #   Then verify the transaction is available in the table
  #   Examples:
  #     | tc_id |
  #     | TC_01 |

  Scenario Outline: verify the beneficiary added successfully
    Given the user navigates to the login page
    When the user enters credentials from sheet "LoginData" with ID "<tc_id>"
    And clicks the login button
    Then the user should be redirected to the dashboard
    And user clicks on banking button
    Then user clicks on the beneficiary tab
    Then verify able to add the beneficiary
    Then verify beneficiary available in the table
    Examples:
      | tc_id |
      | TC_01 |