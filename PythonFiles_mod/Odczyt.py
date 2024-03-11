import codecs
import os
def OdczytanieNotatki():
    name = input("Podaj tytuł notatki: ")

    try:
        with codecs.open(os.path.join("Notes/", name + ".txt"), 'r', "utf-8") as odczyt:
            odczyt = odczyt.read()
            print(odczyt)

    except:
        print("Brak pliku o takiej nazwie!")