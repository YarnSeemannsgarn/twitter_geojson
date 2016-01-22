import json

with open('boundingbox1.geojson') as f:
    data = json.load(f)

print data["features"]
