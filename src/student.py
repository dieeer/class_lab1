
class Student:
    def __init__(self, student_name, student_cohort):
        self.name = student_name 
        self.cohort = student_cohort  

    def change_name(self, student_name):
        self.name = "Mike"

    def change_cohort(self, student_cohort):
        self.cohort = "G21"

    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, favourite_language):
        return "I love " + favourite_language