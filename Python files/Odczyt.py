def OdczytanieNotatki():
    index = open("index.txt", 'r')
    print(index.read())

    odczyt = open("Notes/" + input("który plik chcesz otworzyć: ") + ".txt", 'r')
    print(odczyt.read())
