# Will Vanderploeg
import pickle
import os
# Sorts, then saves the highscore in a binary file
def savehighscore(score, name, names, scores_list):
    try:
        high = open("Highscores.dat", "wb")
        scores_list.append(score)
        names.append(name)
        score_table_temp = {names[i]: scores_list[i] for i in range(len(names))}
        scores_list.sort(reverse=True)
        scores_table = {}
        for value in scores_list:
            for item in score_table_temp:
                if value == score_table_temp[item]:
                    scores_table[item] = value
        pickle.dump(scores_table, high)
        high.close()
        print("\nFile Saved\n")
        return scores_table

    except FileNotFoundError:
        print("File not found")

# Reads a binary file to retrieve past highscores
# It will detect if the file has nothing in it and if so, it will make a placeholder
# It will get rid of this placeholder once another real value has entered the file
def readhighscores():
    high = open("Highscores.dat", 'rb')
    try:
        score_table = pickle.load(high)
    except EOFError:
        score_table = {}
    names = list(score_table.keys())
    scores = list(score_table.values())
    if len(names) == 0:
        names.append("placeholder")
        scores.append(0)
        print("\n-No scores found-\n")
    elif len(names) != 0 and "placeholder" in names:
        delete1 = names.index("placeholder")
        delete2 = scores.index(0)
        del names[delete1]
        del scores[delete2]
    high.close()
    return names, scores


def displayscores(scores):
    os.system('cls')
    print("High Scores:")
    print("________________________")
    counter = 0
    for value in scores:
        counter += 1
        print(f"{counter}: {value} -- {scores[value]}")


def full_process(score, name):
    names, scores = Filesaver.readhighscores()
    score_table = Filesaver.savehighscore(score, name, names, scores)
    Filesaver.displayscores(score_table)




