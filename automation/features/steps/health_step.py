"""Define the actions to perform /health check"""

from typing import Any

# pylint: disable=no-name-in-module
from behave import when, then
from requests import Response

# pylint: disable=import-error
from assertions.rest import RestAssertions
from generic_api_step import step_get_call_url
from features import config, constants


@when("user call /health endpoint")
def step_when_call_health_endpoint(context: Any) -> None:
    """Calling GET /health path on our api"""
    context.response = step_get_call_url("health")


@then("response should match JSON file {file_path}")
def step_then_response_should_match(context: Any, file_path: str) -> None:
    """Check health response match status and body"""
    expected_response: dict[str, Any] = config.load_json(file_path)
    actual_response = context.response

    RestAssertions.assert_not_error(actual_response)
    safe_response: Response = actual_response
    RestAssertions.assert_status(
        safe_response, expected_response.get(constants.STATUS_CODE)
    )
    RestAssertions.assert_body_match(
        safe_response.json(), expected_response.get(constants.BODY)
    )
