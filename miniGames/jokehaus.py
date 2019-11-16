import json
import random


def arb():
    print("")


def get_joke():
    with open('../sys_reqs/jokehaus.json', 'r') as infile:
        joke_list = json.load(infile)

    for x in range(1):
        joke_idx = random.randint(1, 20)

    return joke_list['joke_repo'][0][str(joke_idx)]


if __name__ == '__main__':
    arb()
