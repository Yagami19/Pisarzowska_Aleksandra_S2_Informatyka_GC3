import os
from time import sleep
import datetime
import csv


def welcomescreen():
    print("Witaj w aplikacji monitorującej twoje wydatki")
    Print_Base_Data()


# Funkcje zarzadzajace programem

#Funkcje zarzadzajace wydatkami:
# Menu zarzadzajace wydatkami
def manage_expenses_menu():
    clear_screen()
    print("\nWybierz co chcesz zrobić:")
    print(" [1] Wprowadź wydatek")
    print(" [2] Usun wydatek")
    print(" [3] Wyswietl wydatki")
    print(" [4] Wroc\n")
    option = input()
    if option == "1":
        insert_expenses()
    elif option == "2":
        delete_expenses()
    elif option == "3":
        print_expenses()
    elif option == "4":
        main()

    elif option != "":
        print("\n Zly wybor")
        manage_expenses_menu()

def insert_expenses():
    Expense = 1
    # petla zeby wprowadzac kategorie do pliku
    while Expense != "f":
        # input linijki
        Wydatek = input("Wprowadz wydatek")
        #sprawdzic czy wydatek to liczba

        ManageDate = input("Czy wydatek jest z dzisiaj? (0 tak)")
        if ManageDate == "0":
            ExpenseDate = datetime.date.today()
            ExpenseDate = ExpenseDate.strftime("%d.%m.%Y")

        else:
            print("Wprowadz date:")
            try:
                DateEntry = input('Wprowadz date w formacie DD-MM-YYYY')
                day, month, year = map(int, DateEntry.split('-'))
                ExpenseDate = datetime.date(year, month, day)
                ExpenseDate = ExpenseDate.strftime("%d.%m.%Y")
            except:
                print("Bledna data")
                insert_expenses()
        Kategoria = input("Wprowadz kategorie:")
        print(ExpenseDate, Kategoria, Wydatek)

        print("Wydatki wprowadzone pomyslnie")
        sleep(2)
        # Wyswietlenie ponownie menu wydatkow
        manage_expenses_menu()

def delete_expenses():
    print("xd")

def print_expenses():
    print("xd")

#Funkcje zarzadzania kategoriami:
# Menu zarzadzajace kategoriami
def Manage_Categories_Menu():
    #Czyszczenie ekranu
    clear_screen()
    #wyswietlanie opcji menu
    print("\nWybierz co chcesz zrobić:")
    print(" [1] Wprowadź kategorie")
    print(" [2] Usun kategorie")
    print(" [3] Wyswietl kategorie")
    print(" [4] Wroc\n")
    #Uzycie funkcji w zaleznosci od wyboru uzytkownika
    Option = input()
    if Option == "1":
        #wprowadzenie kategorii
        Insert_Category()
    elif Option == "2":
        #usuwanie kategorii
        Delete_Category()
    elif Option == "3":
        #wyswietlenie kategorii
        Print_Categories()
    elif Option == "4":
        #powrot dom menu
        main()
    elif Option != "":
        print("\n Zly wybor")
        Manage_Categories_Menu()


# Funkcje kategorii
# Wprowadzanie kategorii do pliku
def Insert_Category():
    category = 1
    # petla zeby wprowadzac kategorie do pliku
    while category != "0":
        # input linijki
        category = input("Wprowadz kategorie: (0 aby zakonczyc wprowadzanie)\n")
        if category != "0":
            with open("kategorie.txt", "r") as file:
                lines = file.readlines()
                found = any(x == category + "\n" for x in lines)
            with open("kategorie.txt", "a") as file:
                if found != True:
                    file.write(category + "\n")
                else:
                    print("taka kategoria juz istnieje")

    print("Kategorie wprowadzone pomyslnie")
    sleep(2)
    # Wyswietlenie ponownie menu kategorii
    Manage_Categories_Menu()


# Usuwanie kategorii z pliku
def Delete_Category():
    category: str = input("Podaj nazwe kategorii: \n")
    with open("kategorie.txt", "r") as file:
        lines = file.readlines()
        found = any(x == category+"\n" for x in lines)
    if found==True:
        with open("kategorie.txt", "w") as file:
            for line in lines:
                if line.strip("\n") != category:
                    file.write(line)
        print("kategoria usunieta pomyslnie")
    else:
        print("nie ma takiej kategorii")
    sleep(2)
    Manage_Categories_Menu()

#Wyswietlanie kategorii

def Print_Categories():
    with open("kategorie.txt", "r") as file:
        lines = file.readlines()
        for x in lines:
            print(x)
        input("Wcisnij klawisz aby kontynuowac")
        Manage_Categories_Menu()


# Podsumowanie wydatkow jako podstawowe dane
def Print_Base_Data():
    print("Wydatki za wczoraj: Wydatki za dzisiaj: Wydatki za poprzedni miesiac: Wydatki za poprzedni rok: ")


# Wyczyszczenie ekranu
def clear_screen():
    # Zamiennik wyczyszczenia dla pycharma
    print('\n' * 80)
    # Wyczyszczenie dla terminala w linuxie lub Windowsie
    os.system('cls')


option = 0


def menu():
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
    clear_screen()
    welcomescreen()
    while option != 3:
        menu()

 
main()
