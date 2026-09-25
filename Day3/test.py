# class Vehicles :       #parent\base\super class
#     def __init__(self,brand,model):
#         self._brand=brand   #  _ => protected
#         self.model=model

#     def move(self):
#         print("Let's go !")

#     def stop(self):
#         print(" stop!")

# class Car(Vehicles):    # child\sub class
#     def __init__(self,brand,model,nums_of_doors):
#         super().__init__(brand,model)            # car inherits attributess from Vehicles
#         self.nums_of_doors=nums_of_doors

#     def move(self):
#         super().move()    #car inherits method  from Vehicles
#         print("hello")



# car1=Car("bmw","2026",4)
# car1.move()
#================================================================
class Restraunt:    # module
    def order(self):
        print("your order is ready")

        