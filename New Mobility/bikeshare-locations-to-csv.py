# Obtain data from LA Metro Bikeshare locations for uses such as geocoding to shapefile in ArcGIS Developer

import csv
import time
import requests

url = 'https://gbfs.bcycle.com/bcycle_lametro/station_information.json'
r = requests.get(url)

bikestation_data = r.json()
bikestation_data_dict = bikestation_data['data']
bikestation_data_list = bikestation_data_dict['stations']

filename_with_time = 'bikestations_' + time.strftime('%Y%m%d') + '_' + time.strftime('%H%M') + '.csv'
# will write to new file in same folder as script
with open(filename_with_time, 'w', newline='') as file_to_write:
	writer = csv.writer(file_to_write)
	writer.writerow([
		'lon',
		'lat',
		'address',
		'name',
		'station_id',
	])
	
	for station in bikestation_data_list:
		print('Writing row...' + station['name'])
		writer.writerow([
			station['lon'],
			station['lat'],
			station['address'],
			station['name'],
			station['station_id'],
		])
