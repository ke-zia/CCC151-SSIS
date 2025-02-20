# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addcollegezUQTaN.ui'
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

class Ui_AddCollege_Window(object):
    def setupUi(self, AddCollege_Window, main_window): ######## Added main_window
        if not AddCollege_Window.objectName():
            AddCollege_Window.setObjectName(u"AddCollege_Window")
        AddCollege_Window.resize(454, 320)
        self.centralwidget = QWidget(AddCollege_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #073b4c;\n"
"}\n"
"#frame_3, #frame_5{\n"
"	padding: 10px;\n"
"	background-color: #073b4c;\n"
"	border-radius: 10px;\n"
"}\n"
"#frame_4{\n"
"	padding: 10px;\n"
"	background-color: #06d6a0;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"	padding: 5px;\n"
"	background-color: #118ab2;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit {\n"
"    color: black;\n"
"	padding: 3px;\n"
"    background-color: rgba(255, 255, 255, 0.6);\n"
"    border-radius: 5px;\n"
"}\n"
"#label{\n"
"	color: #073b4c;\n"
"}\n"
"")
        self.gridLayout_14 = QGridLayout(self.centralwidget)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_3)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.college_name = QLabel(self.frame_5)
        self.college_name.setObjectName(u"college_name")
        font = QFont()
        font.setFamily(u"Montserrat ExtraBold")
        self.college_name.setFont(font)

        self.verticalLayout_2.addWidget(self.college_name)

        self.cname_info = QLineEdit(self.frame_5)
        self.cname_info.setObjectName(u"cname_info")
        font1 = QFont()
        font1.setFamily(u"Montserrat SemiBold")
        self.cname_info.setFont(font1)

        self.verticalLayout_2.addWidget(self.cname_info)

        self.college_code = QLabel(self.frame_5)
        self.college_code.setObjectName(u"college_code")
        self.college_code.setFont(font)

        self.verticalLayout_2.addWidget(self.college_code)

        self.ccode_info = QLineEdit(self.frame_5)
        self.ccode_info.setObjectName(u"ccode_info")
        self.ccode_info.setFont(font1)

        self.verticalLayout_2.addWidget(self.ccode_info)


        self.gridLayout_13.addWidget(self.frame_5, 1, 0, 1, 3)

        self.ccancel_btn = QPushButton(self.frame_4)
        self.ccancel_btn.setObjectName(u"ccancel_btn")
        self.ccancel_btn.setFont(font1)

        self.gridLayout_13.addWidget(self.ccancel_btn, 2, 2, 1, 1)

        self.cadd_btn = QPushButton(self.frame_4)
        self.cadd_btn.setObjectName(u"cadd_btn")
        self.cadd_btn.setFont(font1)

        self.gridLayout_13.addWidget(self.cadd_btn, 2, 0, 1, 1)

        self.cclear_btn = QPushButton(self.frame_4)
        self.cclear_btn.setObjectName(u"cclear_btn")
        self.cclear_btn.setFont(font1)

        self.gridLayout_13.addWidget(self.cclear_btn, 2, 1, 1, 1)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamily(u"Montserrat ExtraBold")
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label, 0, 1, 1, 1)


        self.gridLayout_15.addWidget(self.frame_4, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_3, 0, 0, 1, 1)

######################################################################################################################
        self.main_window = main_window  # Store reference to main window
        self.cadd_btn.clicked.connect(self.add_college)
        self.cclear_btn.clicked.connect(self.clear_inputs)
        self.ccancel_btn.clicked.connect(self.cancel)
######################################################################################################################

        AddCollege_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddCollege_Window)

        QMetaObject.connectSlotsByName(AddCollege_Window)
    # setupUi

    def retranslateUi(self, AddCollege_Window):
        AddCollege_Window.setWindowTitle(QCoreApplication.translate("AddCollege_Window", u"MainWindow", None))
        self.college_name.setText(QCoreApplication.translate("AddCollege_Window", u"Name", None))
        self.college_code.setText(QCoreApplication.translate("AddCollege_Window", u"Code", None))
        self.ccancel_btn.setText(QCoreApplication.translate("AddCollege_Window", u"Cancel", None))
        self.cadd_btn.setText(QCoreApplication.translate("AddCollege_Window", u"Add", None))
        self.cclear_btn.setText(QCoreApplication.translate("AddCollege_Window", u"Clear", None))
        self.label.setText(QCoreApplication.translate("AddCollege_Window", u"ADD COLLEGE", None))
    # retranslateUi

######################################################################################################################
    def add_college(self):
        name = self.cname_info.text().strip()
        code = self.ccode_info.text().strip()

        # Validate fields
        if not name or not code:
            QMessageBox.warning(None, "Incomplete Data", "Please fill out all fields before saving.")
            return
        
        df = load_data("colleges")
        
        if "College Name" not in df.columns or "College Code" not in df.columns:
            # If the columns are missing, reinitialize the DataFrame with the correct columns
            df = pd.DataFrame(columns=["College Name", "College Code"])
        
        if not df.empty:
            if df["College Name"].str.lower().eq(name.lower()).any():
                QMessageBox.warning(None, "Duplicate College", f"A college with the name '{name}' already exists.")
                return

            if df["College Code"].str.lower().eq(code.lower()).any():
                QMessageBox.warning(None, "Duplicate College Code", f"A college with the code '{code}' already exists.")
                return

        new_college = pd.DataFrame([[name, code]], columns=["College Name", "College Code"])

        df = pd.concat([df, new_college], ignore_index=True)
        save_data(df, "colleges")

        # Update pcollege_info in add program window
        if hasattr(self.main_window, 'add_program_ui'):
            self.main_window.add_program_ui.load_colleges()

        # Reflect new row in college_table
        self.main_window.add_college_row(name, code)

        # Close window after successful save
        self.main_window.add_college_window.close()
            
    def clear_inputs(self):
        """Clears all input fields in AddCollege_Window."""
        self.cname_info.clear()
        self.ccode_info.clear()

    def cancel(self):
        """Closes the window without saving any data."""
        self.main_window.add_college_window.close()
######################################################################################################################