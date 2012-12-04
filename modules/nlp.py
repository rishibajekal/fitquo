import nltk
import os
import re
from nltk.corpus import stopwords


RES_DIR = "static/resources"
WORD = re.compile(r'\w+')
STOP_WORDS = set(
            "grid6 gutenberg project alice"
            .split())


def generate_data_points(file_name, value, jump):
    data = []
    freq = get_word_features(file_name)
    for i in range(0, len(freq) / jump, jump):
        next_set = dict(sorted(freq.iteritems(), key=lambda item: -item[1])[i:i + jump])
        print next_set
        data.append((next_set, value))
    next_set = dict(sorted(freq.iteritems(), key=lambda item: -item[1])[i:])
    data.append((next_set, value))
    return data


def get_word_features(file_name):
    freq = dict()
    with open(os.path.join(RES_DIR, file_name), "rU") as f:
        for sentence in f.readlines():
            for word in re.findall(WORD, sentence):
                if is_useful_word(word.lower()):
                    freq[word.lower()] = True
    return freq


def is_useful_word(word):
    return (len(word) > 3 and
            word not in STOP_WORDS and
            word not in stopwords.words("english") and
            word[1:] not in stopwords.words("english"))


if __name__ == "__main__":
    positive = generate_data_points("fitness.txt", "pos", 5)
    negative = generate_data_points("alice.txt", "neg", 5)

    neg_cutoff = len(negative) * 3 / 4
    pos_cutoff = len(positive) * 3 / 4

    train_features = negative[:neg_cutoff] + positive[:pos_cutoff]
    test_features = negative[neg_cutoff:] + positive[pos_cutoff:]

    print "Train on %d instances. Test on %d instances." % (len(train_features), len(test_features))
    classifier = nltk.NaiveBayesClassifier.train(train_features)
    print "Accuracy: ", nltk.classify.util.accuracy(classifier, test_features)
    classifier.show_most_informative_features()
