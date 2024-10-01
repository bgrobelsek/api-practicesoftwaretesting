import pytest
import requests
from utils.helpers import generate_new_brand_name_and_slug


def test_create_new_brand_with_valid_payload_201(session, base_url):   
    """
    Test successful creation of a new brand via POST request.

    This test verifies that sending a valid brand payload to the /brands endpoint
    returns a 201 status code and the expected response structure, including the
    unique identifier (id), brand name, and slug. A helper function is used to
    generate a new brand payload with a random name and slug.
    """
    brand_payload = generate_new_brand_name_and_slug()

    response = session.post(f"{base_url}/brands", json=brand_payload)

    assert response.status_code == 201
    response_data = response.json()

    assert isinstance(response_data, dict)
    assert isinstance(response_data["id"], str)
    assert response_data["name"] == brand_payload["name"]
    assert isinstance(response_data["name"], str)
    assert response_data["slug"] == brand_payload["slug"]
    assert isinstance(response_data["slug"], str)
    assert response_data["id"] is not None
    assert isinstance(response_data["id"], str)


def test_create_new_brand_with_unsupported_method_405(session, base_url):
    """
    Test handling of unsupported HTTP method on /brands endpoint.

    This test checks that a PUT request to the /brands endpoint returns a 405 
    status code and the appropriate error message.
    """
    brand_payload = {
        "name": "Random String",
        "slug": None,
    }
    response = session.put(f"{base_url}/brands", json=brand_payload)

    assert response.status_code == 405
    response_data = response.json()

    assert isinstance(response_data, dict)
    assert "message" in response_data
    assert response_data["message"] == "Method is not allowed for the requested route"


@pytest.mark.parametrize(
    "name, slug, error",
    [
        (None, None, {"name": ["The name field is required."], "slug": ["The slug field is required."]}),
        ("Random String", None, {"slug": ["The slug field is required."]}),
        (None, "Random String", {'name': ['The name field is required.'], 'slug': ['The slug field must only contain letters, numbers, dashes, and underscores.']}),
        (123, 123, {"name": ["The name field must be a string."], "slug": ["The slug field must be a string."]}),
        ("Random String", 123, {"slug": ["The slug field must be a string."]}),
        (123, "Random String", {'name': ['The name field must be a string.'], 'slug': ['The slug field must only contain letters, numbers, dashes, and underscores.']}),
    ],
)
def test_create_new_brand_with_invalid_data_422(session, base_url, name, slug, error):
    """Test creation of a brand with invalid data results in a 422 status code.

    This test verifies that providing invalid values for the name and slug fields 
    returns a 422 status code along with the expected error messages.
    """
    brand_payload = {
        "name": name,
        "slug": slug,
    }
    response = session.post(f"{base_url}/brands", json=brand_payload)

    assert response.status_code == 422
    response_data = response.json()

    assert response_data == error
