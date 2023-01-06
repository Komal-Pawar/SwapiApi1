import requests
from utils.fetch_data import fetch_data
from typing import Dict, List
from utils.timing import timeit


@timeit
def get_all_character_names(result1: Dict) -> List:
    """
    pick only names from film data.:param result: data fetched from first film
    :type result1: object
    :return1: names of chars in movie 1
    """

    char_urls = result1.get("characters")
    char_data = fetch_data(char_urls) if char_urls else []  # ternary operator
    char_names1 = [char.get("name") for char in char_data]
    return char_names1


@timeit
def get_all_vehicle_names(result_: Dict) -> List:
    """
    pick all vehicle names:param result: data from first film :return: names of vehicles
    """

    v_urls = result_.get("vehicles")
    v_data = fetch_data(v_urls) if v_urls else []
    v_names1 = [vehicle.get("name") for vehicle in v_data if v_data]
    return v_names1


if __name__ == "__main__":
    url = "https://swapi.dev/api/films/1/"
    # response = requests.request("GET", url)
    response = requests.get(url)
    result = response.json()

    char_names = get_all_character_names(result)
    v_names = get_all_vehicle_names(result)

    print(char_names)
    print("------------------")
    print(v_names)
