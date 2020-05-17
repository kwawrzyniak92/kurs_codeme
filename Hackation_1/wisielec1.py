print("----------------")
print("  GRA WISIELEC  ")
print("----------------")
print(
    "Gra polega na odgadnięciu hasła składającego się z liczby liter równej liczbie pól wyświetlonych na ekranie.\nMasz 10 szans na odgadnięcie hasła.\nPowodzenia! ")

name = input("\nPodaj swoje imie ")
password = str("programowanie")
lives = 5
field = list(password)

# menu wyboru opcji
def menu():
    choice = int(input("\nŻeby odgadnąć literę wciśnij 1 \n\nŻeby odgadnąć całe hasło wciśnij 2 "))
    if choice == 1:
        letter = input("Podaj literę ")
        return letter
    elif choice == 2:
        completepass = input('Podaj całe hasło ')
        return completepass
    else:
        print('nie ma takiego wyboru')
# sprawdzenie czy strał gracza jest zgodny z hasłem
def winner_check(usergues):
    return usergues == password

# sprawdzenie litery
def letter_check(letter, lives):
    if letter in password:
        print("Dobrze!")
        for i in range(len(password)):
            if (password[i] == letter):
                field[i] = letter
        return lives
    else:
        print('Błąd!')
        return lives - 1

# gra
for i in range(len(password)):
    field[i] = "_"

while lives > 0:
    print('masz jeszcze', lives, 'szans\n')
    print(" ".join(field))
# wynik funkcji menu zamieniamy na zmienna userinput
    userinput = menu()
    if len(userinput) == 1:
        lives = letter_check(userinput, lives)

    else:
        if winner_check(userinput):
            print('Wygrana')
        break

else:
    print('-----------------------------------\n   KONIEC GRY\n', name,
          ' PRZEGRYWA ;( \n-----------------------------------')
