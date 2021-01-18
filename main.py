"""
Projekt zaliczeniowy na potrzeby przedmiotu "Programowanie w języku Python"
Autor: Aleksandra Pisarzowska
Tytuł: Nazwa projektu
"""
# TODO: -sprawdzenie poprawnosci wydatku (czy float)
# TODO: -sprawdzenie poprawnosci wprowadzanej kategorii
# TODO: -export do csv
# TODO: -wyswietlanie wydatkow w tym:
#  *za dzien
#  *za miesiac
#  *za rok
#  *po konkretnej dacie
import os
import sys
from time import sleep
import datetime
import csv


# Ekran powitania, ktory pokazuje podsumowanie
def welcomescreen():
    """
    TU WSTAW OPIS FUNKCJI
    :return: null
    """
    print("Witaj w aplikacji monitorującej twoje wydatki")
    print_base_data()


# Funkcje zarzadzajace programem

# Funkcje zarzadzajace wydatkami:
# Menu zarzadzajace wydatkami
def manage_expenses_menu():
    """
    Funkcja obsługująca menu zarządzania wydatkami
    :param option: parametr do wyboru opcji z menu
    :return: null
    """
    # wyczyszenie ekranu
    clear_screen()
    # Wyswietlenie opcji menu
    print("\nWybierz co chcesz zrobić:")
    print(" [1] Wprowadź wydatek")
    print(" [2] Usun wydatek")
    print(" [3] Wyswietl wydatki")
    print(" [4] Wroc\n")
    # Wprowadzenie danych przez uzytkownika
    option = input()
    if option == "1":
        insert_expenses()
    elif option == "2":
        delete_expenses()
    elif option == "3":
        print_expenses()
    elif option == "4":
        main()
    # komunikat o bledzie
    elif option != "":
        print("\n Zly wybor")
        manage_expenses_menu()


