from logic import *

#This is a substitute frontend to show how we would've implemented it in front end
all_desired = []

while True:
    one_course = []
    sub = str(input("Enter the subject of the class (etc AAS) (Enter to Stop): "))
    course = str(input("Enter the course number (etc 001) (Enter to Stop): "))

    if sub == '' or course == '':
        break
    one_course.append(sub)
    one_course.append(course)
    all_desired.append(one_course)

for sche in find_all_schedules(all_desired):
    print(sche)