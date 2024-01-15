import requests
import requests_mock
from src.api import get_data



def test_get_data():
    liquor = 'whisky'
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={liquor}"
    result = requests.get(url)
    assert result.status_code == 200
    assert result.json() == {
    "drinks": [
        {
            "idDrink": "12518",
            "strDrink": "Whisky Mac",
            "strDrinkAlternate": None,
            "strTags": None,
            "strVideo": None,
            "strCategory": "Ordinary Drink",
            "strIBA": None,
            "strAlcoholic": "Alcoholic",
            "strGlass": "Collins Glass",
            "strInstructions": "Pour both of the ingredients into a wine goblet with no ice.",
            "strInstructionsES": None,
            "strInstructionsDE": "Beide Zutaten in einen Weinkelch geben, ohne Eis.",
            "strInstructionsFR": None,
            "strInstructionsIT": "Versare entrambi gli ingredienti in un calice da vino senza ghiaccio.",
            "strInstructionsZH-HANS": None,
            "strInstructionsZH-HANT": None,
            "strDrinkThumb": "https://www.thecocktaildb.com/images/media/drink/yvvwys1461867858.jpg",
            "strIngredient1": "Scotch",
            "strIngredient2": "Wine",
            "strIngredient3": None,
            "strIngredient4": None,
            "strIngredient5": None,
            "strIngredient6": None,
            "strIngredient7": None,
            "strIngredient8": None,
            "strIngredient9": None,
            "strIngredient10": None,
            "strIngredient11": None,
            "strIngredient12": None,
            "strIngredient13": None,
            "strIngredient14": None,
            "strIngredient15": None,
            "strMeasure1": "1 1/2 oz ",
            "strMeasure2": "1 oz Green Ginger ",
            "strMeasure3": None,
            "strMeasure4": None,
            "strMeasure5": None,
            "strMeasure6": None,
            "strMeasure7": None,
            "strMeasure8": None,
            "strMeasure9": None,
            "strMeasure10": None,
            "strMeasure11": None,
            "strMeasure12": None,
            "strMeasure13": None,
            "strMeasure14": None,
            "strMeasure15": None,
            "strImageSource": None,
            "strImageAttribution": None,
            "strCreativeCommonsConfirmed": "No",
            "dateModified": "2016-04-28 19:24:18",
        }
    ]
}

    
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