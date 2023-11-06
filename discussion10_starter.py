import os
import unittest
import json


def read_json(file):
    """Reads a JSON document, decodes the file content, and returns a
    dictionary.

    Parameter:
        file (str): path to file

    Returns:
        dict: dict representations of the decoded JSON document
    """

    pass


def top_movies(rated, data):
    """Returns the top three movies on the basis of the rated specified.

    Parameters:
        rated (str): movie rating category. Example: "PG"
        data (dict): dict representations of a decoded JSON document

    Returns:
        list: top three movies in a list ranked by their imdbRating
    """
    pass

def get_longest_movie(data):
    """Returns the title of longest movie 

    Parameters: 
        data (dict): dict representations of a decoded JSON document

    Returns:
        string: the title of the longest movie
    """

    pass


def main():
    pass


class TestDiscussion11(unittest.TestCase):
    def setUp(self):
        self.movies = read_json('movies.json')

    def test_read_json(self):

        self.assertEqual(len(self.movies), 25)

    def test_top_movie(self):

        self.assertEqual(top_movies("PG",self.movies),['Coco', 'Up', 'Inside Out'])

        self.assertEqual(len(top_movies("PG-13",self.movies)), 1)

        self.assertEqual(top_movies("G",self.movies),['WALL·E', 'Toy Story', 'Toy Story 3'])

        self.assertEqual(top_movies("R",self.movies), ['Parasite', 'V for Vendetta', 'The Terminator'])

    def test_get_longest_movie(self):

        self.assertEqual(get_longest_movie(self.movies), "Inception")




if __name__ == "__main__":
    main()
    # You can comment this out to test with just the main function,
    # But be sure to uncomment it and test that you pass the unittests before you submit!
    unittest.main(verbosity=2)

