#zapisywanie krótkich notatek (aplikacja do zapisywania tekstu brudnopis)#

import Zapis
import Odczyt
import Yeet

AppRunning = True
while bool(AppRunning):
#menu#
    print("Zapisywanie notatek")
    print("1. Otwórz notatke")
    print("2. Napisz notatke")
#    print("3. Usuń notatke")
    mode = input("Podaj numer funkcji:")
#menu end#
    if int(mode) == 1:
        Odczyt.OdczytanieNotatki()

        AppRunning = False
        if input("Czy chcesz kontynuować? (y/n):") == 'y':
            AppRunning = True

    elif int(mode) == 2:
        Zapis.ZapisanieNotatki()

        AppRunning = False
        if input("Czy chcesz kontynuować? (y/n):") == 'y':
            AppRunning = True


#    elif int(mode) == 3:
#        Yeet.Usuniecie()

#        AppRunning = False
#        if input("Czy chcesz kontynuować? (y/n):") == 'y':
#            AppRunning = True

    else:
        print("~")
        print("Wybrano niewłaściwą opcję")
        print("~")
