import pytest
import requests
from jsonschema import validate

def test_api_status_code(base_url):
    response = requests.get(base_url)
    assert response.status_code == 200

def test_schema_brewereis(base_url):
    response = requests.get(f"{base_url}/breweries")
    assert response.status_code == 200
    resp = response.json()
    schema={
        "type":"array",
        "items": {
            "type": "object"
        }
    }
    validate(resp, schema)

@pytest.mark.parametrize("id", [1,24, 3476,55, 721])
def test_id_list(base_url, id):
    url = requests.get(f"{base_url}/breweries/{id}")
    assert url.status_code == 200
    response = url.json()
    assert response["id"] == id

def test_query_search(base_url):
    response = requests.get(f"{base_url}/breweries/search?query=dog")
    assert response.status_code == 200
