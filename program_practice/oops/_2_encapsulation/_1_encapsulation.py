# Encapsulation
# it is use to bind attributes(variable) and behaviour(method) together into one single unit
# it is use to access private members through public environment

# private member - cannot be accessed outside the class.


class Car:
    def __init__(self,__engine, brand, mileage):                                # private member 
        self.__engine = __engine
        self.brand = brand
        self.mileage = mileage

    def display(self):
        return f"car details : \nEngine: {self.__engine} \nBrand: {self.brand} \nMileage :{self.mileage}"
    
    # Getter and Setter:++ Imp++ it can assess the instance class

    # Setter for engine
    def set_engine(self, __engine):
        # if username =="Ajeeth":
        self.__engine = __engine

    # getter for engine    
    def get_engine(self):
        return self.__engine
    
    # Setter for brand
    def set_brand(self, brand):
        self.brand = brand
    
    # getter for brand    
    def get_brand(self):
        return self.brand
    
    # Setter for mileage
    def set_mileage(self, mileage):
        self.mileage = mileage

    # getter for mileage       
    def get_mileage(self):
        return self.mileage




car = Car("Diesel Engine","BMW","35km/l")
# print(car.brand)
# print(car.__engine) #AttributeError: 'Car' object has no attribute '__engine'   --- ># private member  cannot be accessed outside the class.
# data = car.get_engine()
# print(data)


# car.set_engine("PEtrol Engine", "Sivani")      #Setting the username in __engine, If it changes only valid username== Ajeeth else its not changing.
# data = car.get_engine()
# print(data)

data = car.display()
print("Before Modification: \n",data, "\n")

car.set_mileage("45km/l")
car.set_engine("Petrol Engine")

data = car.display()
print("After Modification: \n",data, "\n")

# If we need data |specifically| Use getter:

mileage = car.get_mileage() 
print(mileage)