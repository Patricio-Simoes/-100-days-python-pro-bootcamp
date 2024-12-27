import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
numbers = [1,2,3]

new_list_numbers = [item + 1 for item in numbers]

new_tuple_numbers = tuple(item + 1 for item in numbers)

new_range_numbers = [i*2 for i in range(1,5)]

new_names = [name.upper() for name in names if len(name) < 5]

students_scores = {student:random.randint(1,100) for student in names}

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}

print(new_list_numbers) # [2, 3, 4].
print(new_tuple_numbers) # (2, 3, 4).
print(new_range_numbers) # [2, 4, 6, 8].
print(new_names) # ['ALEX', 'BETH', 'DAVE']
print(students_scores) # {'Alex': 62, 'Beth': 19, 'Caroline': 34, 'Dave': 77, 'Elanor': 56, 'Freddie': 36}
print(passed_students) # {'Alex': 62, 'Dave': 77}