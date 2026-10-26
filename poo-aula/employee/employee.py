from abc import ABC, abstractmethod

class Employee(ABC):

    count = 0

    @classmethod
    def get_count(cls):
        return cls.count

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Employee.count += 1


    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name
        
    def set_last_name(self, new_last_name):
        self.last_name = new_last_name


    @abstractmethod
    def compute_salary(self):
        ...

    
    def full_name(self):
        return(f"{self.first_name} {self.last_name}")

    


class FulltimeEmployee(Employee):

    def __init__(self, first_name, last_name, base_salary, bonus=0):
        super().__init__(first_name, last_name)
        self.base_salary = base_salary
        self.bonus = bonus

    
    def get_base_salary(self):
        return self.base_salary
    
    def get_bonus(self):
        return self.bonus
    

    def set_base_salary(self, new_base_salary):
        if new_base_salary >= 0:
            self.base_salary = new_base_salary
        else:
            print("Erro: o valor do salário base não pode ser negativo.")
        
    def set_bonus(self, new_bonus):
        if new_bonus >= 0:
            self.bonus = new_bonus
        else:
            print("Erro: o valor do bônus não pode ser negativo.")

    def compute_salary(self):
        return self.base_salary + self.bonus




class HourlyEmployee(Employee):

    def __init__(self, first_name, last_name, worked_hours, value_hour=50):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.value_hour = value_hour

    
    def get_worked_hours(self):
        return self.worked_hours
    
    def get_value_hour(self):
        return self.value_hour
    

    def set_worked_hours(self, new_worked_hours):
        if new_worked_hours >= 0:
            self.worked_hours = new_worked_hours
        else:
            print("Erro: o número de horas trabalhadas não pode ser negativo.")
        
    def set_value_hour(self, new_value_hour):
        if new_value_hour >= 0:
            self.value_hour = new_value_hour
        else:
            print("Erro: o valor por hora não pode ser negativo.")
    

    def compute_salary(self):
        return self.worked_hours * self.value_hour