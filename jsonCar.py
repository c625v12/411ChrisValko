#Project: JSON
#Purpose Details: Learn to read and write JSON
#Course: IS411
#Author: Chris Valko
#Date Developed: 08/28/2018
#Last Date Changed: 08/28/2018
#Rev: 1


import json

class Car:
	def __init__(self, carVIN, carName, carYear):
		self.carVIN = carVIN
		self.carName = carName
		self.carYear = carYear

car1 = Car(1234, 'Ford', 2018)
car2 = Car(4325, "Chevrolet", 2016)
carArray = [car1, car2]

with open('jsonCar.json', 'w') as outFile:
	jsonObjCar = outFile.write(json.dumps(car1.__dict__))


with open('jsonCar.json', 'r') as json_data:
	pyObjCar = json.load(json_data)
	print(repr(pyObjCar))
