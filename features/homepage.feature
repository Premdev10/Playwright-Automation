Feature: Home page Functionality

  Scenario Outline: verify the dynamic id field
    Given the user navigates to the login page
    When the user enters credentials from sheet "LoginData" with ID "<tc_id>"
    And clicks the login button
    Then the user should be redirected to the dashboard
    Then user validates the dynamic id field is present on the dashboard

    Examples:
      | tc_id |
      | TC_01 |

  Scenario Outline: verify the hidden element
    Given the user navigates to the login page
    When the user enters credentials from sheet "LoginData" with ID "<tc_id>"
    And clicks the login button
    Then the user should be redirected to the dashboard
    Then user validates the hidden element is visible and becomes invisible after clicks

    Examples:
      | tc_id |
      | TC_01 |

  Scenario Outline: verify the delayed content loaded successfully
    Given the user navigates to the login page
    When the user enters credentials from sheet "LoginData" with ID "<tc_id>"
    And clicks the login button
    Then the user should be redirected to the dashboard
    Then user validates the delayed content loaded successfully

    Examples:
      | tc_id |
      | TC_01 |

  Scenario Outline: verify the alert shown successfully
    Given the user navigates to the login page
    When the user enters credentials from sheet "LoginData" with ID "<tc_id>"
    And clicks the login button
    Then the user should be redirected to the dashboard
    Then user validates the alert shown successfully

    Examples:
      | tc_id |
      | TC_01 |

  Scenario Outline: verify the prompt shown successfully
    Given the user navigates to the login page
    When the user enters credentials from sheet "LoginData" with ID "<tc_id>"
    And clicks the login button
    Then the user should be redirected to the dashboard
    Then user validates the prompt shown successfully

    Examples:
      | tc_id |
      | TC_01 |