# 3. Sort Employees

# Write a function that accepts a list of lists that contain the name, age and
# salary of specific employees and also accepts a string representing the key to
# sort employees by. Your function should return a new list that contains the
# lists representing each employee sorted in ascending order by the given key.


# The string parameter named sort_by  will always be equal to one of
# the following values: name, age or salary

from numpy import sort


employees = [
    ["John", 33, 65000],
    ["Sarah", 24, 75000],
    ["Josie", 29, 100000],
    ["Jason", 26, 55000],
    ["Connor", 25, 110000]
]


def sort_employees(employees, sort_by):
    sorted_lst = employees[:]
    if sort_by == 'name':
        return sorted(sorted_lst, key=lambda x: x[0])
    if sort_by == 'age':
        return sorted(sorted_lst, key=lambda x: x[1])
    if sort_by == 'salary':
        return sorted(sorted_lst, key=lambda x: x[2])


sort_employees(employees, 'age')
