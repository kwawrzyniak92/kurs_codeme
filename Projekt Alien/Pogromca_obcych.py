import random
class Player:
      # Gracz w grze strzelance.

    def blast(self, enemy,):
        shot_chance = random.randrange(1, 10)
        print('Gracz razi wroga.\n')
        if shot_chance >= 3:
            enemy.die()
        else:
            enemy.survive()

class Alien:
    # """ Obcy w grze strzelance. """

    def die(self):
        print('Obcy z trudem łapie oddech, "To już koniec. Ale prawdziwie wielki koniec... \n',
              'Walczyliśmy do końca. Nie, to nie koniec. Larwy moje jednoczcie się! \n',
              'O tak one pomszczą mnie pewnego dnia... \n',
              'Żegnaj, okrutny Wszechświecie! Umieeeraaam"')
    def survive(self):
        print("Strzał był nie celny, obcy łapie i pożera gracza mlaszcząc... 'Omnomnom' \ni objedzony zasypia.")

if __name__ == '__main__':
    print('************ Śmierć Obcego ************\n')
    hero = Player()
    invader = Alien()
    hero.blast(invader)
    input('\n\nAby zakończyć program, naciśnij klawisz Enter.')