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

	latlng = 'll=' + str(lat) + '%2C%20' + str(lng)
	print latlng
	url = 'https://api.foursquare.com/v2/venues/search?v=20120321&' + latlng + '&intent=checkin&oauth_token='
	full_url = url + token

	obj = urllib2.urlopen(full_url)
	data = json.load(obj)

	locations = []
	for location in data['response']['venues']:
		print location['name']
		locations.append(location['name'])
		try:
			print 'phone = ' + location['contact']['phone']
		except Exception:
			pass

		try:
            print 'twitter = ' + abc['contact']['twitter']
        except Exception:
            pass
    
        try:
            print 'city = ' + abc['location']['city']
        except Exception:
            pass

    return locations

	