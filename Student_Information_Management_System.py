import csv
import copy


class Student:
    def __init__(self, name, number, math, physics, chemistry):
        """Define student class

        Args:
            name:
            number:
            math:
            physics:
            chemistry:
        """
        self.name = name
        self.number = number
        self.math = math
        self.physics = physics
        self.chemistry = chemistry


class Information:
    def __init__(self):
        self.student_info = []

    @staticmethod
    def add_score(subject):
        """Limits the input student's grades, which must be integers from 0 to 100

        Args:
            subject:Input score

        Returns:
            An integer between 0 and 100

        """
        while True:
            try:
                stu_score = input(subject).strip()
                if 0 <= int(stu_score) <= 100:
                    break
                else:
                    print("Please enter an integer between 0 and 100")
                    continue
            except ValueError:
                print("Please enter an integer between 0 and 100")
        return stu_score

    @staticmethod
    def add_id(message):
        """Specify the format of student numbers, which must be integers from 1000 to 9999

        Args:
            message:The student number entered

        Returns:
            An integer between 1000 and 9999

        """
        while True:
            try:
                stu_id = input(message).strip()
                if 1000 <= int(stu_id) <= 9999:
                    break
                else:
                    print("Please enter an integer between 1000 and 9999")
                    continue
            except ValueError:
                print("Please enter an integer between 1000 and 9999")
        return stu_id

    def number(self, number):
        """The student number must be unique. Determine whether the student number already exists

        Args:
            number:The student number entered

        Returns:
            the student number exists or not exists

        """
        for stu in self.student_info:
            if stu.number == number:
                return True
        else:
            return False

    def add_student(self):
        """Add student information, including student number, name, math, physics, chemistry scores

        Returns:
            Student information

        """
        while True:
            number = self.add_id("Student ID number: ")
            if self.number(number):
                print("The student ID number already exists ")
            else:
                name = input("Student name: ").strip()
                math = self.add_score("Math score : ").strip()
                physics = self.add_score("Physic score: ").strip()
                chemistry = self.add_score("Chemistry score: ").strip()
                stu_info = Student(name, number, math, physics, chemistry)
                self.student_info.append(stu_info)
            check = input("Do you want to add more information? Y/N")
            if check.upper() == "Y":
                continue
            else:
                break

    def remove_student(self):
        """Remove existing students"""
        while True:
            del_stu = input("Please enter the student ID that you want to delete: ").strip()
            for stu in self.student_info:
                if stu.number == del_stu:
                    self.student_info.remove(stu)
                    break
            else:
                print("The student number does not exist. Please enter it again")
                continue
            check = input("Do you want to delete more information? Y/N")
            if check.upper().strip() == "Y":
                continue
            else:
                break

    def modify_student(self):
        """Remove existing students

        Returns:
            Modified student information

        """
        while True:
            mod_stud = input("Please enter the student ID that you want to modify: ")
            if self.number(mod_stud):
                for mod_stu in self.student_info:
                    if mod_stu.number == mod_stud:
                        mod_stu.name = input("Student name: ").strip()
                        mod_stu.math = self.add_score("Math score : ").strip()
                        mod_stu.physics = self.add_score("Physic score: ").strip()
                        mod_stu.chemistry = self.add_score("Chemistry score: ").strip()
                        break
            else:
                print("The student number does not exist. Please enter it again")
                continue
            check = input("Do you want to modify more information? Y/N")
            if check.upper().strip() == "Y":
                continue
            else:
                break

    def find_student(self):
        """Find existing student information"""
        while True:
            find_stud = input("Please enter the student ID that you want to search: ").strip()
            if self.number(find_stud):
                for find_stu in self.student_info:
                    if find_stu.number == find_stud:
                        print('{:8}\t{:8}\t{:<8}\t{:<8}\t{:<8}'
                              .format("NAME", "NUMBER", "MATH", "PHYSICS", "CHEMISTRY"))
                        print('{:8}\t{:8}\t{:<8}\t{:<8}\t{:<8}'
                              .format(find_stu.name, find_stu.number, find_stu.math,
                                      find_stu.physics, find_stu.chemistry))
            else:
                print("The student number does not exist. Please enter it again")
            check = input("Do you want to search more information? Y/N")
            if check.upper().strip() == "Y":
                continue
            else:
                break

    def show_student(self):
        """Show  all existing students information"""
        if len(self.student_info) != 0:
            show_title = '{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
            print(show_title.format("NAME", "NUMBER", "MATH", "PHYSICS", "CHEMISTRY"))
            for show_stu in self.student_info:
                print('{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}'
                      .format(show_stu.name, show_stu.number, show_stu.math, show_stu.physics, show_stu.chemistry))
        else:
            print("There are no student information")

    def load_student(self, filename):
        """Load student information from file

        Args:
            filename:loading file name

        Returns:
            Student information that does not exist in the system

        """
        try:
            with open(filename, "r", encoding='utf-8') as f:
                while True:
                    csv_reader = f.readline().strip("\n")
                    if not csv_reader:
                        break
                    else:
                        stu = Student(*csv_reader.split(","))
                        if self.number(stu.number):
                            continue
                        else:
                            self.student_info.append(stu)
            print("Load successfully")
        except FileNotFoundError:
            print("There is an error")

    def save_student(self, filename):
        """Save all student information

        Args:
            filename: saving file name

        Returns:
            Student information file

        """
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for item in self.student_info:
                writer.writerow([item.name, item.number, item.math, item.physics, item.chemistry])
        print("Save successfully")

    def ave_scores(self):
        """Calculate the average scores of all students in math, English and chemistry

        Returns:
            Average scores in  Math, English, chemistry

        """
        if len(self.student_info) > 0:
            stu_length = len(self.student_info)
            ave_math = sum([int(stu.math) for stu in self.student_info])/stu_length
            ave_physics = sum([int(stu.physics) for stu in self.student_info])/stu_length
            ave_chemistry = sum([int(stu.physics) for stu in self.student_info])/stu_length
            print("Math Average Score: %.2f" % ave_math)
            print("physics Average Score: %.2f" % ave_physics)
            print("Chemistry Average Score: %.2f" % ave_chemistry)
        else:
            print("There are no students information")

    @staticmethod
    def formula(x: int):
        """Grade point conversion formula for each course,the full grade point is 4.
           If the grade is 60 or higher, the grade point conversion is based on this formula:
           4-(3*(100-int(x))**2/1600).
           If the score is less than 60, the GPA is 0
        Args:
            x: Student scores in each subject, for example, math: 90, physics: 87, chemistry: 79

        Returns:
            conversion formula

        """
        if 60 <= int(x) <= 100:
            return 4-(3*(100-int(x))**2/1600)
        else:
            return 0

    def average_gpa(self):
        """The grade is converted to a 4-point scale by using the grade point conversion formula for each course
           Math, physics, and chemistry are assigned 3, 4, and 5 credits respectively.
           The final GPA is obtained by taking the weighted GPA of the three courses

        Returns:
            Student's grade point average

        """
        stu_grades = copy.deepcopy(self.student_info)
        if len(stu_grades) > 0:
            for stu in stu_grades:
                stu.math = self.formula(int(stu.math))
                stu.physics = self.formula(int(stu.physics))
                stu.chemistry = self.formula(int(stu.chemistry))
            print(f"Student's GPAs are as follows:")
            print('{:8}\t{:8}\t{:<8}'.format("NAME", "NUMBER", "GPA"))
            for stu in stu_grades:
                stu_gpa = list(map(lambda x, y: x*y, [stu.math, stu.physics, stu.chemistry], [3, 4, 5]))
                print('{:8}\t{:8}\t{:<8}'.format(stu.name, stu.number, round(sum(stu_gpa)/12, 2)))

    def rank_stu_math(self):
        """Display student information in order of highest to the lowest math scores

        Returns:
            Student information, including student name, student number, math score

        """
        if len(self.student_info) > 0:
            get_math = sorted(self.student_info, key=lambda x: x.math, reverse=True)
            print("The ranking of math scores from highest to lowest is as follows: ")
            print('{:8}\t{:8}\t{:<8}'.format("NAME", "NUMBER", "MATH"))
            for stu in get_math:
                print('{:8}\t{:8}\t{:<8}'.format(stu.name, stu.number, stu.math))
        else:
            print("There are no students information")

    def rank_stu_physics(self):
        """Display student information in order of highest to the lowest physics scores

        Returns:
            Student information, including student name, student number, physics score

        """
        if len(self.student_info) > 0:
            get_physics = sorted(self.student_info, key=lambda x: x.physics, reverse=True)
            print("The ranking of physics scores from highest to lowest is as follows: ")
            print('{:8}\t{:8}\t{:<8}'.format("NAME", "NUMBER", "PHYSICS"))
            for stu in get_physics:
                print('{:8}\t{:8}\t{:<8}'.format(stu.name, stu.number, stu.physics))
        else:
            print("There are no students information")

    def rank_stu_chemistry(self):
        """Display student information in order of highest to the lowest chemistry scores

        Returns:
            Student information, including student name, student number, chemistry score

        """
        if len(self.student_info) > 0:
            get_chemistry = sorted(self.student_info, key=lambda x:  x.chemistry, reverse=True)
            print("The ranking of chemistry scores from highest to lowest is as follows: ")
            print('{:8}\t{:8}\t{:<8}'.format("NAME", "NUMBER", "CHEMISTRY"))
            for stu in get_chemistry:
                print('{:8}\t{:8}\t{:<8}'.format(stu.name, stu.number, stu.chemistry))
        else:
            print("There are no students information")

    def filter_stu_math(self):
        """filter the information of students who scored below 60 in math.
           Show and count the number of students who scored 60 or above in math

        Returns:
            Student information, including student name, student number, math score
            The number of students

        """
        if len(self.student_info) > 0:
            filter_math = filter(lambda x: int(x.math) >= 60, self.student_info)
            print("Math scores over 60 are as follows:")
            print('{:8}\t{:8}\t{:<8}'.format("NAME", "NUMBER", "MATH"))
            num = 0
            for stu in filter_math:
                print('{:8}\t{:8}\t{:<8}'.format(stu.name, stu.number, stu.math))
                num += 1
            print(f"total number is: {num} ")
        else:
            print("There are no students information")

    def filter_stu_physics(self):
        """filter the information of students who scored below 60 in physics.
           Show and count the number of students who scored 60 or above in physics

        Returns:
            Student information, including student name, student number, physics score
            The number of students

        """
        if len(self.student_info) > 0:
            filter_physics = filter(lambda x: int(x.physics) >= 60, self.student_info)
            print("Physics scores over 60 are as follows:")
            print('{:8}\t{:8}\t{:<8}'.format("NAME", "NUMBER", "PHYSICS"))
            num = 0
            for stu in filter_physics:
                print('{:8}\t{:8}\t{:<8}'.format(stu.name,  stu.number, stu.physics))
                num += 1
            print(f"total number is: {num} ")
        else:
            print("There are no students information")

    def filter_stu_chemistry(self):
        """filter the information of students who scored below 60 in chemistry.
           Show and count the number of students who scored 60 or above in chemistry

        Returns:
            Student information, including student name, student number, chemistry score
            The number of students

        """
        if len(self.student_info) > 0:
            filter_chemistry = filter(lambda x:  int(x.chemistry) >= 60, self.student_info)
            print("Chemistry scores over 60 are as follows:")
            print('{:8}\t{:8}\t{:<8}'.format("NAME", "NUMBER", "CHEMISTRY"))
            num = 0
            for stu in filter_chemistry:
                print('{:8}\t{:8}\t{:<8}'.format(stu.name, stu.number, stu.chemistry))
                num += 1
            print(f"total number is: {num} ")
        else:
            print("There are no students information")

    def info_statistics(self):
        """Student information statistics menu

        Returns:
            Average Scores
            Score ranking In Math
            Score ranking In Physics
            Score ranking In Chemistry
            Pass Student In Math
            Pass Student In Physics
            Pass Student In Chemistry
            Grade Point Average
            Return
        """
        print("Information Statistics".center(64, "*"))
        print(" "*20 + "A------Average Score")
        print(" "*20 + "B------Score ranking In Math")
        print(" "*20 + "C------Score ranking In Physics")
        print(" "*20 + "D------Score ranking In Chemistry")
        print(" "*20 + "E------Pass Student In Math")
        print(" "*20 + "F------Pass Student In Physics")
        print(" "*20 + "G------Pass Student In Chemistry")
        print(" "*20 + "H------Grade Point Average")
        print(" "*20 + "R------Return")
        print("".center(64, "*"))
        while True:
            choice = input("info_statistics: ").strip().upper()
            if choice == "A":
                self.ave_scores()
            elif choice == "B":
                self.rank_stu_math()
            elif choice == "C":
                self.rank_stu_physics()
            elif choice == "D":
                self.rank_stu_chemistry()
            elif choice == "E":
                self.filter_stu_math()
            elif choice == "F":
                self.filter_stu_physics()
            elif choice == "G":
                self.filter_stu_chemistry()
            elif choice == "H":
                self.average_gpa()
            elif choice == "R":
                break
            else:
                print("Input error")

    def main(self):
        """The main function of the program."""
        while True:
            print("Student Information Management System".center(64, "*"))
            print("Menu".center(64, "="))
            print("A-------Add Student Information".center(64, " "))
            print("R-----Remove Student Information".center(64, " "))
            print("M-----Modify Student Information".center(64, " "))
            print("F-------Find Student Information".center(64, " "))
            print("S-------Show Student Information".center(64, " "))
            print("L-------Load Student Information".center(64, " "))
            print("K-------Save Student Information".center(64, " "))
            print("I--------Information Statistics".center(64, " "))
            print("E-------Exit Information system".center(64, " "))
            print("".center(64, "*"))
            choice = input("main:").strip().upper()
            if choice == "A":
                self.add_student()
            elif choice == "R":
                self.remove_student()
            elif choice == "M":
                self.modify_student()
            elif choice == "F":
                self.find_student()
            elif choice == "S":
                self.show_student()
            elif choice == "L":
                filename = input("Please enter filename: ")
                self.load_student(filename)
            elif choice == "K":
                filename = input("Please enter filename: ")
                self.save_student(filename)
            elif choice == "I":
                self.info_statistics()
            elif choice == "E":
                break
            else:
                print("Input error")


if __name__ == '__main__':
    st = Information()
    st.main()
