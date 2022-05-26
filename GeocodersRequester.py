import requests
from ApiKeys import HereApiKey, YandexApiKey


def here_geocoder(address):
    response = requests.get(f"https://geocode.search.hereapi.com/v1/geocode?q={address}&apiKey={HereApiKey}")
    if response.status_code == 200:
        response = response.json()
        if len(response['items']) != 0 and response['items'][0].get('position') is not None:
            geom = f"POINT({response['items'][0]['position']['lng']} {response['items'][0]['position']['lat']})"
            return geom
    return None


def yandex_geocoder(address):
    response = requests.get(
        "https://geocode-maps.yandex.ru/1.x/",
        params=dict(format="json", apikey=YandexApiKey, geocode=address, kind='house')
    )
    if response.status_code == 200:
        data = response.json()["response"]
        geom = f"POINT({data['GeoObjectCollection']['featureMember'][0]['point']['pos']})"
        return geom
    elif response.status_code == 403:
        print('Invalid key')
        return None
    else:
        print(f"status_code={response.status_code}, body={response.content}")
        return None
