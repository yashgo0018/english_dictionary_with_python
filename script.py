import json, sys
from difflib import get_close_matches

data = json.load(open('data.json'))

def main(word):
    if word in data.keys():
        defination = data[word]
    elif len(get_close_matches(word, data.keys(), n=1, cutoff=0.8)) == 1:
        related_word = get_close_matches(word, data.keys(), n=1, cutoff=0.7)[0]
        yes = input("do you mean by '%s' [Y/N]" % related_word)
        if yes.lower() == 'y':
            defination = data[related_word]
        else:
            return None
    else:
        print('No Word Found check the word')
        return None
    return defination

if __name__ == '__main__':
    if len(sys.argv) > 1:
        defination = main(sys.argv[1])
        if defination != None:
            print(defination)
    else: print('no word given')