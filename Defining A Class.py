#define a Class
class Bike:
    name = ""
    gear = 0
#create object of Class
bike1 = Bike()

#access attribute and assign new value 
bike1.gear = 11
bike1.name = "Mountain Bike"
print(f"Name : {bike1.name}, Gears : {bike1.gear}")