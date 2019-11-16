import json
import random


def arb():
    print("")


def get_riddle():
    with open('../sys_reqs/riddles.json', 'r') as infile:
        riddle_list = json.load(infile)

        for x in range(1):
            riddle_idx = random.randint(1, 20)

    return riddle_list['riddle_repo'][0][str(riddle_idx)]


def get_joke():
    with open('../sys_reqs/jokehaus.json', 'r') as infile:
        joke_list = json.load(infile)

        for x in range(1):
            joke_idx = random.randint(1, 20)

    return joke_list['joke_repo'][0][str(joke_idx)]


if __name__ == '__main__':
    arb()
