class Engineering:
    def __init__(self, colleage_name):
        self.college = colleage_name
        self.subject_1 = "Mathematics"
        self.subject_2 = "Soft skills"


class ComputerScience(Engineering):
    def __init__ (self,colleage_name = "St Stephen", special_subject = "Compiler Design"):
        super().__init__(colleage_name)
        self.subject_3 = special_subject

    def course_details(self):
        """ prints course details"""
        print(f"Institution name: {self.college} colleage")
        print("Computer Science course includes: ")
        print(f"1:{self.subject_1}")
        print(f"3:{self.subject_3}")
        print("_" * 10)


cs_course1 = ComputerScience("Presidency", "Python Programming")
cs_course1.course_details()

cs_course2 = ComputerScience()
cs_course2.course_details()
