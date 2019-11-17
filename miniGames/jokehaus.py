import json
import random
import discord


import Bot


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


def roll():
    mins = 1
    maxs = 20

    diceroll = random.randint(mins, maxs)
    return diceroll

def get_maze():
    get_mazeintro()
    return

def get_mazeintro():
    with open('../sys_reqs/maze.json', 'r') as infile:
        intros = json.load(infile)

    mintro = []

    for titles in intros['intro']:
       # print(titles['title'])
        intro_title = titles['title']
        mintro.append(intro_title)

    for stories in intros['intro']:
        #print(stories['story'])
        intro_story = stories['story']
        mintro.append(intro_story)

    for options in intros['intro']:
        #print(options['option1'])
        #print(options['option2'])
        intro_option1 = options['option1']
        intro_option2 = options['option2']
        mintro.append(intro_option1)
        mintro.append(intro_option2)

    for paths in intros['intro']:
        intro_path1 = paths['path1']
        intro_path2 = paths['path2']
        mintro.append(intro_path1)
        mintro.append(intro_path2)

    # global intro_title, intro_story, intro_option1, intro_option2
    #
    # embed = discord.Embed(
    #     title="Maze!", colour=discord.Colour.dark_green()
    # )
    # embed.add_field(name=intro_title, value=intro_story)
    # embed.add_field(name=" ", value=intro_option1)
    # embed.add_field(name=" ", value=intro_option2)

    mazeintro = "Title:" + mintro[0] + '\n' + "Story: " + mintro[1] + "Options" + "\n\n" + mintro[2] + "     " + mintro[3]

    chanel = message.channel

        #  if discord.message.content == "!Left":
        #     MyClient.message.channel.send(mintro[5])
        #     get_hr1()
        # else:
        #     discord.channel.send("You hear a boulder")

    return mazeintro


def get_hr1():
    with open('../sys_reqs/maze.json', 'r') as infile:
        hr1s = json.load(infile)
        mhr1 = []

    for titles in hr1s['hr1']:
        hr1_title = titles['title']
        mhr1.append(hr1_title)

    for stories in hr1s['hr1']:
        hr1_story = stories['story']
        mhr1.append(hr1_story)

    for options in hr1s['hr1']:
        hr1_option1 = options['option1']
        hr1_option2 = options['option2']
        mhr1.append(hr1_option1)
        mhr1.append(hr1_option2)

    for paths in hr1s['hr1']:
        hr1_path1 = paths['path1']
        hr1_path2 = paths['path2']
        mhr1.append(hr1_path1)
        mhr1.append(hr1_path2)



    return mhr1

def get_hl2():
    with open('../sys_reqs/maze.json', 'r') as infile:
        hl2s = json.load(infile)
        mhl2 = []

    for titles in hl2s['hl2']:
        hl2_title = titles['title']
        mhl2.append(hl2_title)

    for stories in hl2s['hl2']:
        hl2_story = stories['story']
        mhl2.append(hl2_story)

    for options in hl2s['hl2']:
        hl2_option1 = options['option1']
        hl2_option2 = options['option2']
        mhl2.append(hl2_option1)
        mhl2.append(hl2_option2)

    for paths in hl2s['hl2']:
        hl2_path1 = paths['path1']
        hl2_path2 = paths['path2']
        mhl2.append(hl2_path1)
        mhl2.append(hl2_path2)



    return mhl2


def get_hl3():
    with open('../sys_reqs/maze.json', 'r') as infile:
        hl3s = json.load(infile)
        mhl3 = []

    for titles in hl3s['hl3']:
        hl3_title = titles['title']
        mhl3.append(hl3_title)

    for stories in hl3s['hl3']:
        hl3_story = stories['story']
        mhl3.append(hl3_story)

    for options in hl3s['hl3']:
        hl3_option1 = options['option1']
        hl3_option2 = options['option2']
        mhl3.append(hl3_option1)
        mhl3.append(hl3_option2)

    for paths in hl3s['hl3']:
        hl3_path1 = paths['path1']
        hl3_path2 = paths['path2']
        mhl3.append(hl3_path1)
        mhl3.append(hl3_path2)

    return mhl3


