#zapisywanie krótkich notatek (aplikacja do zapisywania tekstu brudnopis)#

import os
import Zapis

AppRunning = True
while bool(AppRunning):
#menu#
    print("Zapisywanie notatek")
    print("1. Otwórz notatke")
    print("2. Napisz notatke")
    print("3. Usuń notatke")
    mode = input("Podaj numer funkcji:")
#menu end#
    if int(mode) == 1:
        AppRunning = False

        index = open("index.txt", 'r')
        print(index.read())

        odczyt = open("Notes/" + input("który plik chcesz otworzyć: ") + ".txt", 'r')
        print(odczyt.read())

        if input("Czy chcesz kontynuować? (y/n):") == 'y':
            AppRunning = True

    elif int(mode) == 2:
        AppRunning = False

        name = input("tytuł notatki: ")

        index = open("index.txt", "a")
        index.write(name + "\n")

        Zapis.ZapisanieNotatki(name)

        print("Notatka zapisana")
        if input("Czy chcesz kontynuować? (y/n):") == 'y':
            AppRunning = True


    elif int(mode) == 3:
        AppRunning = False

        print("lista notatek:")

        index = open("index.txt", 'r')
        print(index.read())

        os.remove("Notes/" + input("który plik chcesz usunąć?") + ".txt")

        print("notatka usunięta")

        if input("Czy chcesz kontynuować? (y/n):") == 'y':
            AppRunning = True

    else:
        print("~")
        print("Wybrano niewłaściwą opcję")
        print("~")
