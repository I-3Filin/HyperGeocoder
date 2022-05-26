def data_get(cursor):
    cursor.execute('SELECT "Address", "Id" FROM public."HouseReestrs" where "Geom" is null limit 10')
    entity_list = cursor.fetchall()
    return entity_list
