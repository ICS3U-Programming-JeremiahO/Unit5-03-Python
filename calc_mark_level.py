# !/user/bin/env.python3
# Created By: Jeremiah omoike
# Date: Nov. 28, 2022
# This program


def calc_mark(level):
    levels = {
        "4+": "Level {} has an average of 98%".format(level),
        "4": "Level {} has an average of 91%".format(level),
        "4-": "Level {} has an average of 83%".format(level),
        "3+": "Level {} has an average of of 78%".format(level),
        "3": "Level {} has an average of 75%".format(level),
        "3-": "Level {} has an average of 71%".format(level),
        "2+": "Level {} has an average of 68%".format(level),
        "2": "Level {} has an average of 65%".format(level),
        "2-": "Level {} has an average of 61%".format(level),
        "1+": "Level {} has an average of 58%".format(level),
        "1": "Level {} has an average of 55%".format(level),
        "1-": "Level {} has an average of 51%".format(level),
        "R": "Level {} has an average of 25%".format(level),
    }
    return levels.get(level, -1)


# this function gets input from the user
# and calls the next function
def main():

    # gets input from the user
    level_user = input(" Enter a Level to convert to a percentage: ")
    print("")

    # assigns variable to function call that gives return value
    percent = calc_mark(level_user)

    # displays error if user inputs an invalid mark to user
    if calc_mark(level_user) == -1:
        print("{} is not a valid mark.".format(level_user))
    else:
        print(percent)


if __name__ == "__main__":
    main()
