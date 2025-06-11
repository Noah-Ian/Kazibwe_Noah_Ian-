#Method overriding occurs when a child class provides a specific implementation for a method that is already defined in its parent class.
#The overridden method in the child class must have the same name, parameters, and return type as in the parent class.
#Allows polymorphism, enabling different behaviors depending on the object type.
#Used in inheritance to modify behavior of a superclass method in a subclass.

#Example

class Parent:
    def show(self):
        print("This is the Parent class.")

class Child(Parent):
    def show(self):  # Overriding the show() method
        print("This is the Child class.")

obj = Child()
obj.show()  # Output: This is the Child class.