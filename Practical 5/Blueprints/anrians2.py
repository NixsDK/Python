from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/title/tt6084202/'

def get_movie_data(url):
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'
    }
    
    request = Request(url, headers=headers)
    
    with urlopen(request) as response:
        soup = BeautifulSoup(response.read(), 'html.parser')
        
    Main_stars = set()
    Writer_set = set()

    director = soup.find('a', {'class' : 'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link'})
    writers = soup.find_all('a', href=lambda href: href and '/name/' in href and 'tt_ov_wr' in href)
    stars = soup.find_all('a', href=lambda href: href and '/name/' in href and 'tt_ov_st' in href)
    awards_section = soup.find('span', {'class': 'ipc-metadata-list-item__list-content-item'})
    actors = soup.find_all('div', {'class' : 'sc-bfec09a1-7 gWwKlt'})
    
    for writer in writers:
        writer_name = writer.text
        Writer_set.add(writer_name)
    
    for star in stars:
        star_name = star.text
        Main_stars.add(star_name)
        
    print("Director:", director.get_text() if director else 'N/A')
    print("\nWriters:")
    for writer in Writer_set:
        print(f"- {writer}")
        
    print("\nMain stars:")
    for star in Main_stars:
        print(f"- {star}")

    if awards_section:
        print("\nAwards:", awards_section.get_text().strip())
    else:
        print("\nAwards: N/A")
        
    print("\nMovie actors:")
    for actor in actors:
        actor_name = actor.find('a', {'data-testid': 'title-cast-item__actor'})
            
        if actor_name is not None:
            actor_name = actor_name.text
        else:
            actor_name = "N/A"
            
        character = actor.find('span', {'class' : 'sc-bfec09a1-4 kvTUwN'})
            
        if character is not None:
            character = character.text
        else:
            character = "N/A"

        print(f"- Actor: {actor_name}, Character: {character}")

get_movie_data(url)
