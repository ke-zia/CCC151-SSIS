from ui_interface import Ui_MainWindow
from college_operations import CollegeOperations
from program_operations import ProgramOperations
from student_operations import StudentOperations
from Custom_Widgets.Widgets import *
from PySide2.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.student_ops = StudentOperations(self.ui)
        self.program_ops = ProgramOperations(self.ui, self.student_ops)
        self.college_ops = CollegeOperations(self.ui, self.program_ops)

        self.ui.students.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.students_page))
        self.ui.colleges.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.colleges_page))
        self.ui.programs.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.programs_page))

        self.ui.stackedWidget.setCurrentWidget(self.ui.students_page)

        self.student_ops.load_students()
        self.college_ops.load_colleges()
        self.program_ops.load_programs()

        self.ui.addstdnt_btn.clicked.connect(self.open_add_student)
        self.ui.college_btn.clicked.connect(self.open_add_college)
        self.ui.program_btn.clicked.connect(self.open_add_program)

        self.ui.csearch_btn.clicked.connect(self.college_ops.search_colleges)
        self.ui.psearch_btn.clicked.connect(self.program_ops.search_programs)
        self.ui.search_btn.clicked.connect(self.student_ops.search_students)

        self.college_ops.setup_college_filter()
        self.program_ops.setup_program_filter()
        self.student_ops.setup_student_filter()

        loadJsonStyle(self, self.ui)
        self.ui.side_menu.setFixedWidth(0)
        self.show()

    def open_add_student(self):
        self.student_ops.open_add_student()

    def open_add_college(self):
        self.college_ops.open_add_college()

    def open_add_program(self):
        self.program_ops.open_add_program()