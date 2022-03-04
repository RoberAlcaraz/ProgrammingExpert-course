# Employee class
class Employee:
    n_of_employees = 0
    sum_of_age = 0
    sum_of_salary = 0

    average_age = 0
    average_salary = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

        Employee.n_of_employees += 1
        Employee.sum_of_age += age
        Employee.sum_of_salary += salary

        Employee.average_age = Employee.sum_of_age/Employee.n_of_employees
        Employee.average_salary = Employee.sum_of_salary/Employee.n_of_employees


employee = Employee("Clement", 23, 10000)
employee = Employee("Tim", 10, 65000)
print(employee.average_age)
print(employee.average_salary)

# Temperature class


class Temperature:

    min_temperature = 0
    max_temperature = 1000

    def __init__(self, kelvin):
        if Temperature.min_temperature < kelvin < Temperature.max_temperature:
            self.kelvin = kelvin
        else:
            raise Exception('Invalid temperature')

    @classmethod
    def update_min_temperature(cls, kelvin):
        if kelvin > cls.max_temperature:
            raise Exception('Invalid temperature')
        cls.min_temperature = kelvin

    @classmethod
    def update_max_temperature(cls, kelvin):
        if kelvin < cls.min_temperature:
            raise Exception('Invalid temperature')
        cls.max_temperature = kelvin


temperature = Temperature(60)
Temperature.update_max_temperature(100)
print(Temperature.min_temperature)
print(Temperature.max_temperature)
bad_temperature = Temperature(110)
print(bad_temperature.min_temperature)
print(bad_temperature.max_temperature)
