from shapely.geometry import shape
from io import StringIO
import psycopg2
import json

with open('static/v.geojson') as f:
    geojson = json.load(open('static/v.geojson'))
data = StringIO()
for feature in geojson['features']:
    data.write(
        '\t'.join([
            shape(feature['geometry']).wkt,
            json.dumps(feature['properties'])]) + '\n')
data.seek(0)
conn = psycopg2.connect("dbname='xx' \
                        user='xx' \
                        host='xx' \
                        password='xx'")
curs = conn.cursor()
curs.copy_from(data, 'features', columns=('geometry', 'attributes'))
conn.commit()
conn.close()
