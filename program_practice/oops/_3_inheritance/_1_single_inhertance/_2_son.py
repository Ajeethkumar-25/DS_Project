# Single Inheritance - bcz it has one parent class and one child class



from _1_dad import dad

class son(dad):                          #child class
    def mobile(self):
        print("Mobile")
    def bike(self):
        print("Bike")


son_obj = son()
son_obj.bike()
son_obj.mobile()
son_obj.flat()
son_obj.car()
