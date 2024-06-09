class Vehicles:

	car_name1 = "Tesla Model 3"
	car_name2 = "Mustang"

	def main(self):
		print("I have", self.car_name1)
		print("I have", self.car_name2)


Vehicles_class_object = Vehicles()


print("Your car is: ", Vehicles_class_object.car_name1)
Vehicles_class_object.main()