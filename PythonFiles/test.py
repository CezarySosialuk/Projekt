"""
Plik testy.py zawiera kompleksowe testy jednostkowe dla aplikacji notatnika.
"""

import unittest
import os
import sys
from unittest.mock import patch

import FilesList
import DEV
import Fav
import Odczyt
import Yeet
import Zapis
import Main

class TestFilesList(unittest.TestCase):
    def setUp(self):
        if not os.path.exists("Notes"):
            os.makedirs("Notes")
        with open("Notes/test_note.txt", "w", encoding="utf-8") as f:
            f.write("Testowa notatka")
    
    def tearDown(self):
        if os.path.exists("Notes/test_note.txt"):
            os.remove("Notes/test_note.txt")
        if os.path.exists("Notes/test_fav.f.txt"):
            os.remove("Notes/test_fav.f.txt")
        if len(os.listdir("Notes")) == 0:
            os.rmdir("Notes")
    
    @patch('builtins.print')
    def test_wypisz_spis_plikow(self, mock_print):
        FilesList.wypisz_spis_plikow()
        self.assertTrue(mock_print.called)
    
    @patch('builtins.print')
    def test_wypisz_ulubione(self, mock_print):
        FilesList.wypisz_ulubione()
        mock_print.assert_called_with("Brak ulubionych notatek. ")
        
        with open("Notes/test_fav.f.txt", "w", encoding="utf-8") as f:
            f.write("Ulubiona notatka")
        FilesList.wypisz_ulubione()
        self.assertTrue(mock_print.call_count > 1)

class TestMain(unittest.TestCase):
    @patch('builtins.input', return_value='9')
    def test_main_exit(self, mock_input):
        with self.assertRaises(SystemExit):
            Main.AppRunning = True
            Main.main()
    
    @patch('builtins.input', side_effect=['1', 'test_note', 'Testowa notatka', 'y', '9'])
    @patch('builtins.print')
    def test_main_flow(self, mock_print, mock_input):
        with self.assertRaises(SystemExit):
            Main.AppRunning = True
            Main.main()
        self.assertTrue(mock_print.called)

class TestOdczyt(unittest.TestCase):
    def setUp(self):
        if not os.path.exists("Notes"):
            os.makedirs("Notes")
        with open("Notes/test_note.txt", "w", encoding="utf-8") as f:
            f.write("Testowa notatka")
    
    def tearDown(self):
        if os.path.exists("Notes/test_note.txt"):
            os.remove("Notes/test_note.txt")
        if len(os.listdir("Notes")) == 0:
            os.rmdir("Notes")
    
    @patch('builtins.input', return_value='test_note')
    @patch('builtins.print')
    def test_odczytanie_notatki(self, mock_print, mock_input):
        Odczyt.odczytanie_notatki()
        mock_print.assert_any_call("Testowa notatka")
    
    @patch('builtins.input', return_value='nieistniejacy_plik')
    @patch('builtins.print')
    def test_odczytanie_notatki_error(self, mock_print, mock_input):
        Odczyt.odczytanie_notatki()
        self.assertTrue("Wystąpił błąd" in str(mock_print.call_args_list))

class TestYeet(unittest.TestCase):
    def setUp(self):
        if not os.path.exists("Notes"):
            os.makedirs("Notes")
        with open("Notes/test_note.txt", "w", encoding="utf-8") as f:
            f.write("Testowa notatka")
    
    def tearDown(self):
        if os.path.exists("Notes/test_note.txt"):
            os.remove("Notes/test_note.txt")
        if len(os.listdir("Notes")) == 0:
            os.rmdir("Notes")
    
    @patch('builtins.print')
    def test_remove(self, mock_print):
        Yeet.remove("test_note")
        mock_print.assert_called_with("Notatka o nazwie test_note.txt została pomyślnie usunięta.")
        self.assertFalse(os.path.exists("Notes/test_note.txt"))
    
    @patch('builtins.print')
    def test_remove_nonexistent(self, mock_print):
        Yeet.remove("nieistniejacy_plik")
        self.assertTrue("Wystąpił błąd" in str(mock_print.call_args_list))

