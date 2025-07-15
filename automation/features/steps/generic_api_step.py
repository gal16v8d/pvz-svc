"""Include all generic calls that can be reused by any step"""

from http import HTTPStatus
from typing import Any

# pylint: disable=no-name-in-module
from behave import given, then
import requests

# pylint: disable=import-error
from features import config, constants
from features.assertions.rest import RestAssertions
from features.decorators.api_validator import rest_call_validator


def get_request_data(context: Any) -> Any | None:
    """Check request data and get the value if exists"""
    return getattr(context, "request_data", None)


@given("load request data from {request_file}")
def step_given_request_data(context: Any, request_file: str) -> None:
    """Load request json from a given file path"""
    context.request_data = config.load_json(request_file)


@then("user get error from api with code {status}")
def step_then_error_response_from_api(context: Any, status: str) -> None:
    """Check model response match status, and some body validations"""
    actual_response = context.response

    RestAssertions.assert_not_error(actual_response)
    safe_response: requests.Response = actual_response
    RestAssertions.assert_status(safe_response, int(status))
    RestAssertions.assert_content_type(safe_response, constants.JSON_TYPE)
    if safe_response.content:
        data = safe_response.json()
        if int(status) == HTTPStatus.UNPROCESSABLE_ENTITY.value:
            RestAssertions.assert_path_exists(data, constants.JSON_NODE_DETAIL)
        else:
            RestAssertions.assert_path_exists(data, constants.JSON_NODE_PATH)
            RestAssertions.assert_path_exists(data, constants.JSON_NODE_MESSAGE)


@then("user get error from api and msg is {msg}")
def step_then_error_response_from_api_match_msg(context: Any, msg: str) -> None:
    """Check model response match status, and some body validations"""
    actual_response = context.response

    RestAssertions.assert_not_error(actual_response)
    safe_response: requests.Response = actual_response
    RestAssertions.assert_content_type(safe_response, constants.JSON_TYPE)
    data = safe_response.json()
    RestAssertions.assert_path_value(data, constants.JSON_NODE_MESSAGE, msg)


@rest_call_validator
def step_get_call_url(path: str) -> Any:
    """Generic GET call to the api appending the path"""
    return requests.get(
        f"{config.get_base_url()}/{path}", timeout=constants.REQUEST_TIMEOUT
    )


@rest_call_validator
def step_post_call_url(path: str, payload: dict[str, Any] | None) -> Any:
    """Generic POST call to the api appending the path"""
    return requests.post(
        f"{config.get_base_url()}/{path}",
        json=payload,
        timeout=constants.REQUEST_TIMEOUT,
    )


@rest_call_validator
def step_patch_call_url(path: str, payload: dict[str, Any] | None) -> Any:
    """Generic PATCH call to the api appending the path"""
    return requests.patch(
        f"{config.get_base_url()}/{path}",
        json=payload,
        timeout=constants.REQUEST_TIMEOUT,
    )


@rest_call_validator
def step_delete_call_url(path: str) -> Any:
    """Generic DELETE call to the api appending the path"""
    return requests.delete(
        f"{config.get_base_url()}/{path}",
        timeout=constants.REQUEST_TIMEOUT,
    )
