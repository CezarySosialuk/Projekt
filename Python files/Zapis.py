import codecs
def ZapisanieNotatki():
    name = input("tytuł notatki: ")

    try:
        index = codecs.open("index.txt", "a", "utf-8")
        index.write(name + "\n")

        f = codecs.open("Notes/" + name + ".txt", 'w', "utf=8")
    except:
        print("nazwa i notatka nie mogą zawierać polskich znaków")
    else:
        note = input("twoja notatka:\n")
        try:
            f.write(note)
        except:
            print("nazwa i notatka nie mogą zawierać polskich znaków")
        else:
            print("Notatka zapisana")


