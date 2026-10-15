# Classes
class UniversitySystem:
    # ijad sakhtar baraye zakhire kardan ashia
    def __init__(self):
        self.Students = {}
        self.CourseUnits = {}
        self.Teachers = {}

    # zakhire kardan ashia
    def AddStudent(self, Student):
        self.Students[f"{Student}"] = Student.__dict__

    def AddCourseUnit(self, Course):
        self.CourseUnits[f"{Course}"] = Course.__dict__

    def AddTeacher(self, Teacher):
        self.Teachers[f"{Teacher}"] = Teacher.__dict__

    # methodhaye system
    def Get_Unit_Code(self):
        Searched = []
        Select = input("esme darse morede nazar ra vared konid:")
        for course in self.CourseUnits.values():
            if course["CourseName"] == Select:
                Searched.append(course)
                print(Searched)
        Select_UnitCode = int(
            input("code class moredenazar ra az miane liste dade shode entekhab konid:")
        )
        return Select_UnitCode

    def Get_Stu_Code(self):
        Searched = []
        Select = input("esme darneshjoye morede nazar ra vared konid:")
        for student in self.Students.values():
            if f'{student["Firstname"]}{student["Lastname"]}' == Select:
                Searched.append(student)
                print(Searched)
        Select_StuCode = int(
            input(
                "code daneshjoye moredenazar ra az miane liste dade shode entekhab konid:"
            )
        )
        return Select_StuCode

    def SelectUnit(self, studentId, UnitCode):

        # peyda kardane class ba code
        for course in self.CourseUnits.items():
            if course[1]["CourseId"] == UnitCode:
                result = course[1]
            else:
                result = None
                return "class morede nazar peyda nashod"
        # peyda kardane daneshjo bar asas code daneshjo
        for selected_student in self.Students.items():
            if selected_student["StudentId"] == studentId:
                stu = selected_student[1]
            else:
                stu = None
                return "daneshjoye morede nazar peyda nashod"
        # check kardane tekrari bodan
        for selected_course in stu["Units"]:
            if selected_course["CourseId"] == result["CourseId"]:
                print("in dars ghablan entekhab shode ast")
                return False
        #    check kardane zarfiate class
        if result["Capacity"] == 0:
            print("in class zarfiat nadarad")
            return False
        # check kardane jensiat
        if result["Gender"] != "Both" and result["Gender"] != stu["Gender"]:
            print("be dalil jensit mojaz be bardashtane in dars nist")
            return False

        # check kardane reshte tahsili
        if result["StudyField"] != result["StudyField"]:
            print("in class baraye reshteye in daneshjo nist")
            return False

        # sabte class va entekhab vahede movafagh
        else:
            # student.Units.append(result)
            # course.Capacity -= 1
            print("vahede morede nazar ba movafaghiat entekhab shod.")
            return True


System = UniversitySystem()


class CourseUnits:

    def __init__(
        self,
        CourseId,
        CourseName,
        PracticalNum,
        TheoreticalNum,
        EducationLevel,
        StudyField,
        Location,
        Day,
        Time,
        TeacherName,
        Capacity,
        Gender,
        ExamDay,
        ExamTime,
    ):
        self.CourseId = CourseId
        self.CourseName = CourseName
        self.PracticalNum = PracticalNum
        self.TheoreticalNum = TheoreticalNum
        self.EducationLevel = EducationLevel
        self.StudyField = StudyField
        self.Location = Location
        self.Day = Day
        self.Time = Time
        self.TeacherName = TeacherName
        self.Capacity = Capacity
        self.Gender = Gender
        self.ExamDay = ExamDay
        self.ExamTime = ExamTime


class User:
    def __init__(self, Firstname, Lastname, Username, Password, CodeMelli, Gender):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Username = Username
        self.__Password = Password
        self.CodeMelli = CodeMelli
        self.Gender = Gender

    @property
    def Password(self):
        return self.__Password

    @Password.setter
    def Password(self, NewPass):
        self.__Password = NewPass


class Teacher(User):

    def __init__(
        self,
        Firstname,
        Lastname,
        Username,
        Password,
        CodeMelli,
        Gender,
        TeacherId,
        Specialization,
        EducationDegree,
    ):
        super().__init__(Firstname, Lastname, Username, Password, CodeMelli, Gender)
        self.TeacherId = TeacherId
        self.Specialization = Specialization
        self.EducationDegree = EducationDegree


class Student(User):
    TermNumber = 4051

    def __init__(
        self,
        Firstname,
        Lastname,
        Username,
        Password,
        CodeMelli,
        Gender,
        StudentId,
        EducationLevel,
        StudyField,
    ):
        super().__init__(Firstname, Lastname, Username, Password, CodeMelli, Gender)
        self.StudentId = StudentId
        self.EducationLevel = EducationLevel
        self.StudyField = StudyField

        self.Units = []


c101 = CourseUnits(
    101,
    "Riazy1",
    0,
    3,
    "Karshensi",
    "Computer Engineering",
    "class 101",
    "Sunday",
    "12:00",
    "Sara Mohammadi",
    30,
    "Both",
    "1405.10.15",
    "10:00",
)
System.AddCourseUnit(c101)

c102 = CourseUnits(
    102,
    "Riazy2",
    0,
    3,
    "Karshensi",
    "Computer Engineering",
    "class 102",
    "Sunday",
    "12:00",
    "Sara Mohammadi",
    30,
    "Both",
    "1405.10.15",
    "10:00",
)
System.AddCourseUnit(c102)

s401222365412 = Student(
    "Nazanin",
    "Bayati",
    "nazi56",
    "1234",
    "011223344",
    "Female",
    401222365412,
    "Karshenasi",
    "Computer Engineering",
)
System.AddStudent(s401222365412)

sc = System.Get_Stu_Code()
uc = System.Get_Unit_Code()
System.SelectUnit(sc, uc)
