import codecs
import os
def ZapisanieNotatki():
    name = input("Podaj tytuł notatki: ")

    try:
        # Sprawdź, czy folder "Notes" istnieje, jeśli nie, utwórz go
        if not os.path.exists("Notes"):
            os.makedirs("Notes")

        with codecs.open(os.path.join("Notes/", name + ".txt"), 'w', "utf-8") as f:
            print("Utworzono nowy plik notatki o nazwie:", name + ".txt")

    except:
        print("Nazwa pliku ma zakazane znaki!")

    else:
        note = input("Twoja notatka: \n")
        try:
            with codecs.open(os.path.join("Notes/", name + ".txt"), 'w', "utf-8") as f:
                f.write(note)
        except:
            print("W pliku są zakazane znaki!")
        else:
            print("Notatka zapisana")


