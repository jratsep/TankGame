from random import randint
import main_functions as fns

directions = {'w':'up', 's':'down', 'a':'left', 'd':'right'}


class Tank:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'up'

    def __str__(self):
        return f"Current tank position is [{self.x}, {self.y}] and it is facing {self.direction}"

    def move(self, direction):
        if direction in directions.values():
            if direction == 'up':
                if self.y <5:
                    self.y += 1
                else: print("Coordinate can't be over 5")
            elif direction == 'down':
                if self.y > -5:
                    self.y -= 1
                else:
                    print("Coordinate can't be less than 5")

            elif direction == 'left':
                if self.x > -5:
                    self.x -= 1
                else:
                    print("Coordinate can't be less than 5")
            elif direction == 'right':
                if self.x < 5:
                    self.x += 1
                else:
                    print("Coordinate can't be over 5")
            self.direction = direction
        else:
            print("Not present")

    def shoot(self, targetX, targetY):
        if self.direction == 'up' or self.direction == 'down':
            if targetX == self.x:
                if targetY > self.y and self.direction == 'up':
                    return True
                elif targetY < self.y and self.direction == 'down':
                    return True
                return False





class Target:
    def __init__(self):
        self.x = randint(-5, 5)
        self.y = randint(-5, 5)

    def __str__(self):
        return f'Target position is at [{self.x}, {self.y}]'



    def reset(self):
        self.x = randint(-5, 5)
        self.y = randint(-5, 5)

tank = Tank()
target = Target()

# Making sure that that target and tank are not in the same place

while tank.x == target.x and tank.y == target.y:
    target.reset()

while True:
    main_action = fns.initial_user_input()
    if main_action == '1':
        print("Welcome to the tank game, lets GOOO!")
        while True:
            tank_move = fns.tm_input()
            if tank_move == "t":
                if tank.shoot(target.x, target.y):
                    while tank.x == target.x and tank.y == target.y:
                        target.reset()
                else:
                    print("you missed the target")
            tank.move(directions[tank_move])
            print(tank)
            print(target)
    elif main_action == '2':
        print("The previous results")
    elif main_action == '3':
        print("Getting a username")
        print("Saving the username and the score")

