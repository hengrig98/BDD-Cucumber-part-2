# Epic in Agile
Feature: Login

    Application must have login functionality. 


Scenario Outline: Login with invalid username and password combination. 
    When User enters username "<username>".
    And User enters password "<password>". 
    And User clicks login button. 
    Then text "<text>" will display. 

    Examples:
        | username | password | text                |
        | test     | test     | Invalid credentials |
        | %$^&*    | 126252   | Invalid credentials |
        # |     empty| test     |      Required       |
        # | test     |     empty|      Required       |


        # Compared to user story in agile
Scenario: Login with valid username and password.
    When User enters username "Admin"
    And User enters password "admin123"
    And User clicks login button. 
    Then Home page should display.
    