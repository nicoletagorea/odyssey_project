import requests
from bs4 import BeautifulSoup

def extract_movie_data_for_year(year: int):
    """Fetch the most popular movies in a given year
    
    Args:
        year (int): the year for which to fetch the most popular movies
        
    Returns:
        list: a list of dictionaries, each containing movie information
    """
    url = f'https://www.google.com/search?q=popular+movies+in+2023'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Dummy selectors, these need to be updated based on actual page structure
    movies = soup.find_all('div', class_='movie_container')  # Update this selector based on actual HTML structure
    movie_data = []

    for movie in movies:
        name = movie.find('span', class_='movie_title').get_text()  # Update selectors
        duration = movie.find('span', class_='movie_duration').get_text()  # Update selectors
        type_ = movie.find('span', class_='movie_type').get_text()  # Update selectors
        genre = movie.find('span', class_='movie_genre').get_text()  # Update selectors
        
        movie_info = {
            'Name': name,
            'Duration': duration,
            'Type': type_,
            'Genre': genre
        }
        movie_data.append(movie_info)
    
    return movie_data

# Example use
movies_2023 = extract_movie_data_for_year(2023)
print(movies_2023)
