import nltk
import os
import re
from nltk.corpus import stopwords
from collections import defaultdict


RES_DIR = "static/resources"
WORD = re.compile(r'\w+')


def get_words(sentence):
    words = []
    for word in sentence.split(' '):
        try:
            words.append(re.match(WORD, word).group(0))
        except:
            pass
    return words


def get_rating(sentence):
    sent_dict = defaultdict(int)
    words = get_words(sentence)
    for word in words:
        if is_useful_word(word):
            sent_dict[word.lower()] += 1
    return sent_dict


def get_word_features(file_name):
    freq = defaultdict(int)
    with open(os.path.join(RES_DIR, file_name), 'rU') as f:
        for sentence in f.readlines():
            for word in re.findall(WORD, sentence):
                if is_useful_word(word.lower()):
                    freq[word.lower()] += 1
    return freq


def is_useful_word(word):
    return (len(word) > 3 and
            word not in stopwords.words('english') and
            word[1:] not in stopwords.words('english'))


if __name__ == "__main__":
    negative = [(get_word_features('alice.txt'), "neg")]
    positive = [(get_word_features('fitness.txt'), "pos")]

    print positive
    neg_cutoff = len(negative) * 3 / 4
    pos_cutoff = len(positive) * 3 / 4

    train_features = negative[:neg_cutoff] + positive[:pos_cutoff]
    test_features = negative[neg_cutoff:] + positive[pos_cutoff:]

    print "Train on %d instances. Test on %d instances." % (len(train_features), len(test_features))
    classifier = nltk.NaiveBayesClassifier.train(train_features)
    print "Accuracy: ", nltk.classify.util.accuracy(classifier, test_features)
    classifier.show_most_informative_features()
