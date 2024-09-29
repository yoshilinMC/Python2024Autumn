import random

class Fight:
    def __init__(self,hp,damage,shield):
        self.hp = hp
        self.damage = damage
        self.shield = shield

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
finish = None
player = 1
while(finish!=True):
    inp = input("Player "+str(player)+"\nEnter Your Choice : ")
    if inp=="attack":
        if y1-x2>0 and y3!=0:
            y1 = y1-x2
            P2 = Fight(y1,y2,y3)
            P2.state()
        elif y1-x2<0 and y3==0:
            finish = True
            print("player "+str(player)+" win")
            break
        elif y1-x2>0 and y3>0:
            y3 = y3-1
            P2 = Fight(y1,y2,y3)
            P2.state()
    if inp=="dodge":
        if random.randint(0,3)==1:
            print("Dodged and counter attack")
            x1 = x1-x2
            P1 = Fight(x1,x2,x3)
        else:
            print("Failed")
    player+=1
    inp2 = input("Player "+str(player)+"\nEnter Your Choice : ")
    if inp2=="attack":
        if x1-y2>0 and x3!=0:
            x1 = x1-y2
            P1 = Fight(x1,x2,x3)
            P1.state()
        elif x1-y2<0 and x3==0:
            finish = True
            print("player "+str(player)+" win")
            break
        elif x1-y2>0 and x3>0:
            x3 = x3-1
            P1 = Fight(x1,x2,x3)
            P1.state()
    if inp2=="dodge":
        if random.randint(0,3)==1:
            print("Dodged and counter attack")
            y1 = y1-y2
            P1 = Fight(x1,x2,x3)
        else:
            print("Failed")
    player=1