import urllib2
import json

from geopy import geocoders
from .apis import *

def find_place(query):
	g = geocoders.GoogleV3()
	place, lat, lng, = find_place(query)

def forsquare_search(query):
	token = forsquare_token
	place, lat, lng = find_place(query)

	