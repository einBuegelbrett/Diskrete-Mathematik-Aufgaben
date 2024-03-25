a = input("gib das Element: ")
k = input("gib die Gruppe: ")
i = 1

while (pow(int(a), i) % int(k)) != 1:
    i += 1

print(i)
