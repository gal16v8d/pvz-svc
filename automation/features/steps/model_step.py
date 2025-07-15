"""Define the actions to perform CRUD /api/{model} check"""

from http import HTTPStatus
from typing import Any

# pylint: disable=no-name-in-module
from behave import when, then
from requests import Response

# pylint: disable=import-error
from assertions.rest import RestAssertions
import generic_api_step
from features import constants


MODELS: dict[str, Any] = {
    "achievements": {
        "id": str,
        "name": str,
        "description": str,
    },
    "gardens": {
        "id": str,
        "number": int,
        "name": str,
        "max_plants": int,
        "coin_helper": bool,
    },
    "items": {
        "id": str,
        "name": str,
        "note": str,
    },
    "levels": {
        "id": str,
        "level": str,
        "unlock": list,
        "ref": str,
        "is_minigame": bool,
        "notes": str,
    },
    "minigames": {
        "id": str,
        "name": str,
    },
    "plants": {
        "id": str,
        "number": int,
        "name": str,
        "description": str,
        "text": str,
    },
    "puzzles": {
        "id": str,
        "name": str,
        "category": str,
        "with_streak": bool,
    },
    "survivals": {
        "id": str,
        "name": str,
        "flags": int,
        "endless": bool,
    },
    "zombies": {
        "id": str,
        "number": int,
        "name": str,
        "text": str,
        "toughness": str,
    },
}


@when("user call model GET endpoint as /api/{path}")
def step_when_call_get_all_model_endpoint(context: Any, path: str) -> None:
    """Calling GET /api/{path} on our api"""
    context.response = generic_api_step.step_get_call_url(f"api/{path}")


@when("user call model GET by Id endpoint as /api/{path}/{model_id}")
def step_when_call_get_by_id_model_endpoint(
    context: Any, path: str, model_id: int
) -> None:
    """Calling GET /api/{path}/{model_id} on our api"""
    context.response = generic_api_step.step_get_call_url(f"api/{path}/{model_id}")


@when("user call model POST endpoint as /api/{path}")
def step_when_call_post_model_endpoint(context: Any, path: str) -> None:
    """Calling POST /api/{path} on our api"""
    context.response = generic_api_step.step_post_call_url(
        f"api/{path}",
        generic_api_step.get_request_data(context),
    )


@when("user call model PATCH endpoint as /api/{path}/{model_id}")
def step_when_call_patch_model_endpoint(context: Any, path: str, model_id: int) -> None:
    """Calling PATCH /api/{path}/{model_id} on our api"""
    context.response = generic_api_step.step_patch_call_url(
        f"api/{path}/{model_id}",
        generic_api_step.get_request_data(context),
    )


@when("user call model DELETE endpoint as /api/{path}/{model_id}")
def step_when_call_delete_model_endpoint(
    context: Any, path: str, model_id: int
) -> None:
    """Calling DELETE /api/{path}/{model_id} on our api"""
    context.response = generic_api_step.step_delete_call_url(
        f"api/{path}/{model_id}",
    )


@then("response should match model list validations")
def step_then_model_response_should_match_list(context: Any) -> None:
    """Check model response match status, and some body validations"""
    actual_response = context.response

    RestAssertions.assert_not_error(actual_response)
    safe_response: Response = actual_response
    RestAssertions.assert_status(safe_response, HTTPStatus.OK.value)
    RestAssertions.assert_content_type(safe_response, constants.JSON_TYPE)
    data = safe_response.json()
    RestAssertions.assert_is_list(data)
    if len(data) > 0:
        model = getattr(context, constants.JSON_NODE_PATH, "")
        arg_and_type = MODELS.get(model, {})
        RestAssertions.assert_data_elements(data[0], arg_and_type)


@then("response should match model element validations")
def step_then_model_response_should_match_single(context: Any) -> None:
    """Check model response match status, and some body validations"""
    actual_response = context.response

    RestAssertions.assert_not_error(actual_response)
    safe_response: Response = actual_response
    RestAssertions.assert_status(safe_response, HTTPStatus.OK.value)
    RestAssertions.assert_content_type(safe_response, constants.JSON_TYPE)
    data = safe_response.json()
    model = getattr(context, constants.JSON_NODE_PATH, "")
    arg_and_type = MODELS.get(model, {})
    RestAssertions.assert_data_elements(data, arg_and_type)


@then("request data is cleared out")
def step_then_request_data_is_cleared(context: Any) -> None:
    """Clear out request data"""
    if hasattr(context, "request_data") and context.request_data:
        context.request_data = None
