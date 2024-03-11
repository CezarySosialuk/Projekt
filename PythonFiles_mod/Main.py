#zapisywanie krótkich notatek (aplikacja do zapisywania tekstu brudnopis)#

import Zapis
import Odczyt
import Yeet
import os

AppRunning = True
while bool(AppRunning):
#menu#
    print("Zapisywanie notatek")
    print("1. Otwórz notatkę")
    print("2. Napisz notatkę")
    print("3. Usuń notatkę (Nie wspierane)")
    print("4. Statystyki (Nie wspierane)")
    print("5. Zakończ\n")
    mode = input("Podaj numer funkcji: ")
#menu end#

    match mode:
        case "1":
            Odczyt.OdczytanieNotatki()

            if input("Czy chcesz kontynuować? (y/n): ") == 'y':
                print("\n")
                os.system("cls")
            else:
                AppRunning = False

        case "2":
            Zapis.ZapisanieNotatki()

            if input("Czy chcesz kontynuować? (y/n): ") == 'y':
                print("\n")
                os.system("cls")
            else:
                AppRunning = False

#       case "3":
#           Yeet.Usuniecie()
#
#           if input("Czy chcesz kontynuować? (y/n):") == 'n':
#               AppRunning = False

        case "5":
            if input("Czy aby na pewno chcesz wyjść? (y/n): ") == 'y':
                AppRunning = False
            else:
                print("\n")
                os.system("cls")

        case _:
            print("~")
            print("Wybrano niewłaściwą opcję!")
            print("~")
