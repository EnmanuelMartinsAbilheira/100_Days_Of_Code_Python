names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']

import random

students_score = {student:random.randint(1,100) for student in names}

#students_score.keys()
#dict_keys(['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie'])

#students_score.values()
#dict_values([64, 95, 67, 56, 54, 36])

passed_students = {student:score for (student, score) in students_score.items() if score >=60}