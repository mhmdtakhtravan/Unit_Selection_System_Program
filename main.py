# Classes
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
        Univercity,
        Units,
    ):
        super().__init__(Firstname, Lastname, Username, Password, CodeMelli, Gender)
        self.StudentId = StudentId
        self.EducationLevel = EducationLevel
        self.StudyField = StudyField
        self.Univercity = Univercity
        self.Units = Units


class Operator(User):

    def __init__(
        self,
        Firstname,
        Lastname,
        Username,
        Password,
        CodeMelli,
        Gender,
        OperatorId,
        WorkDomain,
    ):
        super().__init__(Firstname, Lastname, Username, Password, CodeMelli, Gender)
        self.OperatorId = OperatorId
        self.WorkDomain = WorkDomain


class CourseUnit:

    def __init__(
        self,
        CourseId,
        PracticalNum,
        theoreticalNum,
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
        self.PracticalNum = PracticalNum
        self.theoreticalNum = theoreticalNum
        self.Location = Location
        self.Day = Day
        self.Time = Time
        self.TeacherName = TeacherName
        self.Capacity = Capacity
        self.CourseId = CourseId
        self.Gender = Gender
        self.ExamDay = ExamDay
        self.ExamTime = ExamTime
