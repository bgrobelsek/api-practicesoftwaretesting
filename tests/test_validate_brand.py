import json
from utils.helpers import create_brand_and_return_details


def test_get_brands_search_with_valid_id_200(session, base_url):
    """
    Test the /brands/{id} GET endpoint with a valid brand ID.

    Sends a GET request for a specific brand ID and checks that
    the response status code is 200. It verifies that the response
    contains the expected brand details, including non-empty
    values for ID, name, and slug.
    """
    brand_id, brand_name, brand_slug = create_brand_and_return_details(
        session, base_url
    )
    response = session.get(f"{base_url}/brands/{brand_id}")
    assert response.status_code == 200
    response_data = response.json()

    assert len(response_data) > 0
    assert isinstance(response_data, dict)
    assert isinstance(response_data["id"], str)
    assert response_data["id"] == brand_id
    assert isinstance(response_data["name"], str)
    assert response_data["name"] == brand_name
    assert isinstance(response_data["slug"], str)
    assert response_data["slug"] == brand_slug


def test_get_brands_search_with_invalid_id_404(session, base_url):
    """
    Test the /brands/{id} GET endpoint with an invalid brand ID.

    Sends a GET request with an invalid brand ID and checks that
    the response status code is 404. It verifies that the response
    contains the expected error message indicating that the item was not found.
    """
    response = session.get(f"{base_url}/brands/random")
    assert response.status_code == 404
    response_data = response.json()

    assert response_data["message"] == "Requested item not found"


def test_get_brands_search_with_invalid_method_405(session, base_url):
    """
    Test /brands/search?q= endpoint for unsupported HTTP methods.

    Sends a PATCH request and checks that the response status code
    is 405. Verifies the presence of a 'message' key indicating
    the method is not allowed.
    """
    response = session.post(f"{base_url}/brands/someId")
    assert response.status_code == 405
    data = response.json()

    assert isinstance(data, dict)
    assert "message" in data
    assert data["message"] == "Method is not allowed for the requested route"
