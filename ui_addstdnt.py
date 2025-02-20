# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addstdntYIIfKX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import re
import pandas as pd
from data_handler import load_data, save_data

class Ui_AddStdnt_Window(object):
    def setupUi(self, AddStdnt_Window, main_window):
        if not AddStdnt_Window.objectName():
            AddStdnt_Window.setObjectName(u"AddStdnt_Window")
        AddStdnt_Window.resize(756, 422)
        font = QFont()
        font.setFamily(u"Montserrat SemiBold")
        AddStdnt_Window.setFont(font)
        self.centralwidget = QWidget(AddStdnt_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #073b4c;\n"
"}\n"
"#frame_2{\n"
"	padding: 10px;\n"
"	background-color: #06d6a0;\n"
"	border-radius: 10px;\n"
"}\n"
"#name_header, #college_header{\n"
"	padding: 10px;\n"
"	background-color: #073b4c;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"	padding: 5px;\n"
"	background-color: #118ab2;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit, QComboBox {\n"
"    color: black;\n"
"	padding: 3px;\n"
"    background-color: rgba(255, 255, 255, 0.6);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.name_header = QFrame(self.frame_2)
        self.name_header.setObjectName(u"name_header")
        self.name_header.setFrameShape(QFrame.StyledPanel)
        self.name_header.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.name_header)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(0)
        self.first_n = QLabel(self.name_header)
        self.first_n.setObjectName(u"first_n")
        font1 = QFont()
        font1.setFamily(u"Montserrat ExtraBold")
        font1.setBold(True)
        font1.setWeight(75)
        self.first_n.setFont(font1)

        self.gridLayout_2.addWidget(self.first_n, 0, 0, 1, 1)

        self.year_lvl = QLabel(self.name_header)
        self.year_lvl.setObjectName(u"year_lvl")
        self.year_lvl.setFont(font1)

        self.gridLayout_2.addWidget(self.year_lvl, 0, 1, 1, 1)

        self.firstn_info = QLineEdit(self.name_header)
        self.firstn_info.setObjectName(u"firstn_info")
        font2 = QFont()
        font2.setFamily(u"Montserrat SemiBold")
        font2.setBold(True)
        font2.setWeight(75)
        self.firstn_info.setFont(font2)

        self.gridLayout_2.addWidget(self.firstn_info, 1, 0, 1, 1)

        self.yearlvl_info = QComboBox(self.name_header)
        self.yearlvl_info.addItem("")
        self.yearlvl_info.addItem("")
        self.yearlvl_info.addItem("")
        self.yearlvl_info.addItem("")
        self.yearlvl_info.addItem("")
        self.yearlvl_info.setObjectName(u"yearlvl_info")
        self.yearlvl_info.setFont(font2)

        self.gridLayout_2.addWidget(self.yearlvl_info, 1, 1, 1, 1)

        self.last_n = QLabel(self.name_header)
        self.last_n.setObjectName(u"last_n")
        self.last_n.setFont(font1)

        self.gridLayout_2.addWidget(self.last_n, 2, 0, 1, 1)

        self.id_num = QLabel(self.name_header)
        self.id_num.setObjectName(u"id_num")
        self.id_num.setFont(font1)

        self.gridLayout_2.addWidget(self.id_num, 2, 1, 1, 1)

        self.lastn_info = QLineEdit(self.name_header)
        self.lastn_info.setObjectName(u"lastn_info")
        self.lastn_info.setFont(font2)

        self.gridLayout_2.addWidget(self.lastn_info, 3, 0, 1, 1)

        self.idnum_info = QLineEdit(self.name_header)
        self.idnum_info.setObjectName(u"idnum_info")
        self.idnum_info.setFont(font2)

        self.gridLayout_2.addWidget(self.idnum_info, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.name_header, 0, 0, 1, 3)

        self.college_header = QFrame(self.frame_2)
        self.college_header.setObjectName(u"college_header")
        self.college_header.setMaximumSize(QSize(16777215, 16777215))
        self.college_header.setFrameShape(QFrame.StyledPanel)
        self.college_header.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.college_header)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gender_frame = QFrame(self.college_header)
        self.gender_frame.setObjectName(u"gender_frame")
        self.gender_frame.setMinimumSize(QSize(0, 70))
        self.gender_frame.setMaximumSize(QSize(16777215, 70))
        self.gender_frame.setFrameShape(QFrame.StyledPanel)
        self.gender_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.gender_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(0)
        self.gender = QLabel(self.gender_frame)
        self.gender.setObjectName(u"gender")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gender.sizePolicy().hasHeightForWidth())
        self.gender.setSizePolicy(sizePolicy)
        self.gender.setMaximumSize(QSize(16777215, 16))
        self.gender.setFont(font1)

        self.gridLayout_3.addWidget(self.gender, 0, 0, 1, 1)

        self.gender_info = QComboBox(self.gender_frame)
        self.gender_info.addItem("")
        self.gender_info.addItem("")
        self.gender_info.addItem("Others")
        self.gender_info.setObjectName(u"gender_info")
        self.gender_info.setFont(font2)

        self.gridLayout_3.addWidget(self.gender_info, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.gender_frame, 0, 0, 1, 1)

        self.college_frame = QFrame(self.college_header)
        self.college_frame.setObjectName(u"college_frame")
        self.college_frame.setMinimumSize(QSize(0, 70))
        self.college_frame.setMaximumSize(QSize(16777215, 70))
        self.college_frame.setFrameShape(QFrame.StyledPanel)
        self.college_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.college_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(0)
        self.college = QLabel(self.college_frame)
        self.college.setObjectName(u"college")
        sizePolicy.setHeightForWidth(self.college.sizePolicy().hasHeightForWidth())
        self.college.setSizePolicy(sizePolicy)
        self.college.setMaximumSize(QSize(16777215, 16))
        self.college.setFont(font1)

        self.gridLayout_4.addWidget(self.college, 1, 0, 1, 1)

        self.college_info = QComboBox(self.college_frame)
        self.college_info.setObjectName(u"college_info")
        self.college_info.setFont(font)

        self.gridLayout_4.addWidget(self.college_info, 2, 0, 1, 1)


        self.gridLayout_6.addWidget(self.college_frame, 0, 1, 1, 1)

        self.program_frame = QFrame(self.college_header)
        self.program_frame.setObjectName(u"program_frame")
        self.program_frame.setMinimumSize(QSize(0, 70))
        self.program_frame.setMaximumSize(QSize(16777215, 70))
        self.program_frame.setFrameShape(QFrame.StyledPanel)
        self.program_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.program_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(0)
        self.program = QLabel(self.program_frame)
        self.program.setObjectName(u"program")
        sizePolicy.setHeightForWidth(self.program.sizePolicy().hasHeightForWidth())
        self.program.setSizePolicy(sizePolicy)
        self.program.setMaximumSize(QSize(16777215, 16))
        self.program.setFont(font1)

        self.gridLayout_5.addWidget(self.program, 0, 0, 1, 1)

        self.program_info = QComboBox(self.program_frame)
        self.program_info.setObjectName(u"program_info")
        self.program_info.setFont(font)

        self.gridLayout_5.addWidget(self.program_info, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.program_frame, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.college_header, 1, 0, 1, 3)

        self.add_btn = QPushButton(self.frame_2)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setFont(font)

        self.gridLayout.addWidget(self.add_btn, 2, 0, 1, 1)

        self.clear_btn = QPushButton(self.frame_2)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setFont(font)

        self.gridLayout.addWidget(self.clear_btn, 2, 1, 1, 1)

        self.cancel_btn = QPushButton(self.frame_2)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setFont(font)

        self.gridLayout.addWidget(self.cancel_btn, 2, 2, 1, 1)

        self.verticalLayout.addWidget(self.frame_2)

        self.horizontalLayout.addWidget(self.frame)

