def menu():
    choice = int(input("\nŻeby wyświetlić kontakty wciśnij 1 \n\nŻeby dodać kontakt wciśnij 2\n\nŻeby usunąć kontakt wciśnij 3\n\nŻeby zamknąć program wciśnij 4\n\n"))
    if choice == 1:
        for key, value in contacts.items():
         print(key,value)

    elif choice == 2:
            new_contactname = input('Podaj nazwę nowego kontaktu w formacie [imie.nazwisko] ')
            new_phone = input('Podaj numer telefonu nowego kontaktu ')
            contacts[new_contactname] = new_phone
            print("Poprawnie dodano nowy kontakt do listy ")
            return contacts
    elif choice == 3:
             delete_contact = input ('podaj imie i nazwisko kontaktu który chcesz usunąć w formacie [imie.nazwisko]')
             contacts.pop(delete_contact)

    elif choice == 4:
        return 
    else:
        print('niepoprawny wybór')


def main():
    print ("#######################\n    KSIĄŻKA ADRESOWA    \n#######################")
    menu()
contacts = {
    "Kamil.Wawrzyniak": 666222333,
    "Adam.Kowalski": 776555433,
    "Tony.Stark": 55443322,
    "Bruce.Wayne": 556644331,
  }

main()
