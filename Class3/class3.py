class Person:
    @staticmethod
    def work(hours):
        print("Working hours : ", hours)

amy = Person()
amy.work(8)

# ==封裝encapsulation=========================================================================================
class Student:
    def __init__(self,name):
        self.__name = name
        self.__score = {"Math":0, "Pysics":0, "Chemistry":0}
    # private method
    def __add_subject(self, subject):
        self.__score[subject] = 0
    # public method
    def set_score(self, subject, score):
        if subject not in self.__score:
            self.__add_subject = score
        self.__score[subject] = score
    def get_subject(self):
        for key in self.__score:
            print(key)

Bob = Student("Bob")
Bob.set_score("English",100)
Bob.get_subject()

# ==封裝encapsulation=========================================================================================

# 被繼承的類別 -> 父類別
class Person : # 1
    def __init__(self, name, age, ID):
        self.name = name
        self.age = age
        self.__ID = ID
    def speak(self, sentence):
        return self.name + "says" + sentence

# 繼承 Person 的類別 -> 子類別
class Athlete(Person): # 2
    # 複寫建構子
    def __init__(self, name, age, ID, height):
        super().__init__(name, age, ID)
        self.height = height
    # 複寫 speak 方法
    def speak(self, sentence):
        print("Athlete : ", super().speak(sentence)) # 2
    def workout(self):
        return "%s goes to the gym to exercise." % (self.name)
    
# ===========================================================================================================
    
import abc
 
class Member(metaclass=abc.ABCMeta):
    def __init__(self, name, level):
        self.name = name 
        self.level = level

    @abc.abstractclassmethod
    def discount(self, price):
        pass
    def buy(self, price):
        d_price = self.discount(price)
        print(self.name, "'s member level is ", self.level, "After discount : ",d_price)
    
class GoldenMember(Member):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.discount_rate = 0.9

    def discount(self, price):
        return price * self.discount_rate
    
class VIPMember(Member):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.discount_rate = 0.8
    def discount(self, price):
        return price * self.discount_rate\

John = GoldenMember("John", "Golden")
Amy = VIPMember("Amy", "VIP")
John.buy(2000)
Amy.buy(2000)