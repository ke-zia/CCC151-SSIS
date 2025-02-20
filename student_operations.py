from PySide2.QtWidgets import QTableWidgetItem, QPushButton, QWidget, QHBoxLayout, QMessageBox, QMainWindow, QHeaderView
from PySide2.QtGui import QIcon, QFont
from PySide2.QtCore import Qt
import re
from data_handler import load_data, save_data
from ui_addstdnt import Ui_AddStdnt_Window

class StudentOperations:
    def __init__(self, ui):
        self.ui = ui

    def open_add_student(self):
        self.add_student_window = QMainWindow()
        self.add_student_ui = Ui_AddStdnt_Window()
        self.add_student_ui.setupUi(self.add_student_window, self)
        self.add_student_ui.setComboBoxPlaceholders()
        self.add_student_window.show()
        
    def add_student_row(self, first_name, last_name, id_number, year_level, gender, program_code):
        search_term = self.ui.search_bar.text().strip().lower()
        search_by = self.ui.searchby_bar.currentText()

        if search_term:
            if search_by == "First Name" and search_term not in first_name.lower():
                return
            elif search_by == "Last Name" and search_term not in last_name.lower():
                return
            elif search_by == "ID Number" and search_term not in id_number.lower():
                return
            elif search_by == "Year Level" and search_term not in str(year_level):
                return
            elif search_by == "Gender" and search_term not in gender.lower():
                return
            elif search_by == "Program" and search_term not in program_code.lower():
                return

        self.ui.student_table.setSortingEnabled(False) 

        try:
            year_level = int(year_level)
            if year_level < 1 or year_level > 5:
                raise ValueError("Invalid Year Level")
            
            year_level = str(year_level)

            if not re.match(r"^\d{4}-\d{4}$", id_number):
                raise ValueError("Invalid ID Number format")

            row_position = self.ui.student_table.rowCount()
            self.ui.student_table.insertRow(row_position)

            font = QFont("Montserrat SemiBold")
            firstname_item = QTableWidgetItem(first_name)
            firstname_item.setFont(font)
            lastname_item = QTableWidgetItem(last_name)
            lastname_item.setFont(font)
            idnumber_item = QTableWidgetItem(id_number)
            idnumber_item.setFont(font)
            yearlevel_item = QTableWidgetItem(year_level)
            yearlevel_item.setFont(font)
            yearlevel_item.setText(str(year_level))
            gender_item = QTableWidgetItem(gender)
            gender_item.setFont(font)
            program_item = QTableWidgetItem(program_code)
            program_item.setFont(font)

            self.ui.student_table.setItem(row_position, 0, firstname_item)
            self.ui.student_table.setItem(row_position, 1, lastname_item)
            self.ui.student_table.setItem(row_position, 2, idnumber_item)
            self.ui.student_table.setItem(row_position, 3, yearlevel_item)
            self.ui.student_table.setItem(row_position, 4, gender_item)
            self.ui.student_table.setItem(row_position, 5, program_item)

            update_btn = QPushButton()
            update_btn.setIcon(QIcon("icons/edit.svg"))
            update_btn.setStyleSheet("border: none; background: transparent;")
            update_btn.clicked.connect(lambda: self.update_student(self.get_stable_row(update_btn)))

            delete_btn = QPushButton()
            delete_btn.setIcon(QIcon("icons/trash-2.svg"))
            delete_btn.setStyleSheet("border: none; background: transparent;")
            delete_btn.clicked.connect(lambda: self.delete_student(delete_btn))

            action_widget = QWidget()
            action_layout = QHBoxLayout(action_widget)
            action_layout.addWidget(update_btn)
            action_layout.addWidget(delete_btn)
            action_layout.setContentsMargins(0, 0, 0, 0)
            action_widget.setLayout(action_layout)

            self.ui.student_table.setCellWidget(row_position, 6, action_widget)
            self.ui.student_table_format()

        except ValueError as e:
            print(f"Error adding student row: {e}")
            QMessageBox.warning(self, "Invalid Data", f"Invalid data encountered: {e}")

        self.ui.student_table.setSortingEnabled(True)

    def update_student(self, row):
        old_firstname = self.ui.student_table.item(row, 0).text()
        old_lastname = self.ui.student_table.item(row, 1).text()
        old_idnumber = self.ui.student_table.item(row, 2).text()
        old_yearlevel = self.ui.student_table.item(row, 3).text()
        old_gender = self.ui.student_table.item(row, 4).text()
        old_program = self.ui.student_table.item(row, 5).text()

        df_programs = load_data("programs")

        self.add_student_window = QMainWindow()
        self.add_student_ui = Ui_AddStdnt_Window()
        self.add_student_ui.setupUi(self.add_student_window, self)

        self.add_student_ui.firstn_info.setText(old_firstname)
        self.add_student_ui.lastn_info.setText(old_lastname)
        self.add_student_ui.idnum_info.setText(old_idnumber)
        self.add_student_ui.yearlvl_info.setCurrentText(old_yearlevel)
        self.add_student_ui.gender_info.setCurrentText(old_gender)

        if old_program.lower() == "not applicable":
            self.add_student_ui.college_info.setCurrentIndex(0)
            self.add_student_ui.program_info.setCurrentIndex(0)
        else:
            # Find the college associated with the current program
            program_row = df_programs[df_programs["Program Code"] == old_program]
            if not program_row.empty:
                college_code = program_row.iloc[0]["College"]
                program_name = program_row.iloc[0]["Program Name"]

                # Set the college in the combobox
                college_index = self.add_student_ui.college_info.findData(college_code)
                if college_index >= 0:
                    self.add_student_ui.college_info.setCurrentIndex(college_index)

                # Set the program in the combobox
                program_index = self.add_student_ui.program_info.findText(program_name, Qt.MatchFixedString)
                if program_index >= 0:
                    self.add_student_ui.program_info.setCurrentIndex(program_index)
            else:
                self.add_student_ui.college_info.setCurrentIndex(0)
                self.add_student_ui.program_info.setCurrentIndex(0)

        self.add_student_ui.add_btn.clicked.disconnect()
        self.add_student_ui.add_btn.clicked.connect(lambda: self.save_student_update(
            row, old_firstname, old_lastname, old_idnumber, old_yearlevel, old_gender, old_program
        ))

        self.add_student_window.show()

    def save_student_update(self, row, old_firstname, old_lastname, old_idnumber, old_yearlevel, old_gender, old_program):
        new_firstname = self.add_student_ui.firstn_info.text().strip()
        new_lastname = self.add_student_ui.lastn_info.text().strip()
        new_idnumber = self.add_student_ui.idnum_info.text().strip()
        new_yearlevel = self.add_student_ui.yearlvl_info.currentText().strip()
        new_gender = self.add_student_ui.gender_info.currentText().strip()
        new_program = self.add_student_ui.program_info.currentText().strip()
        new_program_code = self.add_student_ui.program_info.currentData()

        if (not new_firstname or not new_lastname or not new_idnumber or not new_yearlevel or 
            new_gender == "Select Gender" or not new_program):
            QMessageBox.warning(None, "Incomplete Data", "Please fill out all fields before saving.")
            return

        try:
            new_yearlevel = int(new_yearlevel)
        except ValueError:
            QMessageBox.warning(None, "Invalid Year Level", "Year Level must be a valid integer.")
            return

        df_students = load_data("students")

        if ((df_students["ID Number"].str.strip() == new_idnumber).any() and 
            new_idnumber != old_idnumber):
            QMessageBox.warning(None, "Duplicate ID", "This ID number is already registered.")
            return

