import requests

latitude = input("Enter latitude: ")
longitude = input("Enter longitude: ")

url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={latitude}&lon={longitude}"
response = requests.get(url)
data = response.json()

place_name = data.get('display_name')
place_type = data.get('type')
house_number = data.get('address', {}).get('house_number', 'N/A')
street = data.get('address', {}).get('road', 'N/A')
city = data.get('address', {}).get('city', 'N/A')
postcode = data.get('address', {}).get('postcode', 'N/A')
country_name = data.get('address', {}).get('country', 'N/A')
country_code = data.get('address', {}).get('country_code', 'N/A')

print("Place Name:", place_name)
print("Type:", place_type)
print("House Number:", house_number)
print("Street:", street)
print("City:", city)
print("Postcode:", postcode)
print("Country Name:", country_name)
print("Country Code:", country_code)
