class Person:
    def __init__(self,eye,hair):
        self.eye = eye
        self.hair = hair

    @classmethod
    def American(cls):
        return cls("blue","brown")
    @classmethod
    def Taiwanese(cls):
        return cls("black","black")
    def print(self):
        print("My eye is {} and my hair is {}".format(self.eye, self.hair))


American = Person.American()
American.print()
Taiwanese = Person.Taiwanese()
Taiwanese.print()