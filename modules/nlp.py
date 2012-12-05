import nltk
import os
import re
from nltk.corpus import stopwords


RES_DIR = "static/resources"
WORD = re.compile(r'\w+')
STOP_WORDS = set(
            "grid6 gutenberg project alice leaves"
            .split())


def get_classifier():
    fitness = create_data_points("fitness.txt", "pos")
    alice = create_data_points("alice.txt", "neg")
    curse = create_data_points("curse.txt", "neg")

    train_features = fitness + alice + curse
    classifier = nltk.NaiveBayesClassifier.train(train_features)
    return classifier


def create_data_points(file_name, value):
    return list(({word: count}, value) for word, count in generate_word_freq_from_file(file_name).items())


def get_features(file_name, value, jump):
    data = []
    freq = generate_word_freq_from_file(file_name)
    for i in range(0, len(freq) / jump, jump):
        next_set = dict(sorted(freq.iteritems(), key=lambda item: -item[1])[i:i + jump])
        data.append((next_set, value))
    next_set = dict(sorted(freq.iteritems(), key=lambda item: -item[1])[i * jump:])
    data.append((next_set, value))
    return data


def generate_word_freq_from_file(file_name):
    freq = dict()
    with open(os.path.join(RES_DIR, file_name), "rU") as f:
        for sentence in f.readlines():
            for word in re.findall(WORD, sentence):
                if is_useful_word(word.lower()):
                    freq[word.lower()] = True
    return freq


def generate_word_freq(string):
    freq = dict()
    for word in re.findall(WORD, string):
        freq[word] = True
    return freq


def is_useful_word(word):
    return (word not in STOP_WORDS and
            word not in stopwords.words("english"))


def test():
    classifier = get_classifier()
    pos_sent = "weight-loss backache headache?"
    neg_sent = "blah this is useless rabbit?"

    print "Classification for '" + pos_sent + "': ", classifier.classify(generate_word_freq(pos_sent))
    print "Classification for '" + neg_sent + "': ", classifier.classify(generate_word_freq(neg_sent))


if __name__ == "__main__":
    test()
