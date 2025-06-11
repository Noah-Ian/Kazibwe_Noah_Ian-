#MRO(Method Resolution Order) determines the order in which methods are searched in a multiple inheritance hierarchy.
#Follows the C3 Linearization (Algorithm) in Python.
#Uses depth-first, left-to-right method lookup with special handling to prevent inconsistencies.
#Can be checked using ClassName.__mro__ or ClassName.mro()

#example
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):  # Multiple Inheritance
    pass

print(D.__mro__)  # Shows method resolution order