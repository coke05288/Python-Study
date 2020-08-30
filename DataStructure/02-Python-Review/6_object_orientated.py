class Car:
    def __init__(self, color, speed=10):
        self.color = color
        self.speed = speed

    def speedUp(self): self.speed += 10
    def speedDown(self): self.speed -= 10

    def __eq__(self, temp): return self.color == temp.color

    def __str__(self): return "color = %s, speed = %d" % (
        self.color, self.speed)


class SuperCar(Car):
    def __init__(self, color, speed=10, turbo=True):
        super().__init__(color, speed)
        self.turbo = turbo

    def setTurbo(self, turbo=True):
        self.turbo = turbo

    def speedUp(self):
        if self.turbo == True:
            self.speed += 50
        else:
            super().speedUp()

    def __str__(self):
        if self.turbo == True:
            return "color = %s, speed = %d, 터보 모드" % (self.color, self.speed)
        else:
            return "color = %s, speed = %d, 일반 모드" % (self.color, self.speed)


car1 = Car("Brown", 100)
car2 = Car("Blue", 80)

super_car1 = SuperCar("Black", 100)

super_car1.speedUp()
super_car1.speedUp()

print(car1)
print(car2)
print(car1 == car2)
print(super_car1)

super_car1.setTurbo(False)
super_car1.speedUp()
print(super_car1)
