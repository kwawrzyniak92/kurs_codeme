import gra, random

print("witaj w szybkiej grze!\n")
again = None
while again != "n":
    players = []
    num = gra.ask_number(question = "Podaj liczbę graczy (2 - 5):" , low = 2, high = 5)
    for i in range(num):
        name = input("Nazwa gracza: ")
        score = random.randrange(100) + 1
        player = gra.Player(name,score)
        players.append(player)

    print("Wyniki gry: ")
    for player in players:
        print(player)

    again = gra.ask_yes_no("Chcesz zagrać jeszcze raz? (t/n): ")

