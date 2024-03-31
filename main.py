# Built-in imports
import math

# Your code below
GRADE = {}
for i in range(0, 100):
    if i >= 70:
        GRADE[i] = 'A'
    elif i >= 60:
        GRADE[i] = 'B'
    elif i >= 55:
        GRADE[i] = 'C'
    elif i >= 50:
        GRADE[i] = 'D'
    elif i >= 45:
        GRADE[i] = 'E'
    elif i >= 40:
        GRADE[i] = 'S'
    else:
        GRADE[i] = 'U'

def read_testscores(filename):
    '''
    Function that reads data from filename and represents     each row's data as a dict
    filename -> a string containing the file
    '''
    students = []
    file = open(filename, "r")
    file.readline()
    for i in range(419):
        row = {}
        line = file.readline().strip().split(",")
        row["class"] = line[0]
        row["name"] = line[1]
        p1 = int(line[2])
        p2 = int(line[3])
        p3 = int(line[4])
        p4 = int(line[5])
        overall = (p1/30 * 15) + (p2/40 * 30) + (p3/80 *          35) + (p4/30 * 20)
        overall = math.ceil(overall)
        row["overall"] = overall
        row["grade"] = GRADE[overall]
        students.append(row)
    file.close()
    return students

def analyze_grades(studentdata):
    '''
    Function that returns a dict representing the number      of students that achieved each grade for each class
    '''
    count = {}
    for class_ in range(1, 19):
        s = "Class" + str(class_)
        count[s] = {}
        count[s]['A'] = 0
        count[s]['B'] = 0
        count[s]['C'] = 0
        count[s]['D'] = 0
        count[s]['E'] = 0
        count[s]['S'] = 0
        count[s]['U'] = 0
        
    
    for item in studentdata:
        count[item["class"]][item["grade"]] += 1
    return count
