def database_update(geom, identify, cursor, connect):
    cursor.execute(f'update public."HouseReestrs" set "Geom" = st_geomfromtext(\'{geom}\') where "Id" = \'{identify}\'')
    connect.commit()
