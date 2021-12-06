#здесь тоже тесты проходят, все ок
import pytest
import requests



def test_check_ya(base_url):
    response = requests.get(base_url)
    assert response.status_code == 200

@pytest.mark.parametrize("id", ["sfhfhfhfhfhfhfhfh", 23, 0, -1])
def test_negative_yandex(base_url, id):
    response = requests.get(f"{base_url}/{id}")
    assert response.status_code == 404
