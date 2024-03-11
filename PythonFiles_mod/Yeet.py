import os
def Usuniecie():
    print("Lista notatek: ")

    index = open("index.txt", 'r')
    print(index.read())

    ToYeet = input("Który plik chcesz usunąć?")

    os.remove("Notes/" + ToYeet + ".txt")

    buffor = index.read()

    print("buffor" + buffor)

    buff2 = buffor.replace(ToYeet, " ")

    print("buff2" + buff2)

    index = open("index.txt", "w")
    index.write(buff2)

    print("Notatka usunięta.")

