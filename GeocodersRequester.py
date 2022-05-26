import requests
from ApiKeys import HereApiKey, yandex_api_key_funk


def here_geocoder(address):
    response = requests.get(f"https://geocode.search.hereapi.com/v1/geocode?q={address}&apiKey={HereApiKey}")
    if response.status_code == 200:
        response = response.json()
        if len(response['items']) != 0 and response['items'][0].get('position') is not None:
            geom = f"POINT({response['items'][0]['position']['lng']} {response['items'][0]['position']['lat']})"
            return geom
    return None


def yandex_geocoder(address):
    yandex_api_key = yandex_api_key_funk()
    key = next(yandex_api_key)
    while True:
        response = requests.get(
            "https://geocode-maps.yandex.ru/1.x/",
            params=dict(format="json", apikey=key, geocode=address, kind='house')
        )
        if response.status_code == 200:
            data = response.json()["response"]
            geom = f"POINT({data['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']})"
            return geom
        elif response.status_code == 403:
            key = next(yandex_api_key)
            print('Invalid key')
        else:
            print(f"status_code={response.status_code}, body={response.content}")
            return None
