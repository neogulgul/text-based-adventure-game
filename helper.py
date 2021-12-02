from main import *

def clear_screen():
    os.system('cls')

def typing(message):
    time.sleep(0.5)
    for char in message:
        if char in [",", ".", "!", "?"]:
            print(char, end = "", flush = True)
            time.sleep(0.5)
        else:
            print(char, end = "", flush = True)
            time.sleep(random.choice([0.02, 0.03, 0.04, 0.05]))
    time.sleep(1)
    print("")

def a_or_an(word):
    if word[0].lower() in ["a", "e", "i", "o", "u", "y"]:
        return "an"

    return "a"

def s_or_no_s(dmg):
    if dmg == 1:
        return "" # no s :(

    return "s" # s :)