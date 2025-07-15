Feature: Health endpoint check

    Scenario: AT-01 Check app status
        When user call /health endpoint
        Then response should match JSON file features/data/AT-01/response.json
