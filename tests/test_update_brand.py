import pytest
import requests
from utils.helpers import create_brand_and_return_details, generate_new_brand_name_and_slug


def test_brands_put_with_valid_data_200(session, base_url):
    """
    Tests the /brands/{id} PUT endpoint with valid brand data.

    First, this tests creates a new brand and get its ID.
    Then, it updates the brand with a new name and slug 
    using the ID and checks if the response is 200.
    """
    brand_id, _, _ = create_brand_and_return_details(
        session, base_url
    )
    response = session.get(f"{base_url}/brands/{brand_id}")
    assert response.status_code == 200
    
    new_brand_name = generate_new_brand_name_and_slug()

    response = session.put(f"{base_url}/brands/{brand_id}", json=new_brand_name)
    response_data = response.json()
    assert response.status_code == 200

    assert isinstance(response_data, dict)
    assert isinstance(response_data["success"], bool)
    assert response_data["success"] == True 


def test_brands_put_with_invalid_id_200(session, base_url):
    """
    Test the /brands/{id} PUT endpoint with an invalid brand ID.

    This test attempts to update a brand using a clearly invalid brand ID 
    (e.g., "1234567") and checks that the response status code is 200. 
    It verifies that the response indicates the operation was not successful 
    by asserting that the 'success' field is False.
    """
    new_brand_name = {
        "name": "New Brand Name",
        "slug": "new-brand-name"
    }

    response = session.put(f"{base_url}/brands/1234567", json=new_brand_name)
    response_data = response.json()
    assert response.status_code == 200

    assert isinstance(response_data, dict)
    assert isinstance(response_data["success"], bool)
    assert response_data["success"] == False 


@pytest.mark.parametrize(
    "name, slug, error",
    [
        (None, None, {"name": ['The name field must be a string.'], "slug": ['The slug field must only contain letters, numbers, dashes, and underscores.', 'The slug field must be a string.']}),
        ("Random String", None, {"slug": ['The slug field must only contain letters, numbers, dashes, and underscores.', 'The slug field must be a string.']}),
        (None, "Random String", {'name': ['The name field must be a string.'], 'slug': ['The slug field must only contain letters, numbers, dashes, and underscores.']}),
        (123, 123, {"name": ["The name field must be a string."], "slug": ["The slug field must be a string."]}),
        ("Random String", 123, {"slug": ["The slug field must be a string."]}),
        (123, "Random String", {'name': ['The name field must be a string.'], 'slug': ['The slug field must only contain letters, numbers, dashes, and underscores.']}),
    ],
)
def test_brands_put_with_invalid_data_422(session, base_url, name, slug, error):
    """
    Test the /brands/{id} PUT endpoint with invalid brand data.

    This test verifies that when invalid data (e.g., None, non-string values) 
    is sent to update a brand using the PUT endpoint, the server responds 
    with a 422 status code and returns the appropriate error messages.
    The test uses parameterized inputs to cover multiple scenarios for 
    invalid 'name' and 'slug' fields.
    """
    brand_id, _, _ = create_brand_and_return_details(
        session, base_url
    )
    response = session.get(f"{base_url}/brands/{brand_id}")
    assert response.status_code == 200
    
    response = session.put(f"{base_url}/brands/{brand_id}", json={"name": name, "slug": slug})
    response_data = response.json()
    assert response.status_code == 422
    assert response_data == error
