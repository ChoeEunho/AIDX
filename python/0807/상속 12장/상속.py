class Car:
    def __init__(self, make, model, color, price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price  

    def setMake(self, make):
        self.make = make

    def getMake(self):
        return self.make

    def printInfo(self):
        return "메이커 = " + self.make + " 모델 = " + self.model + " 색상 = " + self.color + " 가격 = " + str(self.price)  

class ElectricCar(Car):
    def __init__(self, make, model, color, price, batterySize):
        super().__init__(make, model, color, price)  
        self.batterySize = batterySize

    def setBatterySize(self, batterySize):
        self.batterySize = batterySize

    def getBatterySize(self):
        return self.batterySize

    def printInfo(self):
        return super().printInfo() + " 배터리 용량 = " + str(self.batterySize)  

def main():
    basicCar = Car("현대", "아반떼", "블랙", 20000)  
    myCar = ElectricCar("Tesla", "Model S", "White", 100000, 60)  
    print(myCar.printInfo())
    
main()