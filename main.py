"""
Projekt zaliczeniowy na potrzeby przedmiotu "Programowanie w języku Python"
Autor: Aleksandra Pisarzowska
Tytuł: Nazwa projektu
"""
import os
from time import sleep
import datetime
import csv


# Ekran powitania, ktory pokazuje podsumowanie
def welcomescreen():
    """
    TU WSTAW OPIS FUNKCJI
    :return:
    """
    print("Witaj w aplikacji monitorującej twoje wydatki")
    Print_Base_Data()


# Funkcje zarzadzajace programem

# Funkcje zarzadzajace wydatkami:
# Menu zarzadzajace wydatkami
def manage_expenses_menu():
    """
    TU WSTAW OPIS FUNKCJI
    :return:
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
    TU WSTAW OPIS FUNKCJI
    :return:
    """
    Expense = 1
    # petla zeby wprowadzac kategorie do pliku
    while Expense != "f":
        # input linijki
        Wydatek = input("Wprowadz wydatek")
        # sprawdzic czy wydatek to liczba
        # Sprawdzenie czy uzytkownik chce wprowadzic wydatek z dzisiaj
        ManageDate = input("Czy wydatek jest z dzisiaj? (0 tak)")
        if ManageDate == "0":
            ExpenseDate = datetime.date.today()
            ExpenseDate = ExpenseDate.strftime("%d.%m.%Y")

        else:
            # jezeli nie to uzytkownik wprowadza date
            print("Wprowadz date:")
            # upewnienie sie czy data jest poprawna
            try:
                DateEntry = input('Wprowadz date w formacie DD-MM-YYYY')
                day, month, year = map(int, DateEntry.split('-'))
                ExpenseDate = datetime.date(year, month, day)
                ExpenseDate = ExpenseDate.strftime("%d.%m.%Y")
            # wyswietlenie bledu
            except:
                print("Bledna data")
                insert_expenses()
        # wprowadzenie kategorii wydatkow
        Kategoria = input("Wprowadz kategorie:")
        print(ExpenseDate, Kategoria, Wydatek)
        # komunikat o bledzie
        print("Wydatki wprowadzone pomyslnie")
        sleep(2)
        # Wyswietlenie ponownie menu wydatkow
        manage_expenses_menu()


# funkcja usuwajaca wydatki
def delete_expenses():
    """
    TU WSTAW OPIS FUNKCJI
    :return:
    """
    print("xd")


# funkcja wyswietlajaca wydatki
def print_expenses():
    """
    TU WSTAW OPIS FUNKCJI
    :return:
    """
    print("xd")


# Funkcje zarzadzania kategoriami:
# Menu zarzadzajace kategoriami
def Manage_Categories_Menu():
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
    Option = input()
    if Option == "1":
        # wprowadzenie kategorii
        Insert_Category()
    elif Option == "2":
        # usuwanie kategorii
        Delete_Category()
    elif Option == "3":
        # wyswietlenie kategorii
        Print_Categories()
    elif Option == "4":
        # powrot dom menu
        main()
    elif Option != "":
        print("\n Zly wybor")
        Manage_Categories_Menu()


# Funkcje kategorii
# Wprowadzanie kategorii do pliku
def Insert_Category():
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
                if found != True:
                    file.write(category + "\n")
                # wyswietlenie komunikatu o bledzie
                else:
                    print("taka kategoria juz istnieje")
    # wyswietlenie komunikatu o pomyslnym wprowadzeniu kategorii
    print("Kategorie wprowadzone pomyslnie")
    # odczekanie 2 sekundy,zeby uzytkownik sie zapoznal z komunikatem
    sleep(2)
    # Wyswietlenie ponownie menu kategorii
    Manage_Categories_Menu()


# Usuwanie kategorii z pliku
def Delete_Category():
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
    if found == True:
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
    Manage_Categories_Menu()


# Wyswietlanie kategorii
def Print_Categories():
    """
    TU WSTAW OPIS FUNKCJI
    :return:
    """
    with open("kategorie.txt", "r") as file:
        lines = file.readlines()
        for x in lines:
            print(x)
        input("Wcisnij klawisz aby kontynuowac")
        Manage_Categories_Menu()


# Podsumowanie wydatkow jako podstawowe dane
def Print_Base_Data():
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


option = 0


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
        Manage_Categories_Menu()
    elif option == "3":
        exit()
    elif option != "":
        print("\n Zly wybor")


def main():
    """
    TU WSTAW OPIS FUNKCJI
    :return:
    """
    clear_screen()
    welcomescreen()
    while option != 3:
        menu()


main()