######################################################################################################################
        self.main_window = main_window
        self.populate_colleges()

        self.idnum_info.textChanged.connect(self.validate_id)
        self.college_info.currentIndexChanged.connect(self.populate_programs)
        self.add_btn.clicked.connect(self.add_student)
        self.clear_btn.clicked.connect(self.clear_inputs)
        self.cancel_btn.clicked.connect(self.cancel)
######################################################################################################################

        AddStdnt_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddStdnt_Window)

        QMetaObject.connectSlotsByName(AddStdnt_Window)
    # setupUi

    def retranslateUi(self, AddStdnt_Window):
        AddStdnt_Window.setWindowTitle(QCoreApplication.translate("AddStdnt_Window", u"MainWindow", None))
        self.first_n.setText(QCoreApplication.translate("AddStdnt_Window", u"First Name", None))
        self.year_lvl.setText(QCoreApplication.translate("AddStdnt_Window", u"Year Level", None))
        self.firstn_info.setPlaceholderText("")
        self.yearlvl_info.setItemText(0, QCoreApplication.translate("AddStdnt_Window", u"1", None))
        self.yearlvl_info.setItemText(1, QCoreApplication.translate("AddStdnt_Window", u"2", None))
        self.yearlvl_info.setItemText(2, QCoreApplication.translate("AddStdnt_Window", u"3", None))
        self.yearlvl_info.setItemText(3, QCoreApplication.translate("AddStdnt_Window", u"4", None))
        self.yearlvl_info.setItemText(4, QCoreApplication.translate("AddStdnt_Window", u"5", None))

        self.last_n.setText(QCoreApplication.translate("AddStdnt_Window", u"Last Name", None))
        self.id_num.setText(QCoreApplication.translate("AddStdnt_Window", u"ID Number", None))
        self.lastn_info.setPlaceholderText("")
        self.idnum_info.setPlaceholderText(QCoreApplication.translate("AddStdnt_Window", u"YYYY-NNNN", None))
        self.gender.setText(QCoreApplication.translate("AddStdnt_Window", u"Gender", None))
        self.gender_info.setItemText(0, QCoreApplication.translate("AddStdnt_Window", u"Female", None))
        self.gender_info.setItemText(1, QCoreApplication.translate("AddStdnt_Window", u"Male", None))

        self.college.setText(QCoreApplication.translate("AddStdnt_Window", u"College", None))
        self.program.setText(QCoreApplication.translate("AddStdnt_Window", u"Program", None))
        self.add_btn.setText(QCoreApplication.translate("AddStdnt_Window", u"Add Student", None))
        self.clear_btn.setText(QCoreApplication.translate("AddStdnt_Window", u"Clear", None))
        self.cancel_btn.setText(QCoreApplication.translate("AddStdnt_Window", u"Cancel", None))
    # retranslateUi

