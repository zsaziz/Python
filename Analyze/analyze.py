from functools import *
import json

with open("tweets.json", "r") as tweet_db:
    tweets = json.load(tweet_db)


def flatten(xs):
    return reduce((lambda x, y: x + y), xs)


def difference(xs, ys):
    return list(set(xs) - set(ys)) + list(set(ys) - set(xs))


def to_text(tweets):
    return list(map(lambda x: x['content'], tweets))


def to_lowercase(tweets):
    return list(map(lambda x: {**x, **{'content':x['content'].lower()}}, tweets))


def nonempty(tweets):
    return list(filter(lambda x: len(x['content']) != 0, tweets))


def total_word_count(tweets):
    return reduce(lambda x, y: len(x['content'].split(' ')) + len(y['content'].split(' ')), tweets)


def hashtags(tweet):
    return list(filter(lambda x: x.__contains__('#'), tweet['content'].split()))


def mentions(tweet):
    return list(filter(lambda x: x.__contains__('@'), tweet['content'].split()))


def all_hashtags(tweets):
    return flatten(list(map(lambda x: hashtags(x), tweets)))


def all_mentions(tweets):
    return flatten(list(map(lambda x: mentions(x), tweets)))


def all_caps_tweets(tweets):
    return list(filter(lambda x: x['content'].isupper(), tweets))


def count_individual_words(tweets):
    alist = ' '.join(to_text(tweets)).split(' ')
    return _count_individual_words_help(alist, {})


def _count_individual_words_help(alist, adict):
    if alist == []:
        return adict
    elif adict.__contains__(alist[0]):
        return _count_individual_words_help(alist[1:], {**adict, **{alist[0]: adict.get(alist[0]) + 1}})
    else:
        return _count_individual_words_help(alist[1:], {**adict, **{alist[0]: 1}})


def count_individual_hashtags(tweets):
    alist = all_hashtags(tweets)
    return _count_individual_words_help(alist, {})


def count_individual_mentions(tweets):
    alist = all_mentions(tweets)
    return _count_individual_words_help(alist, {})


def n_most_common(n, word_count):
    return sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))[:n]

def iphone_tweets(tweets):
    return list(filter(lambda x: x['source'].__contains__('iPhone'), tweets))


def android_tweets(tweets):
    return list(filter(lambda x: x['source'].__contains__('Android'), tweets))


def average_favorites(tweets):
    avg = float(reduce(lambda x,y: x['favorites'] + y['favorites'], tweets))
    return int(round(avg/float(len(tweets)), 0))


def average_retweets(tweets):
    avg = float(reduce(lambda x,y: x['retweets'] + y['retweets'], tweets))
    return int(round(avg/float(len(tweets)), 0))


def sort_by_favorites(tweets):
    return sorted(tweets, key = lambda k: k['favorites'])


def sort_by_retweets(tweets):
    return sorted(tweets, key = lambda k: k['favorites'])


def upper_quartile(tweets):
    return tweets[int(len(tweets)*3/4)]


def lower_quartile(tweets):
    return tweets[int(len(tweets)*1/4)]


def top_quarter_by(tweets, factor):
    return tweets[int(len(tweets)*3/4):]


def bottom_quarter_by(tweets, factor):
    return tweets[0:int(len(tweets)*1/4) + 1]
