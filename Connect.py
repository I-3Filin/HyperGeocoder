import psycopg2

connect = psycopg2.connect(dbname='housing_reform', user='trefilin', password='OGzFE9XjwtEN', host='172.16.27.36',
                           port='5432')
cursor = connect.cursor()
