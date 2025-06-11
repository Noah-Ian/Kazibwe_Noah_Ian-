#Banking System (Method Overriding & Overloading)

class BankAccount:
    def interest_rate(self):
        return "Standard bank interest rate: 3%"

class SavingsAccount(BankAccount):
    def interest_rate(self):  # Overriding method
        return "Savings Account interest rate: 5%"

class CheckingAccount(BankAccount):
    def interest_rate(self):  # Overriding method
        return "Checking Account interest rate: 2%"

 
savings = SavingsAccount()
checking = CheckingAccount()

print(savings.interest_rate())  
print(checking.interest_rate()) 



#Self-Driving Cars (MRO in Multiple Inheritance)
class Vehicle:
    def control(self):
        return "Basic vehicle control activated."

class AutonomousSystem(Vehicle):
    def control(self):
        return "Autonomous driving activated."

class EmergencySystem(Vehicle):
    def control(self):
        return "Emergency override activated."

class SmartCar(AutonomousSystem, EmergencySystem):
    pass

print(SmartCar.__mro__)  
print(SmartCar().control()) 