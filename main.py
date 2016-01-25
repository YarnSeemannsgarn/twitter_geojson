#!/usr/bin/env python

import json
import matplotlib.pyplot as plt
from communities_tirol import communitiesTirol
from osgeo import ogr
from LatLongUTMconversion import UTMtoLL
import dateutil.parser
import datetime

ELLIPSOID_ID = 23

""" 
Determine if a point is inside a given polygon or not Polygon is a list of (x,y) pairs. 
This function returns True or False.  The algorithm is called the "Ray Casting Method". 
Taken from http://geospatialpython.com/2011/01/point-in-polygon.html
"""
def pointInPolygon(x, y, poly):
    n = len(poly)
    inside = False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside

""" 
Reads specified shapefile and returns polygons.
Polygon format: [(x1, y1), (x2, y2), ...] 
"""
def readShapefile(filePath):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    datasource = driver.Open(filePath, 0)
    layer = datasource.GetLayer()

    polygons = []
    featureCount = layer.GetFeatureCount()
    for i in range (layer.GetFeatureCount()):
	feature = layer.GetFeature(i)
	geometry = feature.GetGeometryRef()
    	#print geometry.GetGeometryCount()
	for ring in range(geometry.GetGeometryCount()):
		outring = geometry.GetGeometryRef(ring)
                polygon = []
		for j in range(outring.GetPointCount()): 
			x = outring.GetX(j)
			y = outring.GetY(j)
                        lat_lon = UTMtoLL(ELLIPSOID_ID, y, x, '28R')
			polygon.append(lat_lon);
		if ring == 0:
			polygons.append(polygon)

    return polygons

"""
Read tweet data and change communityTweets and datesTweets
communityTweets --> amount of tweets per community
datesTweets --> amount of tweets per date
"""
def readTweets(data, polygons, communitiesTweets, datesTweets):
    for tweet in data["features"]:
        coordinates = tweet["geometry"]["coordinates"]
        for i, polygon in enumerate(polygons):
            if coordinates[0] > 10 and coordinates[0] < 14 and coordinates[1] > 46 and coordinates[1] < 48 and pointInPolygon(coordinates[1], coordinates[0], polygon):
                community = communitiesTirol[i]
                if community in communitiesTweets:
                    communitiesTweets[community] = communitiesTweets[community] + 1
                else:
                    communitiesTweets[community] = 1
                
                dateTimeISO = tweet["properties"]["isots"]
                dateTimeParsed = dateutil.parser.parse(dateTimeISO)
                datesTweets[dateTimeParsed.day-1] = datesTweets[dateTimeParsed.day-1] + 1
                print datesTweets
                break

"""
Saves the tweets per community to a file
"""
def saveCommunityTweets(communitiesTweets):
    f = open("community_tweets.csv", 'w')
    for communityTweets in communitiesTweets:
        f.write("{0}; {1}\n".format(communityTweets, communitiesTweets[communityTweets]))
    f.close()


"""
Plots the tweets per date
"""
def plotDatesTweets(datesTweets):
    # Plot datesTweets
    size = plt.rcParams["figure.figsize"]
    plt.rcParams["figure.figsize"] = [size[0]*3, size[1]]
    xAxis = []
    for i in xrange(27):
        xAxis.append(datetime.date(2014, 04, i+1))
    plt.plot(xAxis, datesTweets)
    plt.savefig('dates_tweets.png')


"""
MAIN METHOD - PROGRAMM STARTING POINT
"""
def main():
    # Read shapefile
    polygons = readShapefile("communities_tirol_map/Export_Output_2.shp")

    # Read geojson
    with open("boundingbox1.geojson") as f:
        data = json.load(f)

    # Read tweets and check polygons
    communitiesTweets = {}
    datesTweets = [0] * 27
    readTweets(data, polygons, communitiesTweets, datesTweets)
    
    # Save communityTweets
    saveCommunityTweets(communitiesTweets)
    
    # Plot datesTweets
    plotDatesTweets(datesTweets)

if __name__ == '__main__':
    main()
    
    
