class Fight:
    def __init__(self,hp,damage,shield):
        self.hp = hp
        self.damage = damage
        self.shield = shield

    @classmethod
    def American(cls):
        return cls("10","4","1")
    @classmethod
    def Taiwanese(cls):
        return cls("5","7","2")
    def intro(self):
        print("I got {}hp of health, {}damage per hit, able to protect {}time of fatal attack".format(self.hp, self.damage, self.shield))

    def state(self):
        print("I got "+str(self.hp)+" hp of health, "+str(self.damage)+" damage per hit, able to protect "+str(self.shield)+" time of fatal attack")

    def intro(self,player):
        print("(I am "+player)

x1=10 
x2=4
x3=1
y1=5
y2=7
y3=2
P1 = Fight(x1,x2,x3)
P1.state()
P1.intro("fighter 1)")
P2 = Fight(y1,y2,y3)
P2.state()
P2.intro("fighter 2)")