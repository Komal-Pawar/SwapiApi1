import requests
from utils.randgen import ProduceChars

start = 1
stop = 83


def get_chars(obj_: ProduceChars):
    characters_ = []  # [1, 4, 5, 13, ....]
    for i in obj_:
        characters_.append(i)

    return characters_


if __name__ == '__main__':
    print(__name__)
    print("current module getting executed")

    home_url = "https://swapi.dev/"
    relative = "/api/people/{0}"  # magic string
    print(f"[ INFO ] done producing random 15 characters_")

    obj = ProduceChars(start, stop)
    characters = get_chars(obj)

    import pdb

    pdb.set_trace()

    print(f"[ INFO ] done - producing random 15 characters")

    for num_ in characters:
        absolute_url = home_url + relative.format(num_)
        print(f"fetching details using - (absolute,url) =>\n")
        response = requests.get(absolute_url)
        response = response.json()
        print(response)
        print("######" * 25)
