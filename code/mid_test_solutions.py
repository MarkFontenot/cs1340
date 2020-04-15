# Q1

def get_sum():
    total = 0
    n = 1
    while 1 / n >=  1 / 1000:
        if n % 2 == 0:
            total -= 1 / n
        else:
            total += 1 / n
        n += 1
    return total

print(get_sum())


# Q2

def remove_duplicates(numbers):
    new_l = []
    for n in numbers:
        if n not in new_l:
            new_l.append(n)
    return new_l

print(remove_duplicates([1, 9, 3, 12, 11, 1, 3, 3, 21]))

# Q3

def count_stuff(a_str):
    res = {"letters": 0, "digits": 0}
    digits = [str(i) for i in range(10)]
    for c in a_str:
        if c in digits:
            res["digits"] += 1
        else:
            res["letters"] += 1
    return res

print(count_stuff("123dght!"))


# Q4

def load_data(filename):
    res = []
    with open(filename) as the_file:
        data = the_file.readlines()
        i = 0
        while i < len(data):
            attempts = int(data[i])
            exercise_ids = list(map(int, data[i + 1].strip().split(",")))
            responses = list(map(int, data[i + 2].strip().split(",")))
            stu = ([attempts], exercise_ids, responses)
            if attempts >= 3:
                res.append(stu)
            i += 3
    return res

filename = "exercises.csv"
data = load_data(filename)
# print(data)


# Q5

max_attempts = 0
exs_ids = []
i = 0
while i < len(data):
    current_student = data[i]  # ([attempts], [exericises_ids], [responses])
    current_attempt = current_student[0][0]
    if current_attempt > max_attempts:
        max_attempts = current_attempt
    exercises_ids = data[i][1]
    for id in exercises_ids:
        if id not in exs_ids:
            exs_ids.append(id)

    i += 1

print(max_attempts)
print(len(exs_ids))
