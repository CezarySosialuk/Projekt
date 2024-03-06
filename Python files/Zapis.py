def ZapisanieNotatki():

    name = input("tytuł notatki: ")

    index = open("index.txt", "a")

    index.write(name + "\n")

    f = open("Notes/" + name + ".txt", 'w')
    f.write(input("twoja notatka:\n"))

    print("Notatka zapisana")
