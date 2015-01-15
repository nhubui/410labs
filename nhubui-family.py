class Student:
    courseMarks={}
    name = ""
    family = ""
    
    def __init__(self, name, family):
        self.studentName = name
        self.studentFamily = family
    
    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark
    
    
    def average(self):
        totalMarks = 0
        numberCourse = len(self.courseMarks)
        average = 0
        for x in self.courseMarks:
            totalMarks += int(self.courseMarks[x])
            #print(int(self.courseMarks[x])) #test
        average= totalMarks/numberCourse
        print(average)
        return average
    
obj1 = Student("nhu", "bui")
obj1.addCourseMark("cmput410", "85")
obj1.addCourseMark("cmput401", "80")
obj1.addCourseMark("cmput402", "90")
obj1.average()