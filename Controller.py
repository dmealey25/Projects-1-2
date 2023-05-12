from project1 import *
from PyQt6.QtWidgets import *

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda: self.submit())
        self.pushButton_2.clicked.connect(lambda: self.clear())

    def calculate_grades(self):
        num_students = int(self.students_output.toPlainText())

        while num_students <= 0:
            num_students = int(self.students_output.toPlainText())

        scores_str = self.scores_output.toPlainText().split(" ")

        scores = []

        while len(scores_str) < num_students:
            scores_str = input(f' Enter {num_students} score(s): ').split()

        for score_str in scores_str:
            scores.append(int(score_str))

        while len(scores) > num_students:
            scores.pop()

        output_text = ""

        student = 0

        best_score = max(scores)

        for score in scores:
            student = student + 1
            if score >= best_score - 10:
                letter = "A"
            elif score >= best_score - 20:
                letter = "B"
            elif score >= best_score - 30:
                letter = "C"
            elif score >= best_score - 40:
                letter = "D"
            elif score < best_score - 40:
                letter = "F"
            self.output.setText(f"Student {student} score is {score} and grade is {letter}")


