def grade_Calculate(line):
    line = line[:-1]
    list = line.split(':')
    studentName = list[0]
    scores = list[1].split(',')
    grade1 = int(scores[0])
    grade2 = int(scores[1])
    grade3 = int(scores[2])
    average = (grade1+grade2+grade3)/3

    if average>= 90 and average<=100:
        grade = "AA"
    elif average >=85 and average<=89:
        grade = "BA"
    elif average >=80 and average<=84:
        grade = "BB"
    elif average >=75 and average<=79:
        grade = "CB"
    elif average >=70 and average<=74:
        grade = "CC"
    elif average >=65 and average<=69:
        grade = "DC"
    elif average >=60 and average<=64:
        grade = "DD"
    elif average >=50 and average<=59:
        grade = "FD"
    else:
        grade = "FF"
    return studentName + ": "+ grade + "\n"


def read_Average():
    with open("test_scores.txt","r",encoding="utf-8") as file:
        for line in file:
            print(grade_Calculate(line))
            

def Enter_grade():
    name = input('Student name: ')
    surname = input('Student surname: ')
    grade1 = input('grade 1: ')
    grade2 = input('grade 2: ')
    grade3 = input('grade 3: ')
    with open("test_scores.txt","a",encoding="utf-8") as file:
        file.write(name + ' ' + surname + ':' + grade1 + ',' + grade2 + ',' + grade3 + '\n')
def record_grade():
    with open('test_scores.txt','w',encoding='utf-8') as file:
        list = []
        for line in file:
            list.append(grade_Calculate(line))
        with open('results.txt','w',encoding='utf-8') as file2:
            for i in file2:
                file2.write(i)


while True:
    process = input("1 - show grades\n2 - enter grades\n3 - record the grades\n4 - Exit\n")

    if process == '1':
        read_Average()
    elif process == '2':
        Enter_grade()
    elif process == '3':
        record_grade()
    else:
        break

    