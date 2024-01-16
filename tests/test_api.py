import os
import json
import requests
import requests_mock
from src.api import get_data

def test_get_data():
    liquor = 'whisky'
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={liquor}"
    result = requests.get(url)
    assert result.status_code == 200

    json_path = os.path.join(os.path.dirname(__file__), 'whisky.json')
    with open(json_path, 'r') as json_file:
        whisky_data = json.load(json_file)
        assert result.json() == whisky_data

def test_get_data_with_mock():
    with requests_mock.Mocker() as mocker:
        mock_response_json = {
            "drinks": [
                {
                    "idDrink": "12518",
                    "strDrink": "Whisky Mac",
                    "strInstructions": "Pour both of the ingredients into a wine goblet with no ice.",
                    "strInstructionsES": None,
                }
            ]
        }
        liquor = 'Whisky'
        url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={liquor}"
        mocker.get(url, json=mock_response_json)
        result = get_data(url)

        assert result == mock_response_json
        

# import requests
# import src.api
# import pytest


# class MockResponse:
#     @staticmethod
#     def json():
#         return {"mock_key": "mock_response"}


# @pytest.fixture(autouse=True)
# def mock_response(monkeypatch):
#     def mock_get(*args, **kwargs):
#         return MockResponse()

#     monkeypatch.setattr(requests, "get", mock_get)


# def test_get_data(mock_response):
#     result = src.api.get_data("https://fakeurl")
#     assert result["mock_key"] == "mock_response"