def get_hl4():
    with open('../sys_reqs/maze.json', 'r') as infile:
        hl4s = json.load(infile)
        mhl4 = []

    for titles in hl4s['hl4']:
        hl4_title = titles['title']
        mhl4.append(hl4_title)

    for stories in hl4s['hl4']:
        hl4_story = stories['story']
        mhl4.append(hl4_story)

    for options in hl4s['hl4']:
        hl4_option1 = options['option1']
        hl4_option2 = options['option2']
        mhl4.append(hl4_option1)
        mhl4.append(hl4_option2)

    for paths in hl4s['hl4']:
        hl4_path1 = paths['path1']
        hl4_path2 = paths['path2']
        mhl4.append(hl4_path1)
        mhl4.append(hl4_path2)

    return mhl4


def get_hr2():
    with open('../sys_reqs/maze.json', 'r') as infile:
        hr2s = json.load(infile)
        mhr2 = []

    for titles in hr2s['hr2']:
        hr2_title = titles['title']
        mhr2.append(hr2_title)

    for stories in hr2s['hr2']:
        hr2_story = stories['story']
        mhr2.append(hr2_story)

    for options in hr2s['hr2']:
        hr2_option1 = options['option1']
        hr2_option2 = options['option2']
        mhr2.append(hr2_option1)
        mhr2.append(hr2_option2)

    for paths in hr2s['hr2']:
        hr2_path1 = paths['path1']
        hr2_path2 = paths['path2']
        mhr2.append(hr2_path1)
        mhr2.append(hr2_path2)

    return mhr2

def get_hr3():
    with open('../sys_reqs/maze.json', 'r') as infile:
        hr3s = json.load(infile)
        mhr3 = []

    for titles in hr3s['hr3']:
        hr3_title = titles['title']
        mhr3.append(hr3_title)

    for stories in hr3s['hr3']:
        hr3_story = stories['story']
        mhr3.append(hr3_story)

    for options in hr3s['hr3']:
        hr3_option1 = options['option1']
        hr3_option2 = options['option2']
        hr3_option3 = options['option3']
        mhr3.append(hr3_option1)
        mhr3.append(hr3_option2)
        mhr3.append(hr3_option3)

    for paths in hr3s['hr3']:
        hr3_path1 = paths['path1']
        hr3_path2 = paths['path2']
        hr3_path3 = paths['path3']
        mhr3.append(hr3_path1)
        mhr3.append(hr3_path2)
        mhr3.append(hr3_path3)

    return mhr3


def get_hl5():
    with open('../sys_reqs/maze.json', 'r') as infile:
        hl5s = json.load(infile)
        mhl5 = []

    for titles in hl5s['hl5']:
        hl5_title = titles['title']
        mhl5.append(hl5_title)

    for stories in hl5s['hl5']:
        hl5_story = stories['story']
        mhl5.append(hl5_story)

    for options in hl5s['hl5']:
        hl5_option1 = options['option1']
        hl5_option2 = options['option2']
        mhl5.append(hl5_option1)
        mhl5.append(hl5_option2)

    for paths in hl5s['hl5']:
        hl5_path1 = paths['path1']
        hl5_path2 = paths['path2']
        mhl5.append(hl5_path1)
        mhl5.append(hl5_path2)

    return mhl5


