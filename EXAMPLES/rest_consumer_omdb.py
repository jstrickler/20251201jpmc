import requests
from pprint import pprint

with open('omdbapikey.txt') as api_in:
    OMDB_API_KEY = api_in.read().rstrip()

OMDB_URL = "http://www.omdbapi.com"

def main():
    requests_params = {'t': 'Wicked', "apikey": OMDB_API_KEY}
    timeout = (3, 5)
    response = requests.get(
        OMDB_URL, 
        params=requests_params, 
        timeout=timeout,
    )
    if response.status_code == requests.codes.OK:  # 200
        raw_data = response.json()  # convert JSON to Python data structure

        print(f"raw_data['Title']: {raw_data['Title']}")
        print(f"raw_data['Director']: {raw_data['Director']}")
        print(f"raw_data['Year']: {raw_data['Year']}")
        print(f"raw_data['Runtime']: {raw_data['Runtime']}")
        print()

        print('-' * 60)

        print("raw DATA:")
        pprint(response.json(), sort_dicts=False, depth=1)
    else:
        print(f"response.status_code: {response.status_code}")

if __name__ == '__main__':
    main()
