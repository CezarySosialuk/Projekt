def ZapisanieNotatki(tytul):
    with open("Notes/" + tytul + ".txt", 'w') as f:
        f.write(input("twoja notatka:\n"))