def get_hr5():
    with open('../sys_reqs/maze.json', 'r') as infile:
        hr5s = json.load(infile)
        mhr5 = []

    for titles in hr5s['hr5']:
        hr5_title = titles['title']
        mhr5.append(hr5_title)

    for stories in hr5s['hr5']:
        hr5_story = stories['story']
        mhr5.append(hr5_story)

    for options in hr5s['hr5']:
        hr5_option1 = options['option1']
        hr5_option2 = options['option2']
        mhr5.append(hr5_option1)
        mhr5.append(hr5_option2)

    for paths in hr5s['hr5']:
        hr5_path1 = paths['path1']
        hr5_path2 = paths['path2']
        mhr5.append(hr5_path1)
        mhr5.append(hr5_path2)

    return mhr5


def get_hl6():
    with open('../sys_reqs/maze.json', 'r') as infile:
        hl6s = json.load(infile)
        mhl6 = []

    for titles in hl6s['hl6']:
        hl6_title = titles['title']
        mhl6.append(hl6_title)

    for stories in hl6s['hl6']:
        hl6_story = stories['story']
        mhl6.append(hl6_story)

    for options in hl6s['hl6']:
        hl6_option1 = options['option1']
        hl6_option2 = options['option2']
        mhl6.append(hl6_option1)
        mhl6.append(hl6_option2)

    for paths in hl6s['hl6']:
        hl6_path1 = paths['path1']
        hl6_path2 = paths['path2']
        mhl6.append(hl6_path1)
        mhl6.append(hl6_path2)

    return mhl6


def get_hr6():
    with open('../sys_reqs/maze.json', 'r') as infile:
        hr6s = json.load(infile)
        mhr6 = []

    for titles in hr6s['hr6']:
        hr6_title = titles['title']
        mhr6.append(hr6_title)

    for stories in hr6s['hr6']:
        hr6_story = stories['story']
        mhr6.append(hr6_story)

    for options in hr6s['hr6']:
        hr6_option1 = options['option1']
        hr6_option2 = options['option2']
        mhr6.append(hr6_option1)
        mhr6.append(hr6_option2)

    for paths in hr6s['hr6']:
        hr6_path1 = paths['path1']
        hr6_path2 = paths['path2']
        mhr6.append(hr6_path1)
        mhr6.append(hr6_path2)

    return mhr6


def get_hl7():
    with open('../sys_reqs/maze.json', 'r') as infile:
        hl7s = json.load(infile)
        mhl7 = []

    for titles in hl7s['hl7']:
        hl7_title = titles['title']
        mhl7.append(hl7_title)

    for stories in hl7s['hl7']:
        hl7_story = stories['story']
        mhl7.append(hl7_story)

    for options in hl7s['hl7']:
        hl7_option1 = options['option1']
        hl7_option2 = options['option2']
        mhl7.append(hl7_option1)
        mhl7.append(hl7_option2)

    for paths in hl7s['hl7']:
        hl7_path1 = paths['path1']
        hl7_path2 = paths['path2']
        mhl7.append(hl7_path1)
        mhl7.append(hl7_path2)

    return mhl7

def get_hl8():
    with open('../sys_reqs/maze.json', 'r') as infile:
        hl8s = json.load(infile)
        mhl8 = []

    for titles in hl8s['hl8']:
        hl8_title = titles['title']
        mhl8.append(hl8_title)

    for stories in hl8s['hl8']:
        hl8_story = stories['story']
        mhl8.append(hl8_story)

    for options in hl8s['hl8']:
        hl8_option1 = options['option1']
        hl8_option2 = options['option2']
        mhl8.append(hl8_option1)
        mhl8.append(hl8_option2)

    for paths in hl8s['hl8']:
        hl8_path1 = paths['path1']
        hl8_path2 = paths['path2']
        mhl8.append(hl8_path1)
        mhl8.append(hl8_path2)

    return mhl8

def get_door():
    with open('../sys_reqs/maze.json', 'r') as infile:
        doors = json.load(infile)
        mdoor = []

    for titles in doors['door']:
        door_title = titles['title']
        mdoor.append(door_title)

    for stories in doors['door']:
        door_story = stories['story']
        mdoor.append(door_story)

    return mdoor


if __name__ == '__main__':
    arb()
    print(get_hl4())


