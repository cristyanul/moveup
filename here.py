import requests
import json

app_ID = 'qU3ZB2KTa4r3RRxC84oL'
app_code = 'SfrJASqqHP3VSU6S6Yv0fA'

r = requests.get(('https://places.cit.api.here.com/places/v1/discover/around?app_id={}&app_code={}&at=45.74698273248355,21.24017715454102&pretty').format(app_ID, app_code))
data = r.json()

with open('output.json', 'w') as outfile:
    json.dump(data, outfile)

#{"type":"Point","coordinates":[21.23047829,45.74776136]}
#{"type":"Point","coordinates":[21.23253822,45.76572674]}
#{"type":"Point","coordinates":[21.23768806,45.75554707]}
#{"type":"Point","coordinates":[21.23253822,45.76572674]}
