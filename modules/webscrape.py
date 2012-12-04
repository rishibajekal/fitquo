import urllib2
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
import os

RES_DIR = "static/resources"
WORD = re.compile(r'\w+')
STOP_WORDS = set(
            "grid grid6 grid_6 pala"
            .split())

# Main function for getting strings in a website
# argv[0] = string for a url
# argv[1] = string for the class name for the div we are starting from
# argv[2] = list of strings for div classes to remove


def get_url_text(url, *args):

    soup = BeautifulSoup(urllib2.urlopen(url).read())
    result = []
    usage = """Invalid format.
            get_url_text(url, *args):
                url = string for a url
                argv[0] = string for the class or id name for the div we are starting from
                argv[1] = list of strings for div classes to remove
            """

    if len(args) >= 1:
        first_arg = args[0]
        if (first_arg != None):
            if first_arg[0:6] == "class=":
                soup = soup.find("div", {"class": first_arg[6:]})
            elif first_arg[0:3] == "id=":
                soup = soup.find("div", {"id": first_arg[3:]})
            else:
                print usage

        if len(args) >= 2:
            for i in args[1]:
                if i[0:6] == "class=":
                    for tag in soup.find_all("div", {"class": i[6:]}):
                        tag.decompose()
                elif i[0:3] == "id=":
                    remove_tag = soup.find("div", {"id": i[3:]})
                    remove_tag.decompose()
                else:
                    print usage

    for row in soup.stripped_strings:
        for word in re.findall(WORD, row):
            if is_useful_word(word):
                result.append(word.lower())

    return result


def is_useful_word(word):
    return (len(word) > 3 and
            word not in STOP_WORDS and
            word not in stopwords.words("english"))


def write_to_file(file_name, url, *args):
    text = get_url_text(url, *args)
    with open(os.path.join(RES_DIR, file_name), "a") as f:
        for word in text:
            f.write(" " + word.lower())
