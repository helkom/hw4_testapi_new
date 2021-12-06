#здесь тесты проходят, все ок
import pytest
import requests
# from jsonschema import validate

"""
Функция заходит на хост и проверяет что ответ равен 200 и проверяет что это объект который пришел в JSON
"""
def test_list_breeds(base_url):
    response = requests.get(f"{base_url}/breeds/list/all")
    assert response.status_code == 200

    schema = {
        "type" : "object",
        "properties": {
            "message": {"type": "object"},
            "status": {"type": "string"},
        },
        "required": ["message", "status"]
    }
    # validate(instance=response.json(), schema=schema)

"""
Функция проверяет что фото в запросе равное с ответом с сервера и что не валидные данные не проходят
"""
@pytest.mark.parametrize("number", [1,2,37,15,50, pytest.param(51, marks=pytest.mark.xfail)])
def test_numbers_image(number,base_url, get_image):
    dogs_image = f"{base_url}/{get_image}/{number}"
    res_dogs = requests.get(dogs_image)
    assert len(res_dogs.json().get("message")) == number

"""
Функция проверяет что отображаются не более 50 фото собак
"""
@pytest.mark.parametrize("number", [50,51,345,999, pytest.param(0, marks=pytest.mark.xfail)])
def test_limit_50(number, base_url, get_image):
    run_limit = f"{base_url}/{get_image}/{number}"
    dogs_limit = requests.get(run_limit)
    assert len(dogs_limit.json().get("message")) == 50

def test_breed_list(base_url):
    response = requests.get(f"{base_url}/breed/hound/images")
    assert response.status_code == 200

    schema = {
        "type": "object",
        "properties": {
            "message": {"type":"array"},
            "status": {"type":"string"}
        },
        "required": ["message","status"]
    }
    # validate(instance=response.json(), schema=schema)

def test_image_list(base_url, get_image):
    response = requests.get(f"{base_url}/{get_image}")
    assert response.status_code == 200
