class FamilyMember:
    def __init__(self,eye_color, height):
        self.eye_color = eye_color
        self.height = height

    def show_traits(self):
        print("Eye color:", self.eye_color)
        print("Height (cm):", self.height)

class Kid(FamilyMember):
    def __init__(self,name,age,eye_color, height):
        self.name = name
        self.age = age
        super().__init__(eye_color, height)

    def show_traits(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().show_traits()

    def favorite_hobby(self, hobby):
        print(self.name, "loves", hobby)

child = Kid("Shenaya", 13, "brown", 156)
child.show_traits()
child.favorite_hobby("Playing football")

print("Is Kid a subclass of FamilyMember?", issubclass(Kid, FamilyMember))