import unittest
from data_processing import extract_movie_type, extract_duration_period, extract_name, extract_genre

class TestMovieDataExtraction(unittest.TestCase):

    def test_extract_movie_type(self):
        """Function for testing the extract_movie_type function"""
        movie = {'type': 'Feature Film'}
        self.assertEqual(extract_movie_type(movie), 'Feature Film')
        
        movie = {'type': 'Short Film'}
        self.assertEqual(extract_movie_type(movie), 'Short Film')

        movie = {'type': 'Documentary'}
        self.assertEqual(extract_movie_type(movie), 'Documentary')

    def test_extract_duration_period(self):
        """Function for testing the extract_duration_period function"""
        movie = {'duration': '120 min'}
        self.assertEqual(extract_duration_period(movie), 120)
        
        movie = {'duration': '90 min'}
        self.assertEqual(extract_duration_period(movie), 90)

        movie = {'duration': '2 hours'}
        self.assertEqual(extract_duration_period(movie), 120)  # Assuming the function handles conversion

    def test_extract_name(self):
        """Function for testing the extract_name function"""
        movie = {'title': 'Inception'}
        self.assertEqual(extract_name(movie), 'Inception')
        
        movie = {'title': 'The Matrix'}
        self.assertEqual(extract_name(movie), 'The Matrix')

        movie = {'title': 'Interstellar'}
        self.assertEqual(extract_name(movie), 'Interstellar')

    def test_extract_genre(self):
        """Function for testing the extract_genre function"""
        movie = {'genre': 'Sci-Fi'}
        self.assertEqual(extract_genre(movie), 'Sci-Fi')
        
        movie = {'genre': 'Drama'}
        self.assertEqual(extract_genre(movie), 'Drama')

        movie = {'genre': 'Action'}
        self.assertEqual(extract_genre(movie), 'Action')

if __name__ == '__main__':
    unittest.main()
