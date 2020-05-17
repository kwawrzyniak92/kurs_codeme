from abc import ABC, abstractmethod

class Zwierzeta:
    def __init__(self, zwierze):
        self.zwierze = zwierze
        print("Can't speek")

class Ssak(Zwierzeta):
    def __init__(self, name):
        self.name = name
        print(F"{self.name} pije mleko")

class Czlowiek(Ssak):
    def __init__(self, c_name):
        self.c_name = c_name
        print(f"{self.c_name} only one who can speek")
class Kot(Ssak):
    def __init__(self, k_name):
        self.k_name = k_name
        print(f"{self.k_name} miau")

class Pies(Ssak):
    def __init__(self, p_name):
        self.p_name = p_name
        print(f"{self.p_name} hau")


# s = Ssak("ssak")
# c = Czlowiek("czlowiek")
# k = Kot("kot")
c = Pies("pies")
