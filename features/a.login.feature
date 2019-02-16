Feature: Login into replicon

    Scenario: fill credentials
        Given Go to login page
        When fill valid credentials
        Then click on login