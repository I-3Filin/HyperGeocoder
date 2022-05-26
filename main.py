from Connect import cursor, connect
from GeocodersRequester import here_geocoder, yandex_geocoder
from DatabaseCoordinateUpdater import database_update
from DataFromDb import data_get


while True:
    EntityList = data_get(cursor)
    if len(EntityList) == 0:
        break
    for i in EntityList:
        HereData = here_geocoder(i[0])
        if HereData is not None:
            database_update(HereData, i[1], cursor, connect)
            print('coordinates found by HereGeocoder')
        else:
            YandexData = yandex_geocoder(i[0])
            if YandexData is not None:
                database_update(YandexData, i[1], cursor, connect)
                print('coordinates found by YandexGeocoder')
            elif YandexData is None:
                print('ran out of ApiKeys')
                break
            else:
                print('coordinates not found')

cursor.close()
connect.close()
