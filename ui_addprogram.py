# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addprogramzXVsKq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import pandas as pd
from data_handler import load_data, save_data

class Ui_AddProgram_Window(object):
    def setupUi(self, AddProgram_Window, main_window):
        if not AddProgram_Window.objectName():
            AddProgram_Window.setObjectName(u"AddProgram_Window")
        AddProgram_Window.resize(454, 320)
        self.centralwidget = QWidget(AddProgram_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #073b4c;\n"
"}\n"
"#frame_21, #frame_23{\n"
"	padding: 10px;\n"
"	background-color: #073b4c;\n"
"	border-radius: 10px;\n"
"}\n"
"#frame_22{\n"
"	padding: 10px;\n"
"	background-color: #06d6a0;\n"
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
"#plabel{\n"
"	color: #073b4c;\n"
"}")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_21 = QFrame(self.centralwidget)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_21)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_22 = QFrame(self.frame_21)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_22)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.plabel = QLabel(self.frame_22)
        self.plabel.setObjectName(u"plabel")
        font = QFont()
        font.setFamily(u"Montserrat ExtraBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.plabel.setFont(font)
        self.plabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.plabel, 0, 1, 1, 1)

        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_23)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.prog_college = QLabel(self.frame_23)
        self.prog_college.setObjectName(u"prog_college")
        font1 = QFont()
        font1.setFamily(u"Montserrat ExtraBold")
        self.prog_college.setFont(font1)

        self.verticalLayout.addWidget(self.prog_college)

        self.pcollege_info = QComboBox(self.frame_23)
        self.pcollege_info.setObjectName(u"pcollege_info")
        font2 = QFont()
        font2.setFamily(u"Montserrat SemiBold")
        self.pcollege_info.setFont(font2)

        self.verticalLayout.addWidget(self.pcollege_info)

        self.prog_name = QLabel(self.frame_23)
        self.prog_name.setObjectName(u"prog_name")
        self.prog_name.setFont(font1)

        self.verticalLayout.addWidget(self.prog_name)

        self.pname_info = QLineEdit(self.frame_23)
        self.pname_info.setObjectName(u"pname_info")
        self.pname_info.setFont(font2)

        self.verticalLayout.addWidget(self.pname_info)

        self.prog_code = QLabel(self.frame_23)
        self.prog_code.setObjectName(u"prog_code")
        self.prog_code.setFont(font1)

        self.verticalLayout.addWidget(self.prog_code)

        self.pcode_info = QLineEdit(self.frame_23)
        self.pcode_info.setObjectName(u"pcode_info")
        self.pcode_info.setFont(font2)

        self.verticalLayout.addWidget(self.pcode_info)


        self.gridLayout_3.addWidget(self.frame_23, 1, 0, 1, 3)

        self.padd_btn = QPushButton(self.frame_22)
        self.padd_btn.setObjectName(u"padd_btn")
        self.padd_btn.setFont(font2)

        self.gridLayout_3.addWidget(self.padd_btn, 2, 0, 1, 1)

        self.pclear_btn = QPushButton(self.frame_22)
        self.pclear_btn.setObjectName(u"pclear_btn")
        self.pclear_btn.setFont(font2)

        self.gridLayout_3.addWidget(self.pclear_btn, 2, 1, 1, 1)

        self.pcancel_btn = QPushButton(self.frame_22)
        self.pcancel_btn.setObjectName(u"pcancel_btn")
        self.pcancel_btn.setFont(font2)

        self.gridLayout_3.addWidget(self.pcancel_btn, 2, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_22, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_21, 0, 0, 1, 1)

######################################################################################################################
        self.main_window = main_window
        self.load_colleges()
        self.padd_btn.clicked.connect(self.add_program)
        self.pclear_btn.clicked.connect(self.clear_inputs)
        ## self.window = AddProgram_Window  # ✅ Store reference
        self.pcancel_btn.clicked.connect(self.cancel)  # ✅ Use stored reference
