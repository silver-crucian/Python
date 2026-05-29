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
    def getDesc(self):
        return "차량 =("+str(self.make)+","+\
        str(self.model)+","+\
        str(self.color)+","+\
        str(self.price)+")"
    

class ElectricCar(Car):
    def __init__(self, make, model, color, price, batterySize):
        super().__init__(make, model, color, price) 
        self.batterySize=batterySize 
    def setBatterySize(self, batterySize): 
        self.batterySize=batterySize
    def getBatterySize(self): 
        return self.batterySize
    

def main():
    myCar = ElectricCar("Tesla","Model T","Black",1000,0)
    myCar.setBatterySize(100)
    myCar.setMake("Tesla")

    print(myCar.getDesc())

main()