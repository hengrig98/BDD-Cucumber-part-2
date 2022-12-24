# Epic in Agile
Feature: Login

    Application must have login functionality. 

    # Shared steps, similar to setup in POM...
    Background: Common steps before Each scenario. 
        Given Login Page is displayed.


# User story in agile
@login
Scenario: Login with Valid username & password. 
    When User enters username "Admin".
    And User enters password "admin123". 
    And User clicks login button. 
    Then New page will display. 


Scenario Outline: Login with invalid username and password combination. 
    When User enters username "<username>".
    And User enters password "<password>". 
    And User clicks login button. 
    Then text "<text>" will display. 

    Examples:
        | username | password | text                |
        | test     | test     | Invalid credentials |
        | %$^&*    | 126252   | Invalid credentials |
        |     empty| test     |      Required       |
        | test     |     empty|      Required       |