######################################################################################################################

        AddProgram_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddProgram_Window)

        QMetaObject.connectSlotsByName(AddProgram_Window)
    # setupUi

    def retranslateUi(self, AddProgram_Window):
        AddProgram_Window.setWindowTitle(QCoreApplication.translate("AddProgram_Window", u"MainWindow", None))
        self.plabel.setText(QCoreApplication.translate("AddProgram_Window", u"ADD PROGRAM", None))
        self.prog_college.setText(QCoreApplication.translate("AddProgram_Window", u"College", None))
        self.prog_name.setText(QCoreApplication.translate("AddProgram_Window", u"Name", None))
        self.prog_code.setText(QCoreApplication.translate("AddProgram_Window", u"Code", None))
        self.padd_btn.setText(QCoreApplication.translate("AddProgram_Window", u"Add", None))
        self.pclear_btn.setText(QCoreApplication.translate("AddProgram_Window", u"Clear", None))
        self.pcancel_btn.setText(QCoreApplication.translate("AddProgram_Window", u"Cancel", None))
    # retranslateUi

######################################################################################################################
    def setComboBoxPlaceholders(self):
        self.insertPlaceholder(self.pcollege_info, "Select College")

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
######################################################################################################################

######################################################################################################################
    def load_colleges(self):
        """Loads college names from data.csv into pcollege_info dropdown."""
        df = load_data("colleges")  # ✅ Use Pandas to load the CSV file

        if df.empty or not isinstance(df, pd.DataFrame): # added "or not isinstance(df, pd.DataFrame)"
            QMessageBox.warning(None, "Missing College Data", "No college data found.")
            return

        self.pcollege_info.clear()  # Clear existing items

        # Sort college names alphabetically before adding them
        sorted_colleges = df.sort_values(by="College Name")
            
        for _, row in sorted_colleges.iterrows():

            self.pcollege_info.addItem(row["College Name"], row["College Code"])

    def add_program(self):
        # Saves program details to data.csv using data_handler.py.
######################################################################################################################
        college_name = self.pcollege_info.currentText().strip()
        college_code = self.pcollege_info.currentData()
        program_name = self.pname_info.text().strip()
        program_code = self.pcode_info.text().strip()

        if college_name == "Select College" or not program_name or not program_code: # changed "college_code" to "college_name"
            QMessageBox.warning(None, "Incomplete Data", "Please fill out all fields before saving.")
            return

        df = load_data("programs")  # Load existing data
        
        if "College" not in df.columns or "Program Name" not in df.columns or "Program Code" not in df.columns:
            # If the columns are missing, reinitialize the DataFrame with the correct columns
            df = pd.DataFrame(columns=["College", "Program Name", "Program Code"])

        if not df.empty:
            if df["Program Name"].str.lower().eq(program_name.lower()).any():
                QMessageBox.warning(None, "Duplicate Program", f"A program with the name '{program_name}' already exists.")
                return
            
            if df["Program Code"].str.lower().eq(program_code.lower()).any():
                QMessageBox.warning(None, "Duplicate Program Code", f"A program with the code '{program_code}' already exists.")
                return

        # Add new program to the DataFrame
        new_program = pd.DataFrame([[college_code, program_name, program_code]], columns=["College", "Program Name", "Program Code"])  # changed "college" to "college_code"
        df = pd.concat([df, new_program], ignore_index=True)

        # Save the updated DataFrame
        save_data(df, "programs")

        # Reflect new row in college_table
        self.main_window.add_program_row(college_code, program_name, program_code)  # changed "college" to "college_code"

        self.main_window.add_program_window.close()  # Close window after saving

    def clear_inputs(self):
        """Clears input fields."""
        self.pname_info.clear()
        self.pcode_info.clear()

    def cancel(self):
        self.main_window.add_program_window.close()
######################################################################################################################