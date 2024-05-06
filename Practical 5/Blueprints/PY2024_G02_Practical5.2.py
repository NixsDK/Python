import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/title/tt6084202/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

director = soup.find('div', class_='credit_summary_item').find('a').text.strip()
writers = [writer.text.strip() for writer in soup.find_all('div', class_='credit_summary_item')[1].find_all('a')]
stars = [star.text.strip() for star in soup.find('div', class_='plot_summary_wrapper').find_all('a', href=True)[:3]]

awards_section = soup.find('span', {'class': 'awards-blurb'}).text.strip()
awards_received = awards_section.split('|')[0].strip()
awards_nominated = awards_section.split('|')[1].strip()

cast_list = soup.find('table', class_='cast_list')
cast = [(actor.find('a').text.strip(), actor.find('td', class_='character').text.strip()) for actor in cast_list.find_all('tr')[1:]]

print("Director:", director)
print("Writers:", writers)
print("Stars:", stars)
print("Awards Received:", awards_received)
print("Awards Nominated:", awards_nominated)
print("Cast:")
for i, (actor, role) in enumerate(cast, start=1):
    print(f"{i}. {actor} as {role}")
