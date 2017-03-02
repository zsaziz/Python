import unittest
from analyze import *
from functools import *
import json

with open("tweets.json", "r") as tweet_db:
    tweets = json.load(tweet_db)

class TestBankAccount(unittest.TestCase):

    def test_flatten(self):
        self.assertEqual(flatten([[1,2],[3,4],[5],[6,7,8]]), [1,2,3,4,5,6,7,8])

    def test_difference(self):
        self.assertEqual([1,2,4,5], difference([1,2,3], [3,4,5]))

    def test_to_text(self):
        self.assertEqual(['a', 'b', 'c'], to_text([{'content': 'a'}, {'content': 'b'}, {'content': 'c'}]))
        #print(to_text(tweets))

    def test_to_lowercase(self):
        self.assertEqual(['a', 'b', 'c'], to_text(to_lowercase([{'content': 'A'}, {'content': 'B'}, {'content': 'C'}])))

    def test_nonempty(self):
        self.assertEqual(['a', 'b', 'c'], to_text(nonempty([{'content': 'a'}, {'content': 'b'},
                                                            {'content': 'c'}, {'content': ''}])))

    def test_hashtags(self):
        (hashtags({'content': 'hello i am #the #best'}))

    def test_all_hashtags(self):
        (all_hashtags(tweets))

    def test_count_individual_words(self):
        tweet1 = {'username': 'hello', 'content': 'Hello I am Zain'}
        tweet2 = {'content': 'Hello what is up'}
        tweet3 = {'content': 'I am America!'}
        tweet = [tweet1, tweet2, tweet3]
        self.assertEqual(11, total_word_count(tweet))


if __name__ == '__main__':
    unittest.main()