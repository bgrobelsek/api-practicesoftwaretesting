from faker import Faker
from slugify import slugify

fake = Faker()


def slugify_company_name(name):
    """Converts a company name to a slug using slugify."""
    return slugify(name, separator="-")


def generate_new_brand_name_and_slug():
    """Generates a new brand with a name and slug."""
    name = fake.company()
    slug = slugify_company_name(name)

    new_brand_name_and_slug = {
        "name": name,
        "slug": slug,
    }
    return new_brand_name_and_slug


def create_brand_and_return_details(session, base_url):
    """Creates a new brand and returns its name, slug, and ID."""
    brand_payload = generate_new_brand_name_and_slug()
    response = session.post(f"{base_url}/brands", json=brand_payload)

    if response.status_code == 201:
        response_data = response.json()
        return response_data["id"], response_data["name"], response_data["slug"]

    raise Exception(f"Failed to create brand: {response.status_code} - {response.text}")
