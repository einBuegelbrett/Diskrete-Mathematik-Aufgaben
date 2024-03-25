alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"
, "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

monate = ["januar", "februar", "maerz", "april", "mai", "juni", "juli", "august", "september", "oktober", "november", "dezember"]

for monat in monate:
    summe = 0
    for i in range(3):
        summe += alphabet_list.index(monat[i])+1
    print(f"{monat} : {summe % 17}")