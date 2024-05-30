import re
def extract_movie_type(entry: str) -> str:
    """Extract the type of the movie from the entry

    Args:
        entry (str): the entry from which to extract the type

    Returns:
        str: the type of the movie
    """
    types = ["Feature Film", "Short Film", "Documentary", "TV Movie"]
    for movie_type in types:
        if movie_type in entry:
            return movie_type
    return "Unknown"


def extract_duration_period(entry: str) -> tuple:
    """Extract the duration of the movie from the entry

    Args:
        entry (str): the entry from which to extract the duration

    Returns:
        tuple: the duration of the movie
    """
    match = re.search(r'(\d+)\s*min', entry)
    if match:
        return int(match.group(1))
    return 0


def extract_name(entry: str, movie_type="Unknown") -> str:
    """Extract the name of the movie from the entry
    
    Args:
        entry (str): the entry from which to extract the name
        movie_type (str): the type of the movie
        
    Returns:
        str: the name of the movie
    """
    name = entry.split(movie_type)[0].split('(')[0].strip()
    return name


def extract_genre(entry: str) -> str:
    """Extract the genre of the movie from the entry
    
    Args:
        entry (str): the entry from which to extract the genre
        
    Returns:
        str: the genre of the movie
    """
    genres = ["Action", "Comedy", "Drama", "Horror", "Romance", "Thriller", "Sci-Fi", "Documentary"]
    found_genres = []
    for genre in genres:
        if genre.lower() in entry.lower():
            found_genres.append(genre)
    return ", ".join(found_genres) if found_genres else "Unknown"
