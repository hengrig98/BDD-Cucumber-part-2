# Epic in Agile
Feature: Home

    User lands on homepage after logging in.  

    # Shared steps, similar to setup in POM...
    Background: Common steps before Each scenario. 
        Given Login Page is displayed.
        When User enters username "Admin".
        And User enters password "admin123". 
        And User clicks login button. 

Scenario Outline: Check user dropdown menus.
    When User clicks dropdown menu option. 
    And User clicks user menu option "<option>". 
    Then text "<text>" will display. 

    Examples:
        |        option      |      text     |
        |  About           |  Version        |
        | Support          |Customer Support |
        | Change Password  | Update Password |
        # | Logout           | Login           |