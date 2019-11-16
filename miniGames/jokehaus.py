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


def get_wyr():
    with open('../sys_reqs/wyr.json', 'r') as infile:
        wyr_list = json.load(infile)

        for x in range(1):
            wyr_idx = random.randint(1, 20)
    return wyr_list['wyr_repo'][0][str(wyr_idx)]


def get_truth():
    with open('../sys_reqs/tod.json', 'r') as infile:
        truth_list = json.load(infile)

        for x in range(1):
            truth_idx = random.randint(1, 20)

        return truth_list['truth_repo'][0][str(truth_idx)]


def get_dare():
    with open('../sys_reqs/tod.json', 'r') as infile:
        dare_list = json.load(infile)

        for x in range(1):
            dare_idx = random.randint(1, 20)

        return dare_list['dare_repo'][0][str(dare_idx)]


if __name__ == '__main__':
    arb()
