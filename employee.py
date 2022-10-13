"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
from abc import ABC, abstractmethod

class Employee:
    def __init__(self, name, salary, commission=None):
        self.name = name
        self.salary = salary
        if commission == None:
            self.commission = NoCommission()
        else: 
            self.commission = commission

    def get_pay(self):
        return self.salary.get_pay() + self.commission.get_pay()

    def __str__(self):
        return (f'{self.name} works on a {self.salary.__str__()}{self.commission.__str__()}. Their total pay is {self.get_pay()}.')

#Salary - Interface
class Salary(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def get_pay(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

#Salary - Concrete classes   
class HourlySalary(Salary):
    def __init__(self, hourly_wage, hours_worked):
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def get_pay(self):
        return self.hourly_wage * self.hours_worked

    def __str__(self):
        return (f'contract of {self.hours_worked} hours at {self.hourly_wage}/hour')

class MonthlySalary(Salary):
    def __init__(self, monthly_wage):
        self.monthly_wage = monthly_wage

    def get_pay(self):
        return self.monthly_wage

    def __str__(self):
        return (f'monthly salary of {self.monthly_wage}')

#Commission - Interface
class Commission(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_pay(self):
        pass
        
    @abstractmethod
    def __str__(self):
        pass

#Commission - Concrete classes
class NoCommission(Commission):
    def __init__(self):
        pass
    
    def get_pay(self):
        return 0
    
    def __str__(self):
        return ''

class BonusCommission(Commission): 
    def __init__(self, fixed_bonus):
        self.fixed_bonus = fixed_bonus

    def get_pay(self):
        return self.fixed_bonus

    def __str__(self):
        return (f' and receives a bonus commission of {self.fixed_bonus}')

class ContractCommission(Commission):
    def __init__(self, contracts_landed, commission_per_contract):
        self.contracts_landed = contracts_landed
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        return self.contracts_landed * self.commission_per_contract

    def __str__(self):
        return (f' and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract')

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlySalary(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlySalary(25, 100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlySalary(3000), ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlySalary(25, 150), ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlySalary(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlySalary(30, 120), BonusCommission(600))