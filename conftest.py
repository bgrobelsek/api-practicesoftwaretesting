import pytest
import requests


@pytest.fixture(scope="session")
def session():
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    return session


@pytest.fixture(scope="session")
def base_url():
    return "https://api.practicesoftwaretesting.com/"
