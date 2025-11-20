Feature: Google search

    As a user
    I want to search for a term on Google webpage
    So that I can access the first result

    Background:
        Given the the Google webpage is open


    Scenario: Search for the word “QA”
        When the user enters QA in the search box
        Then the user click on the first search result




