#zapisywanie krótkich notatek (aplikacja do zapisywania tekstu brudnopis)

InMenu = True
while(bool(InMenu)):

    print("Zapisywanie notatek")
    print("1. Otwórz notatke")
    print("2. Napisz notatke")
    print("3. Usuń notatke")
    mode = input("Podaj numer funkcji:")

    if (int(mode) == 1):
        print("tutaj pokazanie listy notatek")
        InMenu = False
    elif (int(mode) == 2):
        print("tutaj zapisywanie nowej notatki")
        InMenu = False
    elif (int(mode) == 3):
        print("tutaj usuwanie notatek")
        InMenu = False
    else:
        print("~")
        print("Wybrano niewłaściwą opcję")
        print("~")

#with open("Notes/note1.txt", 'w') as f:
#    f.write('doda czy usunie')
