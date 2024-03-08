import codecs
def ZapisanieNotatki():
    name = input("tytuł notatki: ")

    try:
        index = codecs.open("index.txt", "a", "utf-8")
        index.write(name + "\n")

        f = codecs.open("Notes/" + name + ".txt", 'w', "utf=8")
    except:
        print("nazwa pliku ma zakazane znaki")
    else:
        note = input("twoja notatka:\n")
        try:
            f.write(note)
        except:
            print("w pliku są zakazane znaki")
        else:
            print("Notatka zapisana")