#################################################################################################################
    def setComboBoxPlaceholders(self):
        self.insertPlaceholder(self.yearlvl_info, "Select Year Level")
        self.insertPlaceholder(self.gender_info, "Select Gender")
        self.insertPlaceholder(self.college_info, "Select College")

    def insertPlaceholder(self, combobox, placeholder_text):
        combobox.insertItem(0, placeholder_text)  # Insert at index 0
        combobox.setCurrentIndex(0)  # Select the placeholder
        combobox.setStyleSheet("color: gray;")  # Make it look faint

        # Change text color when selecting a real option
        combobox.currentIndexChanged.connect(lambda: self.restoreTextColor(combobox))

    def restoreTextColor(self, combobox):
        if combobox.currentIndex() == 0:
            combobox.setStyleSheet("color: gray;")
        else:
            combobox.setStyleSheet("color: black;")
#################################################################################################################

######################################################################################################################
    def validate_id(self):
        pattern = re.compile(r"^\d{4}-\d{4}$")
        text = self.idnum_info.text()
        if pattern.match(text):
            self.idnum_info.setStyleSheet("border: 2px solid green;")
        else:
            self.idnum_info.setStyleSheet("border: 2px solid red;")

    def populate_colleges(self):
        self.college_info.clear()
        df_colleges = load_data("colleges")
        df_programs = load_data("programs")
        
        # Get unique colleges that have programs
        colleges_with_programs = df_programs["College"].unique()
        
        # Filter colleges to only include those with programs
        filtered_colleges = df_colleges[df_colleges["College Code"].isin(colleges_with_programs)]
        
        sorted_colleges = filtered_colleges.sort_values(by="College Name")
        
        # Add sorted names to the combobox

        for _, row in sorted_colleges.iterrows():
            college_name = row["College Name"]
            college_code = row["College Code"]
            self.college_info.addItem(college_name, college_code)

        self.populate_programs()

    def populate_programs(self):
        self.program_info.clear()
        selected_college_code = self.college_info.currentData()  # Retrieve the college code
        
        if not selected_college_code:
            return  # No valid college selected

        df = load_data("programs")
        df = df[df["College"] == selected_college_code]

        sorted_programs = df.sort_values(by="Program Name")

        # Add program names to the combobox and store program codes as data
        for _, row in sorted_programs.iterrows():
            program_name = row["Program Name"]
            program_code = row["Program Code"]
            self.program_info.addItem(program_name, program_code)  # Add name and store code as data\

    def add_student(self):
        first_name = self.firstn_info.text().strip()
        last_name = self.lastn_info.text().strip()
        id_number = self.idnum_info.text().strip()
        year_level = self.yearlvl_info.currentText().strip()
        gender = self.gender_info.currentText().strip()
        program_name = self.program_info.currentText().strip()
        program_code = self.program_info.currentData()  # Retrieve the program code from the combobox data

        df = load_data("students")

        # Check if ID number already exists
        if id_number in df["ID Number"].values:
            QMessageBox.warning(None, "Duplicate ID", "This ID number is already registered.")
            return

        # Validate fields
        if (not first_name or not last_name or not id_number or not year_level or gender == "Select Gender" or not program_name):  # changed "college" to "college_name", "program" to "program_name"
            QMessageBox.warning(None, "Incomplete Data", "Please fill out all fields before saving.")
            return

        if not re.match(r"^\d{4}-\d{4}$", id_number):
            QMessageBox.warning(None, "Invalid ID", "ID format must be YYYY-NNNN.")
            return

        # Create new student data
        new_student = {
            "First Name": first_name,
            "Last Name": last_name,
            "ID Number": id_number,
            "Year Level": year_level,
            "Gender": gender,
            "Program": program_code  # changed "program" to "program_code"
        }

        new_student_df = pd.DataFrame([new_student])

        df = pd.concat([df, new_student_df], ignore_index=True)
        save_data(df, "students")

        # Reflect new row in college_table
        self.main_window.add_student_row(first_name, last_name, id_number, year_level, gender, program_code)  # changed "college" to "college_code", "program" to "program_code"

        # Close window after successful save
        self.main_window.add_student_window.close()

    def clear_inputs(self):
        """Clears all input fields in AddStdnt_Window."""
        self.firstn_info.clear()
        self.lastn_info.clear()
        self.idnum_info.clear()
        self.yearlvl_info.setCurrentIndex(0)  # Reset to first option
        self.gender_info.setCurrentIndex(0)  # Reset to first option
        self.program_info.setCurrentIndex(0)  # Reset to first option

    def cancel(self):
        """Closes the window without saving any data."""
        self.main_window.add_student_window.close()
######################################################################################################################