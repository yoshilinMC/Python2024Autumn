class Sport:  # 1
    def __init__(self, sport, time):
        self.sport = sport
        self.time = time
        
    def play(self):
        return "Playing " + str(self.sport) + " takes " + str(self.time) + " hours."
    
class Athlete(Sport):  # 2
    # Override constructor
    def __init__(self, sport, time):
        super().__init__(sport, time)

    # Override play method
    def play(self):
        print("Athlete: ", super().play())
        
    def workout(self):
        return "Playing " + str(self.sport) + " takes " + str(self.time) + " hours."

basketball = Sport("basketball", 2)
print(basketball.play())

baseball = Sport("baseball", 4)
print(baseball.play())

import abc

class Sport(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def play(self):
        pass

class basketball(Sport):
    def play(self):
        print("Playing basketball takes 2 hours")

class baseball(Sport):
    def play(self):
        print("Playing baseball takes 4 hours")

Basketball = basketball()
Basketball.play()
Baseball = baseball()
Baseball.play()