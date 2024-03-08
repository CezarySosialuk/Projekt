import sys, locale
def ZapisanieNotatki():
    name = input("tytuł notatki: ")

    try:
        index = open("index.txt", "a")
        index.write(name + "\n")

        f = open("Notes/" + name + ".txt", 'w')
    except:
        print("nazwa i notatka nie mogą zawierać polskich znaków")
    else:
        note = input("twoja notatka:\n")
        try:
            f.write(note)
        except:
            print("nazwa i notatka nie mogą zawierać polskich znaków")
        else:
            index = open("index.txt", "a")

            index.write(name + "\n")

            print("Notatka zapisana")