#############################################3
        if not re.match(r"^\d{4}-\d{4}$", new_idnumber):
            QMessageBox.warning(None, "Invalid ID", "ID format must be YYYY-NNNN.")
            return

        firstname_item = QTableWidgetItem(new_firstname)
        lastname_item = QTableWidgetItem(new_lastname)
        idnumber_item = QTableWidgetItem(new_idnumber)
        yearlevel_item = QTableWidgetItem(str(new_yearlevel))
        gender_item = QTableWidgetItem(new_gender)
        program_item = QTableWidgetItem(new_program_code)

        default_font = self.ui.student_table.font()
        firstname_item.setFont(default_font)
        lastname_item.setFont(default_font)
        idnumber_item.setFont(default_font)
        yearlevel_item.setFont(default_font)
        gender_item.setFont(default_font)
        program_item.setFont(default_font)

        self.ui.student_table.setItem(row, 0, firstname_item)
        self.ui.student_table.setItem(row, 1, lastname_item)
        self.ui.student_table.setItem(row, 2, idnumber_item)
        self.ui.student_table.setItem(row, 3, yearlevel_item)
        self.ui.student_table.setItem(row, 4, gender_item)
        self.ui.student_table.setItem(row, 5, program_item)

        df_students.loc[
            (df_students["First Name"].str.strip() == old_firstname) &
            (df_students["Last Name"].str.strip() == old_lastname) &
            (df_students["ID Number"].str.strip() == old_idnumber) &
            (df_students["Year Level"] == int(old_yearlevel)) & 
            (df_students["Gender"].str.strip() == old_gender) &
            (df_students["Program"].str.strip() == old_program),
            ["First Name", "Last Name", "ID Number", "Year Level", "Gender", "Program"]
        ] = [new_firstname, new_lastname, new_idnumber, new_yearlevel, new_gender, new_program_code]
        save_data(df_students, "students")

        self.ui.student_table_format()
        self.load_students()
        self.add_student_window.close()

    def delete_student(self, button):
        if not button:
            return

        index = self.ui.student_table.indexAt(button.parentWidget().pos())  
        row = index.row()  

        if row == -1: 
            return  
        
        first_name = self.ui.student_table.item(row, 0).text().strip()
        last_name = self.ui.student_table.item(row, 1).text().strip()
        id_number = self.ui.student_table.item(row, 2).text().strip()
        year_level = int(self.ui.student_table.item(row, 3).text().strip())  # Convert to integer
        gender = self.ui.student_table.item(row, 4).text().strip()
        program = self.ui.student_table.item(row, 5).text().strip()

        reply = QMessageBox.question(
            None,
            "Confirm Deletion",
            f"Are you sure you want to delete student record?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.No:
            return

        self.ui.student_table.setSortingEnabled(False)

        self.ui.student_table.removeRow(row)

        df_students = load_data("students")

        df_students = df_students[~((df_students["First Name"] == first_name) &
                        (df_students["Last Name"] == last_name) &
                        (df_students["ID Number"] == id_number) &
                        (df_students["Year Level"] == year_level) &
                        (df_students["Gender"] == gender) &
                        (df_students["Program"] == program))]
        save_data(df_students, "students")

        self.load_students()

        self.ui.student_table.setSortingEnabled(True)
        self.ui.student_table.clearSelection()  
        self.ui.student_table.setCurrentCell(-1, -1)
        self.ui.student_table.clearFocus()

    def load_students(self):
        df = load_data("students")

        search_term = self.ui.search_bar.text().strip().lower()

        self.ui.student_table.setRowCount(0)
            
        header = self.ui.student_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)  # First Name
        header.setSectionResizeMode(1, QHeaderView.Stretch)  # Last Name
        self.ui.student_table.setColumnWidth(2, 200)  # ID Number
        self.ui.student_table.setColumnWidth(3, 200)  # Year Level
        self.ui.student_table.setColumnWidth(4, 200)  # Gender
        self.ui.student_table.setColumnWidth(5, 200)  # Program
        self.ui.student_table.setColumnWidth(6, 200)  # Action

        for _, row in df.iterrows():
            try:
                first_name = row["First Name"]
                last_name = row["Last Name"]
                id_number = row["ID Number"]
                year_level = row["Year Level"]
                gender = row["Gender"]
                program = row["Program"]

                # Validate Year Level (ensure it's a valid integer)
                year_level = int(year_level)
                if year_level < 1 or year_level > 5:
                    raise ValueError("Invalid Year Level")

                # Validate ID Number (ensure it follows the format YYYY-NNNN)
                if not re.match(r"^\d{4}-\d{4}$", id_number):
                    raise ValueError("Invalid ID Number format")

                self.add_student_row(first_name, last_name, id_number, year_level, gender, program)

            except ValueError as e:
                print(f"Skipping invalid student data: {e}")
                continue

        self.ui.student_table.viewport().update()

        if search_term:
            self.search_students()

    def setup_student_filter(self):
        self.ui.filter_bar.clear()
        self.ui.filter_bar.addItem("Sort by")
        self.ui.filter_bar.addItem("First Name")
        self.ui.filter_bar.addItem("Last Name")
        self.ui.filter_bar.addItem("ID Number")
        self.ui.filter_bar.addItem("Year Level")
        self.ui.filter_bar.addItem("Gender")
        self.ui.filter_bar.addItem("Program")
        self.ui.filter_bar.setCurrentIndex(0)

        self.ui.filter_bar.currentIndexChanged.connect(self.sort_student_table)
        self.ui.searchby_bar.currentIndexChanged.connect(self.search_students)
        self.ui.search_bar.textChanged.connect(self.search_students)

        self.ui.student_table.setSortingEnabled(True)
    
    def sort_student_table(self):
        selected_sort = self.ui.filter_bar.currentText()

        if selected_sort == "Sort by":
            return

        col_index = {
            "First Name": 0,
            "Last Name": 1,
            "ID Number": 2,
            "Year Level": 3,
            "Gender": 4,
            "Program": 5
        }.get(selected_sort, 0)
        
        self.ui.student_table.setSortingEnabled(True)
        self.ui.student_table.sortItems(col_index, Qt.AscendingOrder)

    def get_stable_row(self, button):
        index = self.ui.student_table.indexAt(button.parentWidget().pos())
        return index.row()

    def search_students(self):
        search_term = self.ui.search_bar.text().strip().lower()
        search_by = self.ui.searchby_bar.currentText()

        df = load_data("students")

        if df.empty:
            QMessageBox.warning(None, "No Data", "No student data available.")
            return

        df = df.astype(str)

        if search_by == "First Name":
            filtered_df = df[df["First Name"].fillna("").str.lower().str.contains(search_term, na=False)]
        elif search_by == "Last Name":
            filtered_df = df[df["Last Name"].fillna("").str.lower().str.contains(search_term, na=False)]
        elif search_by == "ID Number":
            filtered_df = df[df["ID Number"].fillna("").str.lower().str.contains(search_term, na=False)]
        elif search_by == "Year Level":
            filtered_df = df[df["Year Level"].astype(str).str.contains(search_term, na=False)]
        elif search_by == "Gender":
            filtered_df = df[df["Gender"].fillna("").str.lower().str.contains(search_term, na=False)]
        elif search_by == "Program":
            filtered_df = df[df["Program"].fillna("").str.lower().str.contains(search_term, na=False)]
        else:
            filtered_df = df[df.apply(lambda row: search_term in row.astype(str).str.lower().str.cat(sep=" "), axis=1)]

        self.ui.student_table.setRowCount(0)

        for _, row in filtered_df.iterrows():
            self.add_student_row(
                row["First Name"],
                row["Last Name"],
                row["ID Number"],
                row["Year Level"],
                row["Gender"],
                row["Program"]
            )

        self.ui.student_table.viewport().update()