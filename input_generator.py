import random

'''
n is the number of students, student is the room assignment for each student, limit is the 
limit for happiness. For example n = 3, students = {0:1, 1:2, 3:4}
'''


def main(n, students, limit):
    input_file = open("input_" + str(n) + ".in", "w")
    for student in students:
        room = students[student]
        friends = [student for student in students if students[student] == room]
        for i in range(student, n // 2):
            friend_stress = random.randrange(limit // len(friends)) * 0.998
            other_stress = random.randrange(limit // len(friends), limit * 2 // len(friends)) * 0.998
            happiness = (student + 0.5) * 10 * ((student + 0.5) / (i + 1))
            if i in friends:
                stress = friend_stress
            else:
                stress = other_stress
            line = str(student) + " " + str(i) + " " + str(happiness) + " " + str(stress)
            input_file.write(line + "\n")
        for i in range(n // 2, n):
            stress = random.randrange(limit // len(friends))
            friend_happiness = random.randrange(5, 10) * 1.115
            other_happiness = random.randrange(5) * 1.115
            if i in friends:
                happiness = friend_happiness
            else:
                happiness = other_happiness
            line = str(student) + " " + str(i) + " " + str(happiness) + " " + str(stress)
            input_file.write(line + "\n")


'''
n is the number of students and r is the number of rooms. Write to the output file and generate output 
in dictionary form
'''


def generate_output(n, r):
    output_file = open("output_" + str(n) + ".out", "w")
    result = {}
    for student in range(n):
        room = random.randrange(r)
        line = str(student) + " " + str(room) + "\n"
        output_file.write(line)
        result[student] = room
    #is_valid_solution(D, G, s, rooms):
    #is_valid_solution(result, )
    return result


if __name__ == "__main__":
    student_size = [10, 20, 50] 
    room_num = [3, 6, 10]
    for i in range(3):
        output = generate_output(student_size[i], room_num[i])
        main(student_size[i], output, student_size[i] * 4)
