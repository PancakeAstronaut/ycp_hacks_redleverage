import json


def arb():
    print("")


def ban_tunnel(chat_str):
    ban_bool = check_words(inputVar=chat_str)
    return ban_bool


def check_words(inputVar):
    with open('../sys_reqs/bannedwords.json', 'r') as infile:
        banned_words = json.load(infile)

    tmp_dict = dict(banned_words['ban_responses'][0])
    banned_list = []
    ini_idx = 1
    while ini_idx < len(tmp_dict):
        banned_list.append(tmp_dict[str(ini_idx)])
        ini_idx += 1
    idx = 0
    banctr = []
    while idx < len(banned_list):
        if banned_list[idx] in inputVar:
            banctr.append(1)
        idx += 1
    if len(banctr) > 0:
        return True

    else:
        return False


if __name__ == '__main__':
    arb()
