# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacegxxMVa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(986, 623)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #073b4c;\n"
"}\n"
"#side_menu{\n"
"	background-color: #118ab2;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: #118ab2;\n"
"	border-radius: 10px;\n"
"}\n"
"#dashboard, #students, #colleges, #programs{\n"
"	padding: 10px;\n"
"	background-color: #073b4c;\n"
"	border-radius: 10px;\n"
"}\n"
"#total_students{\n"
"	padding: 10px;\n"
"	background-color: #ef476f;\n"
"	border-radius: 10px;\n"
"}\n"
"#create_dash{\n"
"	padding: 10px;\n"
"	background-color: #ffd166;\n"
"	border-radius: 10px;\n"
"}\n"
"#college_pie{\n"
"	padding: 10px;\n"
"	background-color: #06d6a0;\n"
"	border-radius: 10px;\n"
"}\n"
"#frame_7, #ctable_header, #ptable_header{\n"
"	padding: 10px;\n"
"	background-color: #06d6a0;\n"
"	border-radius: 5px;\n"
"}\n"
"#main_body{\n"
"	background-color: #06d6a0;\n"
"	border-radius: 10px;\n"
"}\n"
"#fill{\n"
"	background-color: #073b4c;\n"
"	borde"
                        "r-radius: 8px;\n"
"}\n"
"#filter_header, #csearch_header, #pfilter_header, #psearch_header{\n"
"	padding: 10px;\n"
"	background-color: #ef476f;\n"
"	border-radius: 5px;\n"
"}\n"
"#add_header, #cadd_header, #padd_header{\n"
"	padding: 3px;\n"
"	background-color: #ffd166;\n"
"	border-radius: 5px;\n"
"}\n"
"#search_bar, #filter_bar, #searchby_bar, #csearch_bar, #pfilter_bar,#psearch_bar, #cfilter_bar, #csearchby_bar, #psearchby_bar {\n"
"    padding: 3px;\n"
"    background-color: rgba(255, 255, 255, 0.6);\n"
"    border-radius: 5px;\n"
"}\n"
"QLineEdit, QComboBox {\n"
"    color: black;\n"
"}\n"
"QTableWidget {\n"
"    color: white;\n"
"    background-color: #118ab2;\n"
"	alternate-background-color: #107191;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #073b4c; \n"
"    color: white;\n"
"    padding: 5px;\n"
"}\n"
"#addstdnt_btn, #excel_btn, #pdf_btn, #college_btn, #search_btn, #csearch_btn, #psearch_btn, #program_btn, #psearch_btn{\n"
"	padding: 5px;\n"
"	background-color: #118ab2;\n"
"	border-rad"
                        "ius: 5px;\n"
