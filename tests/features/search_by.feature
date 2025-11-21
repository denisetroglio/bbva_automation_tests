Feature: Search QA on websites

    As a user
    I want to search for a term on webpage
    So I can access the first result

    Scenario Outline: Search by "<word>" and click on first result
        Given the <website> is open
        When the user enters <word> in the search box
        Then the user click on the first search result

        Examples:
            | website    | word |
            | DuckDuckGo | QA   |
            | Google     | QA   |
