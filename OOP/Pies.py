class Pies:
    def __init__(self,name, color, breed):
        self.name = name
        self.color = color
        self.race = breed

    def sound(self):
        print ("Hau,hau")

    obj_dog = Dog('grey', 'jamnik')

    print(obj_dog.name)
    obj_dog.sound()
