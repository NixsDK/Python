import urllib.request
import json

def reverse_geocode(lat, lon):
    api_url = f'https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}'
    
    try:
        with urllib.request.urlopen(api_url) as response:
            response_data = response.read()
            
            data = json.loads(response_data)
            
            if 'address' in data:
                address = data['address']
                place_name = address.get('name', 'N/A')
                place_type = data.get('type', 'N/A')
                house_number = address.get('house_number', 'N/A')
                street_name = address.get('road', 'N/A')
                city = address.get('city', address.get('town', address.get('village', 'N/A')))
                postcode = address.get('postcode', 'N/A')
                country_name = address.get('country', 'N/A')
                country_code = address.get('country_code', 'N/A')
                
                print(f'Place Name: {place_name}')
                print(f'Place Type: {place_type}')
                print(f'House Number: {house_number}')
                print(f'Street Name: {street_name}')
                print(f'City: {city}')
                print(f'Postcode: {postcode}')
                print(f'Country Name: {country_name}')
                print(f'Country Code: {country_code}')
            else:
                print('Error: Unable to retrieve address information.')
    except urllib.error.URLError as e:
        print(f'Error: Failed to get data from the API. URLError: {e}')

lat = float(input('Enter latitude: '))
lon = float(input('Enter longitude: '))

reverse_geocode(lat, lon)
