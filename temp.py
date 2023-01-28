import random

class Student:

    def __init__(self, name):
       self.name = name
       self.gladness = 50
       self.progress = 0
       self.alive = True

    def to_study(self):
        print('Time to study')
        self.gladness += 0.15
        self.progress -= 3

    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3

    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.progress -= 0.2

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out....")
            self.alive = False
        elif self.gladness <= 0
            print('Dipression..')
            self.alive = True
        elif self.progress > 5:
            print('Passed externally....')
            self.alive = False

    def end_of_day(self):
        print(f'Progress = {self.progress}')
        print(f'Gladness = {self.gladness}')

    def live(self, day):
        day =" Day " + str(day) + " of " + self.name + "Life"
        print(f'{day:=^50}')
        Live_cube = random.randit(1,3)
        if Live_cube == 1:
            self.to_study()
        elif Live_cube == 2:
            self.to_sleep()
        elif Live_cube == 3:
            self.to_chill
        self.end_of_day()
        self.is_alive()

nick = Student(name="Nick")
    for day in range(365):
        if nick.alive == False:
            break
        nick.live(day)

