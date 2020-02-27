import datetime
import math

now = datetime.datetime.today()

# print(now.year)
# print(now.month)
# print(now.minute)
# print(now.hour)


# print(math.log(3.3))
# print(math.cos(3))


employee_info  = {
}

employee_info["xinyi"] = "cs major"
employee_info["carl"]  = "stats"
employee_info["bob"]   = "history"

#print(employee_info.items())

for emp in employee_info.items():
    k, v = emp
    print("the key is {} and the value is {}".format(k, v))