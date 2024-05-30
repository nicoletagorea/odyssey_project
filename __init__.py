from .api import app

__all__ = ["app"]

from .data_processing import extract_movie_type, extract_duration_period, extract_name, extract_genre

__all__ = ["extract_movie_type", "extract_duration_period", "extract_name", "extract_genre"]

from .scraper import fetch_movie_data_for_year

__all__ = ["fetch_movie_data_for_year"]