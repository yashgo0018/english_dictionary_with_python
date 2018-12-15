import json, sys
from difflib import get_close_matches
from .settings import BASE_DIR

data = json.load(open(BASE_DIR + '/english_dictionary/data.json'))


def main(word):
    if word in data.keys():
        state = 1
        defination = data[word]
        return state, defination
    elif len(get_close_matches(word, data.keys(), n=1, cutoff=0.8)) == 1:
        state = 0
        related_word = get_close_matches(word, data.keys(), n=1, cutoff=0.7)[0]
        return state, related_word
    else:
        state = -1
        print('No Word Found check the word')
        return state, None


def data_keys():
    return data.keys()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        defination = main(sys.argv[1])
        if defination is not None:
            print(defination)
    else:
        print('no word given')
