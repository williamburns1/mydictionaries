'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

   1) print out the number of earthquakes'''

import json
infile = open('eq_data.json', 'r')
earthquakes = json.load(infile)
len(earthquakes['features'])

'''2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.'''

eq_dict = {}
n = -1
for feature in range(0, len(earthquakes['features'])):
    if earthquakes['features'][feature]['properties']['mag'] > 6:
        n = n + 1
        eq_dict['earthquake' + str(n)] = {
            'location': earthquakes['features'][feature]['properties']['place'],
            'magnitude': earthquakes['features'][feature]['properties']['mag'],
            'longitude': earthquakes['features'][feature]['geometry']['coordinates'][0], 'latitude': earthquakes['features'][feature]['geometry']['coordinates'][1]}

print(eq_dict)

'''3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364

Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604

Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628
'''
for earthquake in eq_dict:
    print("Location:", eq_dict[earthquake]['location'])
    print("Magnitude:", eq_dict[earthquake]['magnitude'])
    print("Longitude:", eq_dict[earthquake]['longitude'])
    print("Latitude:", eq_dict[earthquake]['latitude'], '\n')