class TestZapis(unittest.TestCase):
    def setUp(self):
        if os.path.exists("Notes"):
            for file in os.listdir("Notes"):
                os.remove(os.path.join("Notes", file))
            os.rmdir("Notes")
    
    def tearDown(self):
        if os.path.exists("Notes"):
            for file in os.listdir("Notes"):
                os.remove(os.path.join("Notes", file))
            os.rmdir("Notes")
    
    @patch('builtins.input', side_effect=['test_note', 'Testowa notatka'])
    @patch('builtins.print')
    def test_zapisanie_notatki(self, mock_print, mock_input):
        Zapis.zapisanie_notatki()
        self.assertTrue(os.path.exists("Notes/test_note.txt"))
        mock_print.assert_called_with("\nNotatka zapisana.")
    
    @patch('builtins.input', side_effect=['test_note', 'Testowa notatka', 'test_note', ''])
    @patch('builtins.print')
    def test_zapisanie_notatki_duplicate(self, mock_print, mock_input):
        Zapis.zapisanie_notatki()
        Zapis.zapisanie_notatki()
        mock_print.assert_any_call("Error: Plik o takiej nazwie już istnieje.")

class TestDEV(unittest.TestCase):
    def setUp(self):
        if os.path.exists("Notes/Lorem.txt"):
            os.remove("Notes/Lorem.txt")
        if os.path.exists("Notes") and len(os.listdir("Notes")) == 0:
            os.rmdir("Notes")
    
    def tearDown(self):
        if os.path.exists("Notes/Lorem.txt"):
            os.remove("Notes/Lorem.txt")
        if os.path.exists("Notes") and len(os.listdir("Notes")) == 0:
            os.rmdir("Notes")
    
    @patch('builtins.print')
    def test_lorem_note(self, mock_print):
        DEV.lorem_note()
        self.assertTrue(os.path.exists("Notes/Lorem.txt"))
        mock_print.assert_called_with("Plik 'Lorem.txt' został pomyślnie utworzony.")
    
    def test_note_stats(self):
        if not os.path.exists("Notes"):
            os.makedirs("Notes")
        with open("Notes/test_stats.txt", "w", encoding="utf-8") as f:
            f.write("12345")
        result = DEV.note_stats("test_stats.txt")
        self.assertEqual(result, 5)
        os.remove("Notes/test_stats.txt")
    
    def test_note_time(self):
        if not os.path.exists("Notes"):
            os.makedirs("Notes")
        with open("Notes/test_time.txt", "w", encoding="utf-8") as f:
            f.write("Test")
        result = DEV.note_time("test_time.txt")
        self.assertIsNotNone(result)
        os.remove("Notes/test_time.txt")

class TestFav(unittest.TestCase):
    def setUp(self):
        if not os.path.exists("Notes"):
            os.makedirs("Notes")
        with open("Notes/test_note.txt", "w", encoding="utf-8") as f:
            f.write("Testowa notatka")
    
    def tearDown(self):
        if os.path.exists("Notes/test_note.txt"):
            os.remove("Notes/test_note.txt")
        if os.path.exists("Notes/test_note.f.txt"):
            os.remove("Notes/test_note.f.txt")
        if len(os.listdir("Notes")) == 0:
            os.rmdir("Notes")
    
    @patch('builtins.input', return_value='test_note')
    @patch('FilesList.wypisz_spis_plikow')
    def test_favourite(self, mock_wypisz, mock_input):
        Fav.favourite()
        self.assertTrue(os.path.exists("Notes/test_note.f.txt"))
        Fav.favourite()
        self.assertTrue(os.path.exists("Notes/test_note.txt"))
    
    def test_is_fav(self):
        self.assertTrue(Fav.is_fav("test.f.txt"))
        self.assertFalse(Fav.is_fav("test.txt"))

if __name__ == '__main__':
    # Utwórz folder Notes jeśli nie istnieje
    if not os.path.exists("Notes"):
        os.makedirs("Notes")
    
    # Uruchom testy
    unittest.main(exit=False)
    
    # Posprzątaj po testach
    if os.path.exists("Notes"):
        for file in os.listdir("Notes"):
            if file not in ['.gitkeep', '.gitignore']:  # Zachowaj specjalne pliki git
                os.remove(os.path.join("Notes", file))
        if len(os.listdir("Notes")) <= 2:  # Jeśli tylko pliki git
            os.rmdir("Notes")