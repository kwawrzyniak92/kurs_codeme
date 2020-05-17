# menu wyboru opcji
def menu():
    choice = int(input("\nŻeby odgadnąć literę wciśnij 1 \n\nŻeby odgadnąć całe hasło wciśnij 2\n"))
    if choice == 1:
        letter = input("Podaj literę ")
        return letter
    elif choice == 2:
        completepass = input('Podaj całe hasło ')
        return completepass
    else:
        print('nie ma takiego wyboru')
# funkcja sprawdza czy strzał gracza jest prawidłowy
def winner_check(usergues, password):
    return usergues == password

# funcja sprawdza czy litera jest prawidłowa
def letter_check(letter, lives, password, secret):
    if letter in password:
        print("Dobrze!")
        for i in range(len(password)):
            if (password[i] == letter):
                secret[i] = letter
        return lives
    else:
        print('Błąd!')
        return lives - 1

# hashowanie hasła
def create_secret(password):
    field = list(password)
    for i in range(len(password)):
        field[i] = "_"
    return field

# menu()

# gra
def main():
    print("----------------")
    print("  GRA WISIELEC  ")
    print("----------------")
    print(
        "Gra polega na odgadnięciu hasła składającego się z liczby liter równej liczbie pól wyświetlonych na ekranie.\nMasz 10 szans na odgadnięcie hasła.\nPowodzenia! ")

    name = input("\nPodaj swoje imie ")
    password = str("programowanie")
    lives = 10

    # zamieniamy field na secret dalej zahashowane hasło jest przekazywane w secret
    secret = create_secret(password)

    while lives > 0:
        print('masz jeszcze', lives, 'szans\n')
        print(" ".join(secret))

        user_input = menu()
        if len(user_input) == 1:
            lives = letter_check(user_input, lives, password, secret)

        else:
            if winner_check(user_input, password):
                print('-----------------------------------\n   KONIEC GRY\n', name,'WYGRYWA!!! \n-----------------------------------')

                break
            else:
                print("To nie jest szukane hasło, próbuj dalej ")
                lives -= 1

    else:
        print('-----------------------------------\n   KONIEC GRY\n', name,
              ' PRZEGRYWA ;( \n-----------------------------------')

#start gry wywołujemy metode main
main()