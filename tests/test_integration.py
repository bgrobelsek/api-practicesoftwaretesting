import requests
from utils.helpers import generate_new_brand_name_and_slug


def test_brands_integration(session, base_url):
    """
    Integration test for the '/brands' API endpoints. This test performs the following steps:

    1. POST: Creates a new brand using the '/brands' endpoint.
        - Asserts that the response status code is 201 (Created).
        - Asserts that the returned brand ID is a string.

    2. GET: Retrieves the created brand by ID using the '/brands/{brandID}' endpoint.
        - Asserts that the response status code is 200 (OK).
        - Asserts that the retrieved brand's ID, name, and slug match the created brand.

    3. PUT: Updates the brand's details using the '/brands/{brandID}' endpoint.
        - Asserts that the response status code is 200 (OK).
        - Asserts that the response indicates success.

    4. GET: Verifies that the brand's details were updated correctly by fetching it again.
        - Asserts that the response status code is 200 (OK).
        - Asserts that the retrieved brand's ID, name, and slug match the updated values.
    """
    new_brand = generate_new_brand_name_and_slug()

    response_post = session.post(f"{base_url}/brands", json=new_brand)
    response_post_data = response_post.json()
    assert response_post.status_code == 201
    assert isinstance(response_post_data["id"], str)

    new_brand_id = response_post_data["id"]

    response_get = session.get(f"{base_url}/brands/{new_brand_id}")
    response_get_data = response_get.json()
    assert response_get.status_code == 200
    assert response_get_data["id"] == new_brand_id
    assert response_get_data["name"] == new_brand["name"]
    assert response_get_data["slug"] == new_brand["slug"]

    brand_change = generate_new_brand_name_and_slug()

    response_put = session.put(f"{base_url}/brands/{new_brand_id}", json=brand_change)
    response_put_data = response_put.json()
    assert response_put.status_code == 200
    assert response_put_data["success"] == True

    response_get = session.get(f"{base_url}/brands/{new_brand_id}")
    response_get_data = response_get.json()
    assert response_get.status_code == 200
    assert response_get_data["id"] == new_brand_id
    assert response_get_data["name"] == brand_change["name"]
    assert response_get_data["slug"] == brand_change["slug"]
