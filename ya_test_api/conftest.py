import pytest
import requests

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="Request ya.ru"
    )

@pytest.fixture()
def base_url(request):
    return request.config.getoption("--url")