"}\n"
"#text_frame, #ctext_frame, #ptext_frame, #ctable_frame, #stable_frame, #ptable_frame{\n"
"	padding: 3px;\n"
"	background-color: #073b4c;\n"
"	border-radius: 7px;\n"
"}\n"
"#header{\n"
"	background-color: #118ab2;\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Menu = QPushButton(self.frame)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setMinimumSize(QSize(0, 35))
        self.Menu.setMaximumSize(QSize(16777215, 35))
        font = QFont()
        font.setFamily(u"Montserrat SemiBold")
        font.setBold(True)
        font.setWeight(75)
        self.Menu.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu.setIcon(icon1)
        self.Menu.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.Menu)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        font1 = QFont()
        font1.setPointSize(10)
        self.frame_3.setFont(font1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 10, 0)
        self.SSIS = QLabel(self.frame_3)
        self.SSIS.setObjectName(u"SSIS")
        font2 = QFont()
        font2.setFamily(u"Montserrat ExtraBold")
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.SSIS.setFont(font2)
        self.SSIS.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.SSIS)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.header)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.side_menu = QCustomSlideMenu(self.frame_2)
        self.side_menu.setObjectName(u"side_menu")
        self.verticalLayout_2 = QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.side_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(150, 0))
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.students = QPushButton(self.frame_4)
        self.students.setObjectName(u"students")
        self.students.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.students.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.students)

        self.colleges = QPushButton(self.frame_4)
        self.colleges.setObjectName(u"colleges")
        font3 = QFont()
        font3.setFamily(u"Montserrat SemiBold")
        self.colleges.setFont(font3)
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/star.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.colleges.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.colleges)

        self.programs = QPushButton(self.frame_4)
        self.programs.setObjectName(u"programs")
        self.programs.setFont(font3)
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/pen-tool.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.programs.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.programs)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignTop)


        self.gridLayout_3.addWidget(self.side_menu, 0, 0, 1, 1)

        self.main_body = QFrame(self.frame_2)
        self.main_body.setObjectName(u"main_body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy1)
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.main_body)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.fill = QFrame(self.main_body)
        self.fill.setObjectName(u"fill")
        self.fill.setStyleSheet(u"")
        self.fill.setFrameShape(QFrame.StyledPanel)
        self.fill.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.fill)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.fill)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.gridLayout_2 = QGridLayout(self.dashboard_page)
        self.gridLayout_2.setSpacing(20)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(20, 20, 20, 20)
        self.stackedWidget.addWidget(self.dashboard_page)
        self.students_page = QWidget()
        self.students_page.setObjectName(u"students_page")
        self.gridLayout_5 = QGridLayout(self.students_page)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.add_header = QFrame(self.students_page)
        self.add_header.setObjectName(u"add_header")
        sizePolicy.setHeightForWidth(self.add_header.sizePolicy().hasHeightForWidth())
        self.add_header.setSizePolicy(sizePolicy)
        self.add_header.setMinimumSize(QSize(0, 80))
        self.add_header.setMaximumSize(QSize(16777215, 80))
        self.add_header.setFrameShape(QFrame.StyledPanel)
        self.add_header.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.add_header)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(7, 0, 7, 0)
        self.text_frame = QFrame(self.add_header)
        self.text_frame.setObjectName(u"text_frame")
        self.text_frame.setMinimumSize(QSize(260, 70))
        self.text_frame.setMaximumSize(QSize(260, 70))
        self.text_frame.setFrameShape(QFrame.StyledPanel)
        self.text_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.text_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(7, 0, 0, 0)
        self.body = QPlainTextEdit(self.text_frame)
        self.body.setObjectName(u"body")
        self.body.setMinimumSize(QSize(250, 0))
        self.body.setMaximumSize(QSize(250, 16777215))
        font4 = QFont()
        font4.setFamily(u"Montserrat Light")
        font4.setPointSize(8)
        font4.setBold(False)
        font4.setWeight(50)
        self.body.setFont(font4)
        self.body.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.body.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.body.setReadOnly(True)

        self.gridLayout_6.addWidget(self.body, 1, 0, 1, 2)

        self.icon = QLabel(self.text_frame)
        self.icon.setObjectName(u"icon")
        self.icon.setMaximumSize(QSize(25, 16777215))
        self.icon.setPixmap(QPixmap(u":/newPrefix/icons/users.svg"))

        self.gridLayout_6.addWidget(self.icon, 0, 0, 1, 1)

        self.title = QLabel(self.text_frame)
        self.title.setObjectName(u"title")
        font5 = QFont()
        font5.setFamily(u"Montserrat ExtraBold")
        font5.setPointSize(9)
        font5.setBold(True)
        font5.setWeight(75)
        self.title.setFont(font5)

        self.gridLayout_6.addWidget(self.title, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.text_frame, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(104, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.btns_frame = QFrame(self.add_header)
        self.btns_frame.setObjectName(u"btns_frame")
        self.btns_frame.setMinimumSize(QSize(350, 70))
        self.btns_frame.setMaximumSize(QSize(350, 70))
        self.btns_frame.setFrameShape(QFrame.StyledPanel)
        self.btns_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.btns_frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.addstdnt_btn = QPushButton(self.btns_frame)
        self.addstdnt_btn.setObjectName(u"addstdnt_btn")
        self.addstdnt_btn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icons/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addstdnt_btn.setIcon(icon5)

        self.gridLayout_7.addWidget(self.addstdnt_btn, 0, 1, 1, 1)


        self.gridLayout_8.addWidget(self.btns_frame, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.add_header, 0, 0, 1, 1)

        self.filter_header = QFrame(self.students_page)
        self.filter_header.setObjectName(u"filter_header")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.filter_header.sizePolicy().hasHeightForWidth())
        self.filter_header.setSizePolicy(sizePolicy2)
        self.filter_header.setMinimumSize(QSize(0, 50))
        self.filter_header.setMaximumSize(QSize(16777215, 50))
        self.filter_header.setFrameShape(QFrame.StyledPanel)
        self.filter_header.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.filter_header)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.filter_header)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(200, 0))
        self.frame_6.setMaximumSize(QSize(200, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_6)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(25, 0))
        self.label_2.setMaximumSize(QSize(25, 16777215))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/icons/filter.svg"))

        self.gridLayout_15.addWidget(self.label_2, 0, 0, 1, 1)

        self.filter_bar = QComboBox(self.frame_6)
        self.filter_bar.addItem("")
        self.filter_bar.addItem("")
        self.filter_bar.addItem("")
        self.filter_bar.addItem("")
        self.filter_bar.addItem("")
        self.filter_bar.addItem("")
        self.filter_bar.setObjectName(u"filter_bar")
        self.filter_bar.setMinimumSize(QSize(160, 0))
        self.filter_bar.setMaximumSize(QSize(160, 16777215))
        self.filter_bar.setFont(font)

        self.gridLayout_15.addWidget(self.filter_bar, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_6, 0, 0, 1, 1)

        self.searchby_bar = QComboBox(self.filter_header)
        self.searchby_bar.addItem("")
        self.searchby_bar.addItem("")
        self.searchby_bar.addItem("")
        self.searchby_bar.addItem("")
        self.searchby_bar.addItem("")
        self.searchby_bar.addItem("")
        self.searchby_bar.setObjectName(u"searchby_bar")
        self.searchby_bar.setMinimumSize(QSize(160, 0))
        self.searchby_bar.setMaximumSize(QSize(160, 16777215))
        self.searchby_bar.setFont(font)

        self.gridLayout_4.addWidget(self.searchby_bar, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(147, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 0, 2, 1, 1)

        self.frame_5 = QFrame(self.filter_header)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.search_bar = QLineEdit(self.frame_5)
        self.search_bar.setObjectName(u"search_bar")
        self.search_bar.setMinimumSize(QSize(0, 0))
        self.search_bar.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setFamily(u"Montserrat SemiBold")
        font6.setPointSize(8)
        self.search_bar.setFont(font6)

        self.horizontalLayout_5.addWidget(self.search_bar)

        self.search_btn = QPushButton(self.frame_5)
        self.search_btn.setObjectName(u"search_btn")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.search_btn)


        self.gridLayout_4.addWidget(self.frame_5, 0, 3, 1, 1)


        self.gridLayout_5.addWidget(self.filter_header, 1, 0, 1, 1)

        self.frame_7 = QFrame(self.students_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_7)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.student_table = QTableWidget(self.frame_7)
        if (self.student_table.columnCount() < 7):
            self.student_table.setColumnCount(7)
        font7 = QFont()
        font7.setFamily(u"Montserrat ExtraBold")
        font7.setBold(True)
        font7.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font7);
        self.student_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font8 = QFont()
        font8.setFamily(u"Montserrat ExtraBold")
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font8);
        self.student_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font8);
        self.student_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font8);
        self.student_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font8);
        self.student_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font8);
        self.student_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font8);
        self.student_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.student_table.setObjectName(u"student_table")
        self.student_table.setAlternatingRowColors(True)
        self.student_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.student_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.gridLayout_23.addWidget(self.student_table, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_7, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.students_page)
        self.colleges_page = QWidget()
        self.colleges_page.setObjectName(u"colleges_page")
        self.gridLayout_13 = QGridLayout(self.colleges_page)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.ctable_header = QFrame(self.colleges_page)
        self.ctable_header.setObjectName(u"ctable_header")
        self.ctable_header.setFrameShape(QFrame.StyledPanel)
        self.ctable_header.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.ctable_header)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.college_table = QTableWidget(self.ctable_header)
        if (self.college_table.columnCount() < 3):
            self.college_table.setColumnCount(3)
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font8);
        __qtablewidgetitem7.setBackground(QColor(239, 71, 111));
        __qtablewidgetitem7.setForeground(brush);
        self.college_table.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font7);
        __qtablewidgetitem8.setBackground(QColor(237, 70, 110));
        __qtablewidgetitem8.setForeground(brush1);
        self.college_table.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font8);
        self.college_table.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        self.college_table.setObjectName(u"college_table")
        self.college_table.setAlternatingRowColors(True)
        self.college_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.college_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.gridLayout_12.addWidget(self.college_table, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.ctable_header, 2, 0, 1, 1)

        self.csearch_header = QFrame(self.colleges_page)
        self.csearch_header.setObjectName(u"csearch_header")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(50)
        sizePolicy3.setHeightForWidth(self.csearch_header.sizePolicy().hasHeightForWidth())
        self.csearch_header.setSizePolicy(sizePolicy3)
        self.csearch_header.setMinimumSize(QSize(0, 50))
        self.csearch_header.setMaximumSize(QSize(16777215, 50))
        self.csearch_header.setFrameShape(QFrame.StyledPanel)
        self.csearch_header.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.csearch_header)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.csearch_header)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(200, 0))
        self.frame_9.setMaximumSize(QSize(200, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(25, 0))
        self.label_4.setMaximumSize(QSize(25, 16777215))
        self.label_4.setPixmap(QPixmap(u":/newPrefix/icons/filter.svg"))

        self.horizontalLayout_7.addWidget(self.label_4)

        self.cfilter_bar = QComboBox(self.frame_9)
        self.cfilter_bar.addItem("")
        self.cfilter_bar.addItem("")
        self.cfilter_bar.setObjectName(u"cfilter_bar")
        self.cfilter_bar.setMinimumSize(QSize(160, 0))
        self.cfilter_bar.setMaximumSize(QSize(160, 16777215))
        self.cfilter_bar.setFont(font)

        self.horizontalLayout_7.addWidget(self.cfilter_bar)


        self.gridLayout_11.addWidget(self.frame_9, 0, 0, 1, 1)

        self.csearchby_bar = QComboBox(self.csearch_header)
        self.csearchby_bar.addItem("")
        self.csearchby_bar.addItem("")
        self.csearchby_bar.setObjectName(u"csearchby_bar")
        self.csearchby_bar.setMinimumSize(QSize(160, 0))
        self.csearchby_bar.setMaximumSize(QSize(160, 16777215))
        self.csearchby_bar.setFont(font)

        self.gridLayout_11.addWidget(self.csearchby_bar, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(147, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.csearch_bar = QLineEdit(self.csearch_header)
        self.csearch_bar.setObjectName(u"csearch_bar")
        self.csearch_bar.setMinimumSize(QSize(159, 0))
        self.csearch_bar.setFont(font)

        self.gridLayout_11.addWidget(self.csearch_bar, 0, 3, 1, 1)

        self.csearch_btn = QPushButton(self.csearch_header)
        self.csearch_btn.setObjectName(u"csearch_btn")
        self.csearch_btn.setIcon(icon6)

        self.gridLayout_11.addWidget(self.csearch_btn, 0, 4, 1, 1)


        self.gridLayout_13.addWidget(self.csearch_header, 1, 0, 1, 1)

        self.cadd_header = QFrame(self.colleges_page)
        self.cadd_header.setObjectName(u"cadd_header")
        self.cadd_header.setMaximumSize(QSize(16777215, 79))
        self.cadd_header.setFrameShape(QFrame.StyledPanel)
        self.cadd_header.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.cadd_header)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(7, 0, 7, 0)
        self.ctext_frame = QFrame(self.cadd_header)
        self.ctext_frame.setObjectName(u"ctext_frame")
        self.ctext_frame.setMinimumSize(QSize(245, 55))
        self.ctext_frame.setMaximumSize(QSize(245, 55))
        self.ctext_frame.setFrameShape(QFrame.StyledPanel)
        self.ctext_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.ctext_frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setVerticalSpacing(0)
        self.gridLayout_9.setContentsMargins(7, 3, 0, 0)
        self.cicon = QLabel(self.ctext_frame)
        self.cicon.setObjectName(u"cicon")
        self.cicon.setMaximumSize(QSize(25, 16777215))
        self.cicon.setPixmap(QPixmap(u":/newPrefix/icons/book.svg"))

        self.gridLayout_9.addWidget(self.cicon, 0, 0, 1, 1)

        self.ctitle = QLabel(self.ctext_frame)
        self.ctitle.setObjectName(u"ctitle")
        self.ctitle.setFont(font5)

        self.gridLayout_9.addWidget(self.ctitle, 0, 1, 1, 1)

        self.cbody = QPlainTextEdit(self.ctext_frame)
        self.cbody.setObjectName(u"cbody")
        font9 = QFont()
        font9.setFamily(u"Montserrat Light")
        self.cbody.setFont(font9)
        self.cbody.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.cbody.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_9.addWidget(self.cbody, 1, 0, 1, 2)


        self.gridLayout_10.addWidget(self.ctext_frame, 0, 0, 1, 1)

        self.college_btn = QPushButton(self.cadd_header)
        self.college_btn.setObjectName(u"college_btn")
        self.college_btn.setMinimumSize(QSize(140, 31))
        self.college_btn.setMaximumSize(QSize(140, 31))
        self.college_btn.setFont(font3)
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/icons/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.college_btn.setIcon(icon7)

        self.gridLayout_10.addWidget(self.college_btn, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(329, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)


        self.gridLayout_13.addWidget(self.cadd_header, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.colleges_page)
        self.programs_page = QWidget()
        self.programs_page.setObjectName(u"programs_page")
        self.gridLayout_22 = QGridLayout(self.programs_page)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.padd_header = QFrame(self.programs_page)
        self.padd_header.setObjectName(u"padd_header")
        self.padd_header.setMaximumSize(QSize(16777215, 79))
        self.padd_header.setFrameShape(QFrame.StyledPanel)
        self.padd_header.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.padd_header)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(7, 0, 7, 0)
        self.program_btn = QPushButton(self.padd_header)
        self.program_btn.setObjectName(u"program_btn")
        self.program_btn.setMinimumSize(QSize(140, 31))
        self.program_btn.setMaximumSize(QSize(140, 31))
        self.program_btn.setFont(font3)
        self.program_btn.setIcon(icon7)

        self.gridLayout_16.addWidget(self.program_btn, 0, 2, 1, 1)

        self.ptext_frame = QFrame(self.padd_header)
        self.ptext_frame.setObjectName(u"ptext_frame")
        self.ptext_frame.setMinimumSize(QSize(245, 55))
        self.ptext_frame.setMaximumSize(QSize(245, 55))
        self.ptext_frame.setFrameShape(QFrame.StyledPanel)
        self.ptext_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.ptext_frame)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setVerticalSpacing(0)
        self.gridLayout_17.setContentsMargins(7, 3, 0, 0)
        self.picon = QLabel(self.ptext_frame)
        self.picon.setObjectName(u"picon")
        self.picon.setMaximumSize(QSize(25, 16777215))
        self.picon.setPixmap(QPixmap(u":/newPrefix/icons/box.svg"))

        self.gridLayout_17.addWidget(self.picon, 0, 0, 1, 1)

        self.ptitle = QLabel(self.ptext_frame)
        self.ptitle.setObjectName(u"ptitle")
        self.ptitle.setFont(font5)

        self.gridLayout_17.addWidget(self.ptitle, 0, 1, 1, 1)

        self.pbody = QPlainTextEdit(self.ptext_frame)
        self.pbody.setObjectName(u"pbody")
        self.pbody.setFont(font9)
        self.pbody.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pbody.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_17.addWidget(self.pbody, 1, 0, 1, 2)


        self.gridLayout_16.addWidget(self.ptext_frame, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(341, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)


        self.gridLayout_22.addWidget(self.padd_header, 0, 0, 1, 1)

        self.psearch_header = QFrame(self.programs_page)
        self.psearch_header.setObjectName(u"psearch_header")
        self.psearch_header.setMinimumSize(QSize(0, 50))
        self.psearch_header.setMaximumSize(QSize(16777215, 50))
        self.psearch_header.setFrameShape(QFrame.StyledPanel)
        self.psearch_header.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.psearch_header)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.psearch_header)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(200, 0))
        self.frame_8.setMaximumSize(QSize(200, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(25, 0))
        self.label_3.setMaximumSize(QSize(25, 16777215))
        self.label_3.setPixmap(QPixmap(u":/newPrefix/icons/filter.svg"))

        self.horizontalLayout_6.addWidget(self.label_3)

        self.pfilter_bar = QComboBox(self.frame_8)
        self.pfilter_bar.addItem("")
        self.pfilter_bar.addItem("")
        self.pfilter_bar.addItem("")
        self.pfilter_bar.setObjectName(u"pfilter_bar")
        self.pfilter_bar.setMinimumSize(QSize(160, 0))
        self.pfilter_bar.setMaximumSize(QSize(160, 16777215))
        self.pfilter_bar.setFont(font)

        self.horizontalLayout_6.addWidget(self.pfilter_bar)


        self.gridLayout_14.addWidget(self.frame_8, 0, 0, 1, 1)

        self.psearchby_bar = QComboBox(self.psearch_header)
        self.psearchby_bar.addItem("")
        self.psearchby_bar.addItem("")
        self.psearchby_bar.addItem("")
        self.psearchby_bar.setObjectName(u"psearchby_bar")
        self.psearchby_bar.setMinimumSize(QSize(160, 0))
        self.psearchby_bar.setMaximumSize(QSize(160, 16777215))
        self.psearchby_bar.setFont(font)

        self.gridLayout_14.addWidget(self.psearchby_bar, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(98, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)

        self.psearch_bar = QLineEdit(self.psearch_header)
        self.psearch_bar.setObjectName(u"psearch_bar")
        self.psearch_bar.setMinimumSize(QSize(159, 0))
        self.psearch_bar.setMaximumSize(QSize(311, 16777215))
        self.psearch_bar.setFont(font)

        self.gridLayout_14.addWidget(self.psearch_bar, 0, 3, 1, 1)

        self.psearch_btn = QPushButton(self.psearch_header)
        self.psearch_btn.setObjectName(u"psearch_btn")
        self.psearch_btn.setIcon(icon6)

        self.gridLayout_14.addWidget(self.psearch_btn, 0, 4, 1, 1)


        self.gridLayout_22.addWidget(self.psearch_header, 1, 0, 1, 1)

        self.ptable_header = QFrame(self.programs_page)
        self.ptable_header.setObjectName(u"ptable_header")
        self.ptable_header.setFrameShape(QFrame.StyledPanel)
        self.ptable_header.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.ptable_header)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.prog_table = QTableWidget(self.ptable_header)
        if (self.prog_table.columnCount() < 4):
            self.prog_table.setColumnCount(4)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font8);
        __qtablewidgetitem10.setBackground(QColor(237, 70, 110));
        self.prog_table.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font8);
        __qtablewidgetitem11.setBackground(QColor(237, 70, 110));
        self.prog_table.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFont(font8);
        __qtablewidgetitem12.setBackground(QColor(237, 70, 110));
        self.prog_table.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font8);
        __qtablewidgetitem13.setBackground(QColor(237, 70, 110));
        self.prog_table.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        self.prog_table.setObjectName(u"prog_table")
        self.prog_table.setAlternatingRowColors(True)
        self.prog_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.prog_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.gridLayout_20.addWidget(self.prog_table, 0, 0, 1, 1)


        self.gridLayout_22.addWidget(self.ptable_header, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.programs_page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)


        self.horizontalLayout_4.addWidget(self.fill)


        self.gridLayout_3.addWidget(self.main_body, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.SSIS.setText(QCoreApplication.translate("MainWindow", u"Simple Student Information System", None))
        self.students.setText(QCoreApplication.translate("MainWindow", u"Students", None))
        self.colleges.setText(QCoreApplication.translate("MainWindow", u"Colleges", None))
        self.programs.setText(QCoreApplication.translate("MainWindow", u"Programs", None))
        self.body.setPlainText(QCoreApplication.translate("MainWindow", u"Welcome to the Students Information page!", None))
        self.icon.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"Students Information", None))
        self.addstdnt_btn.setText(QCoreApplication.translate("MainWindow", u" Add New Student", None))
        self.label_2.setText("")
        self.filter_bar.setItemText(0, QCoreApplication.translate("MainWindow", u"First Name", None))
        self.filter_bar.setItemText(1, QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.filter_bar.setItemText(2, QCoreApplication.translate("MainWindow", u"Year Level", None))
        self.filter_bar.setItemText(3, QCoreApplication.translate("MainWindow", u"ID Number", None))
        self.filter_bar.setItemText(4, QCoreApplication.translate("MainWindow", u"Gender", None))
        self.filter_bar.setItemText(5, QCoreApplication.translate("MainWindow", u"Program", None))

        self.searchby_bar.setItemText(0, QCoreApplication.translate("MainWindow", u"First Name", None))
        self.searchby_bar.setItemText(1, QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.searchby_bar.setItemText(2, QCoreApplication.translate("MainWindow", u"Year Level", None))
        self.searchby_bar.setItemText(3, QCoreApplication.translate("MainWindow", u"ID Number", None))
        self.searchby_bar.setItemText(4, QCoreApplication.translate("MainWindow", u"Gender", None))
        self.searchby_bar.setItemText(5, QCoreApplication.translate("MainWindow", u"Program", None))

        self.search_bar.setText("")
        self.search_bar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.search_btn.setText("")
        ___qtablewidgetitem = self.student_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem1 = self.student_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem2 = self.student_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ID Number", None));
        ___qtablewidgetitem3 = self.student_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Year Level", None));
        ___qtablewidgetitem4 = self.student_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem5 = self.student_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Program", None));
        ___qtablewidgetitem6 = self.student_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        ___qtablewidgetitem7 = self.college_table.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem8 = self.college_table.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Code", None));
        ___qtablewidgetitem9 = self.college_table.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        self.label_4.setText("")
        self.cfilter_bar.setItemText(0, QCoreApplication.translate("MainWindow", u"Name", None))
        self.cfilter_bar.setItemText(1, QCoreApplication.translate("MainWindow", u"Code", None))

        self.csearchby_bar.setItemText(0, QCoreApplication.translate("MainWindow", u"Name", None))
        self.csearchby_bar.setItemText(1, QCoreApplication.translate("MainWindow", u"Code", None))

        self.csearch_bar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.csearch_btn.setText("")
        self.cicon.setText("")
        self.ctitle.setText(QCoreApplication.translate("MainWindow", u"Colleges Information", None))
        self.cbody.setPlainText(QCoreApplication.translate("MainWindow", u"Welcome to the Colleges section!", None))
        self.college_btn.setText(QCoreApplication.translate("MainWindow", u"    Add College", None))
        self.program_btn.setText(QCoreApplication.translate("MainWindow", u"  Add Program", None))
        self.picon.setText("")
        self.ptitle.setText(QCoreApplication.translate("MainWindow", u"Programs Information", None))
        self.pbody.setPlainText(QCoreApplication.translate("MainWindow", u"Welcome to the Programs section!", None))
        self.label_3.setText("")
        self.pfilter_bar.setItemText(0, QCoreApplication.translate("MainWindow", u"College", None))
        self.pfilter_bar.setItemText(1, QCoreApplication.translate("MainWindow", u"Program", None))
        self.pfilter_bar.setItemText(2, QCoreApplication.translate("MainWindow", u"Code", None))

        self.psearchby_bar.setItemText(0, QCoreApplication.translate("MainWindow", u"College", None))
        self.psearchby_bar.setItemText(1, QCoreApplication.translate("MainWindow", u"Program", None))
        self.psearchby_bar.setItemText(2, QCoreApplication.translate("MainWindow", u"Code", None))

        self.psearch_bar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.psearch_btn.setText("")
        ___qtablewidgetitem10 = self.prog_table.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"College", None));
        ___qtablewidgetitem11 = self.prog_table.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Program", None));
        ___qtablewidgetitem12 = self.prog_table.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Code", None));
        ___qtablewidgetitem13 = self.prog_table.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Action", None));
    # retranslateUi

######################################################################################################################
    def setComboBoxPlaceholders(self):
        self.insertPlaceholder(self.filter_bar, "Sort by")
        self.insertPlaceholder(self.searchby_bar, "Search by")
        self.insertPlaceholder(self.cfilter_bar, "Sort by")
        self.insertPlaceholder(self.csearchby_bar, "Search by")
        self.insertPlaceholder(self.pfilter_bar, "Sort by")
        self.insertPlaceholder(self.psearchby_bar, "Search by ")

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
    def college_table_format(self):
        for row in range(self.college_table.rowCount()):
            for col in range(self.college_table.columnCount()):
                item = self.college_table.item(row, col)
                if item:  
                    item.setTextAlignment(Qt.AlignCenter)  # Align text to center

    def program_table_format(self):
        for row in range(self.prog_table.rowCount()):
            for col in range(self.prog_table.columnCount()):
                item = self.prog_table.item(row, col)
                if item:  
                    item.setTextAlignment(Qt.AlignCenter)  # Align text to center

    def student_table_format(self):
        for row in range(self.student_table.rowCount()):
            for col in range(self.student_table.columnCount()):
                item = self.student_table.item(row, col)
                if item:  
                    item.setTextAlignment(Qt.AlignCenter)  # Align text to center