import random

class Student:

    def __init__(self, name):
       self.name = name
       self.gladness = 50
       self.progress = 0
       self.money = 10
       self.satiety = 50
       self.strong = 40
       self.energy = 80
       self.alive = True

    def to_study(self):
        print('Time to study')
        self.gladness -= 0.15
        self.progress += 3
        self.money -= 1
        self.satiety += 0.50
        self.energy -= 5

    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3
        self.satiety -= 2
        self.energy += 20

    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.progress -= 0.2
        self.money -= 2
        self.strong -= 1
        self.energy += 15
    def to_work(self):
        print('I go to work')
        self.gladness -= 5
        self.money += 18
        self.satiety -= 5
        self.strong += 3
        self.energy -= 20
    def to_eat(self):
        print('I will eat')
        self.gladness += 5
        self.money -= 6
        self.satiety += 25
        self.energy += 5

    def to_sport(self):
        print('I will do sport')
        self.gladness += 3
        self.satiety -= 8
        self.strong += 10
        self.energy -= 15

    def to_extralesson(self):
        print('I will study again')
        self.gladness -= 0.15
        self.satiety -= 0.50
        self.energy -= 3
        self.money -= 3
        self.progress += 2


    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out....")
            self.alive = False
        elif self.gladness <= 0:
            print('Dipression..')
            self.alive = True
        elif self.progress > 20:
            print('Passed externally....')
            self.alive = False
        elif self.money  < 3:
            print('No money..')
            self.alive = False
        elif self.satiety <= 0:
            print('Very hungry..')
            self.alive = True
        elif self.strong <= 20:
            print('No strong..')
            self.alive = True
        elif self.energy <=0:
            print('I am tired..')
            self.alive = False

    def end_of_day(self):
        print(f'Progress = {self.progress}')
        print(f'Gladness = {self.gladness}')
        print(f'Money = {self.money}')
        print(f'Satiety = {self.satiety}')
        print(f'Sport = {self.strong}')
        print(f'Energy = {self.energy}')

    def live(self, day):
        day =" Day " + str(day) + " of " + self.name + "Life"
        print(f'{day:=^50}')
        Live_cube = random.randint(1,7)
        if Live_cube == 1:
            self.to_study()
        elif Live_cube == 2:
            self.to_sleep()
        elif Live_cube == 3:
            self.to_chill()
        elif Live_cube == 4:
            self.to_work()
        elif Live_cube == 5:
            self.to_eat()
        elif Live_cube == 6:
            self.to_sport()
        elif Live_cube == 7:
            self.to_extralesson()
        self.end_of_day()
        self.is_alive()

nick = Student(name="John ")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)

