class Person:
    def __init__(self,name,age,favoritefood):
        self.name = name
        self.age = age
        self.favoritefood = favoritefood

    def Print(self):
        print("我是 "+str(self.name)+"，今年 "+str(self.age)+" 歲，最喜歡吃 "+str(self.favoritefood))

    def print(self, content):
        print("我大喊 : "+content)

Amy = Person("Amy",15,"Apple")
Amy.Print()
Amy.print("我討厭看牙醫!")