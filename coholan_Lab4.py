#Eric Coholan
#4/20/2020
#GEOG 682 Lab 4

import processing 

dist = "S:/682/Spring20/ecoholan/Lab4/Police_Districts.shp"
crime = "S:/682/Spring20/ecoholan/Lab4/Crime_Incidents_in_2017.shp"

iface.addVectorLayer(dist,"dist","ogr")
iface.addVectorLayer(crime,"crime","ogr")

processing.run("qgis:joinattributesbylocation",
    {'INPUT':dist,'JOIN':crime,'PREDICATE':1,'METHOD':0,'OUTPUT':"S:/682/Spring20/ecoholan/Lab4/join.shp"})
    
#District 3 had the most crimes in 2017, with 5,970 crimes occurring there.