def insert_expenses():
    """
    Funkcja dodawania wyudatków
    :return:
    """
    expense = 1
    # petla zeby wprowadzac kategorie do pliku
    while expense != "f":
        # input linijki
        expense = input("Wprowadz wydatek")
        # sprawdzic czy wydatek to liczba
        # Sprawdzenie czy uzytkownik chce wprowadzic wydatek z dzisiaj
        manage_date = input("Czy wydatek jest z dzisiaj? (0 tak)")
        if manage_date == "0":
            expense_date = datetime.date.today()
            expense_date = expense_date.strftime("%d.%m.%Y")

        else:
            # jezeli nie to uzytkownik wprowadza date
            print("Wprowadz date:")
            # upewnienie sie czy data jest poprawna
            try:
                date_entry = input('Wprowadz date w formacie DD-MM-YYYY')
                day, month, year = map(int, date_entry.split('-'))
                expense_date = datetime.date(year, month, day)
                expense_date = expense_date.strftime("%d.%m.%Y")
            # wyswietlenie bledu
            except ValueError:
                print("Bledna data")
                insert_expenses()
        # wprowadzenie kategorii wydatkow
        # TODO: Wybieramy kategorie (1-n) z zapisanych w pliku
        filesize = os.path.getsize("sample.txt")

        if filesize == 0:

            print("Plik z kategoriami jest pusty")

        else:
            with open("kategorie.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    print(line)
                category = input("Wprowadz numer kategorii:")
                try:
                    category=lines[input-1]
                except:
                        print("podaj poprawny numer kategorii")
                        insert_expenses()
        save_expense_to_csv(expense_date, category, expense)
        # komunikat o bledzie
        print("Wydatki wprowadzone pomyslnie")
        sleep(2)
        # Wyswietlenie ponownie menu wydatkow
        manage_expenses_menu()


# funkcja usuwajaca wydatki
def delete_expenses():
    """
    Funkcja usuwająca wydatki
    :return:
    """
    print("xd")


def save_expense_to_csv(expense_date, category, expense):
    """
    Funkcja zapisująca wydatki do pliku wydatki.csv
    :param expense_date: Data wydatku
    :param kategoria: Kategoria wydatku
    :param wydatek: Kwota wydatku
    :return: NULL
    """
    row_value = [expense_date, category, expense]
    with open('wydatki.csv', 'a',newline='', encoding='utf-8') as wydatki_csv:
        writer = csv.writer(wydatki_csv)
        writer.writerow(row_value)


# funkcja wyswietlajaca wydatki
def print_expenses():
    """
    TU WSTAW OPIS FUNKCJI
    :return:
    """
    print("xd")


# Funkcje zarzadzania kategoriami:
# Menu zarzadzajace kategoriami
def manage_categories_menu():
    """
    TU WSTAW OPIS FUNKCJI
    :return:
    """
    # Czyszczenie ekranu
    clear_screen()
    # wyswietlanie opcji menu
    print("\nWybierz co chcesz zrobić:")
    print(" [1] Wprowadź kategorie")
    print(" [2] Usun kategorie")
    print(" [3] Wyswietl kategorie")
    print(" [4] Wroc\n")
    # Uzycie funkcji w zaleznosci od wyboru uzytkownika
    option = input()
    if option == "1":
        # wprowadzenie kategorii
        insert_category()
    elif option == "2":
        # usuwanie kategorii
        delete_category()
    elif option == "3":
        # wyswietlenie kategorii
        print_categories()
    elif option == "4":
        # powrot dom menu
        main()
    elif option != "":
        print("\n Zly wybor")
        manage_categories_menu()


# Funkcje kategorii
# Wprowadzanie kategorii do pliku
def insert_category():
    """
    TU WSTAW OPIS FUNKCJI
    :return:
    """
    category = 1
    # petla zeby wprowadzac kategorie do pliku
    while category != "0":
        # wprowadzenie kategorii przez uzytkownika
        category = input(
            "Wprowadz kategorie: (0 aby zakonczyc wprowadzanie)\n")
        if category != "0":
            # otwarcie pliku i zapisanie kategorii do zmiennej
            with open("kategorie.txt", "r") as file:
                lines = file.readlines()
                # sprawdzenie czy kategoria istnieje
                found = any(x == category + "\n" for x in lines)
            with open("kategorie.txt", "a") as file:
                # jezeli nie to dopisanie kategorii
                if found is not True:
                    file.write(category + "\n")
                # wyswietlenie komunikatu o bledzie
                else:
                    print("taka kategoria juz istnieje")
    # wyswietlenie komunikatu o pomyslnym wprowadzeniu kategorii
    print("Kategorie wprowadzone pomyslnie")
    # odczekanie 2 sekundy,zeby uzytkownik sie zapoznal z komunikatem
    sleep(2)
    # Wyswietlenie ponownie menu kategorii
    manage_categories_menu()


# Usuwanie kategorii z pliku
def delete_category():
    """
    TU WSTAW OPIS FUNKCJI
    :return:
    """
    # uzytkownik podaje kategorie
    category: str = input("Podaj nazwe kategorii: \n")
    # otwarcie pliku,
    with open("kategorie.txt", "r") as file:
        lines = file.readlines()
        found = any(x == category + "\n" for x in lines)
    # sprawdzenie czy kategoria istnieje
    if found is True:
        with open("kategorie.txt", "w") as file:
            for line in lines:
                # nadpisanie pliku bez podanej kategorii
                if line.strip("\n") != category:
                    file.write(line)
        # wyswietlenie komunikatu o poprawnym usunieciu kategorii
        print("kategoria usunieta pomyslnie")
    else:
        # wyswietlenie komunikatu o bledzie
        print("nie ma takiej kategorii")
    # odczekanie 2 sekundy,zeby uzytkownik sie zapoznal z komunikatem
    sleep(2)
    # ponowne wyswietlenie menu kategorii
    manage_categories_menu()


# Wyswietlanie kategorii
def print_categories():
    """
    TU WSTAW OPIS FUNKCJI
    :return:
    """
    with open("kategorie.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line)
        input("Wcisnij klawisz aby kontynuowac")
        manage_categories_menu()


# Podsumowanie wydatkow jako podstawowe dane
def print_base_data():
    """
    TU WSTAW OPIS FUNKCJI
    :return:
    """
    print(
        "Wydatki za wczoraj: Wydatki za dzisiaj: "
        "Wydatki za poprzedni miesiac: Wydatki za poprzedni rok: ")


# Wyczyszczenie ekranu
def clear_screen():
    """
    TU WSTAW OPIS FUNKCJI
    :return:
    """
    # Zamiennik wyczyszczenia dla pycharma
    print('\n' * 80)
    # Wyczyszczenie dla terminala w linuxie lub Windowsie
    os.system('cls')


def menu():
    """
    TU WSTAW OPIS FUNKCJI
    :return:
    """
    print("\nWybierz co chcesz zrobić:")
    print(" [1] Wprowadź wydatki")
    print(" [2] Zarządzaj kategoriami")
    print(" [3] Wyswietl dane")
    print(" [4] Zakoncz program\n")
    option = input()
    if option == "1":
        manage_expenses_menu()
    elif option == "2":
        manage_categories_menu()
    elif option == "3":
        sys.exit(0)
    elif option != "":
        print("\n Zly wybor")


def main():
    """
    TU WSTAW OPIS FUNKCJI
    :param option: parametr wyboru menu
    :return: NULL
    """
    option = 0
    clear_screen()
    welcomescreen()
    while option != 3:
        menu()

