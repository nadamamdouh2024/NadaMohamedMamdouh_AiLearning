class Person:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def introduce (self):
        print(f" Hi , I'm {self.name}") 


class Student(Person):

    total_students=0

    def __init__(self,name,email,grade):
        super().__init__(name,email)   
        self.__grade=grade
        Student.total_students +=1
        self.courses=[]

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self,newgrade):
        if  0<= newgrade <=100:
            self.__grade= newgrade
        else:
            print("Grade must be between 0:100 ")  

    def add_course(self,course):
        self.courses.append(course)    

    def introduce(self):
        print(f" hi i am dr {self.name} and i am a student and my grade is {self.grade}")       


class Teacher(Person):

    def __init__(self,name , email ,subject):
        super().__init__(name,email)
        self.subject = subject
        self.subjects=[]

    def add_course(self,course):
        self.subjects.append(course)
        

    def introduce(self):
        super().introduce()
        print(f"hi i am {self.name} and i am a teaching {self.subject}") 


class Course:

    total_courses=0

    def __init__ (self,name,teacher):
        self.name=name
        self.teacher=teacher
        self.students=[]
        Course.total_courses +=1

    def add_student(self,student):
        if student not in self.students:
            self.students.append(student)
            print(f"{student.name} is enrolled in {self.name}")
        else:
            print(f"{student.name} is already enrolled in {self.name}")


    def showStudents(self):
        print(f" Students in {self.name}: ")
        if len(self.students)==0:
            print("no students yet")
            return
        for student in self.students:
            print (f"{student.name} , ==> Grade: ==>{student.grade}")


t1= Teacher("tamer","temo@gmail.com","cf")

c1= Course("cf",t1)

t1.add_course(c1)
t1.introduce()

s1=Student("nada","nada@gmail.com",90)
s2=Student("nado","nado@gmail.com",100)

s1.introduce()
s1.grade=50
s1.introduce()


print(Student.total_students)

c1.add_student(s1)
c1.add_student(s2)

c1.add_student(s2)
c1.showStudents()