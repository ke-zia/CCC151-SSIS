from PySide2.QtWidgets import QTableWidgetItem, QPushButton, QWidget, QHBoxLayout, QMessageBox, QMainWindow, QHeaderView
from PySide2.QtGui import QIcon, QFont
from PySide2.QtCore import Qt
from data_handler import load_data, save_data
from ui_addprogram import Ui_AddProgram_Window

class ProgramOperations:
    def __init__(self, ui, student_ops):
        self.ui = ui
        self.student_ops = student_ops

    def open_add_program(self):
        df = load_data("colleges")
        
        if df.empty or "College Name" not in df.columns or df["College Name"].empty:
            QMessageBox.warning(self, "No Colleges Available", "Please add a college first before adding a program.")
            return  
        
        self.add_program_window = QMainWindow()
        self.add_program_ui = Ui_AddProgram_Window()
        self.add_program_ui.setupUi(self.add_program_window, self)
        self.add_program_ui.setComboBoxPlaceholders()
        self.add_program_window.show()
        
    def add_program_row(self, college_code, program_name, program_code):
        search_term = self.ui.psearch_bar.text().strip().lower()
        search_by = self.ui.psearchby_bar.currentText()

        if search_term:
            if search_by == "College" and search_term not in college_code.lower():
                return
            elif search_by == "Program" and search_term not in program_name.lower():
                return
            elif search_by == "Code" and search_term not in program_code.lower():
                return

        self.ui.prog_table.setSortingEnabled(False)
        row_position = self.ui.prog_table.rowCount()
        self.ui.prog_table.insertRow(row_position)

        font = QFont("Montserrat SemiBold")
        college_item = QTableWidgetItem(college_code)
        college_item.setFont(font)
        pname_item = QTableWidgetItem(program_name)
        pname_item.setFont(font)
        pcode_item = QTableWidgetItem(program_code)
        pcode_item.setFont(font)

        self.ui.prog_table.setItem(row_position, 0, college_item)
        self.ui.prog_table.setItem(row_position, 1, pname_item)
        self.ui.prog_table.setItem(row_position, 2, pcode_item)

        update_btn = QPushButton()
        update_btn.setIcon(QIcon("icons/edit.svg"))  
        update_btn.setStyleSheet("border: none; background: transparent;")  
        update_btn.clicked.connect(lambda: self.update_program(self.get_ptable_row(update_btn)))

        delete_btn = QPushButton()
        delete_btn.setIcon(QIcon("icons/trash-2.svg"))  
        delete_btn.setStyleSheet("border: none; background: transparent;") 
        delete_btn.clicked.connect(lambda: self.delete_program(delete_btn))

        action_widget = QWidget()
        action_layout = QHBoxLayout(action_widget)
        action_layout.addWidget(update_btn)
        action_layout.addWidget(delete_btn)
        action_layout.setContentsMargins(0, 0, 0, 0)  
        action_widget.setLayout(action_layout)

        self.ui.prog_table.setCellWidget(row_position, 3, action_widget)
        self.ui.program_table_format()
        self.ui.prog_table.setSortingEnabled(True)

    def update_program(self, row):

        if row < 0 or row >= self.ui.prog_table.rowCount():
            return

        old_college = self.ui.prog_table.item(row, 0).text()
        old_pname = self.ui.prog_table.item(row, 1).text()
        old_pcode = self.ui.prog_table.item(row, 2).text()

        self.add_program_window = QMainWindow()
        self.add_program_ui = Ui_AddProgram_Window()
        self.add_program_ui.setupUi(self.add_program_window, self)

        index = self.add_program_ui.pcollege_info.findData(old_college)
        if index >= 0:
            self.add_program_ui.pcollege_info.setCurrentIndex(index)
        self.add_program_ui.pname_info.setText(old_pname)
        self.add_program_ui.pcode_info.setText(old_pcode)

        self.add_program_ui.padd_btn.clicked.disconnect()
        self.add_program_ui.padd_btn.clicked.connect(lambda: self.save_program_update(row, old_college, old_pname, old_pcode))

        self.add_program_window.show()

    def save_program_update(self, row, old_college, old_name, old_code):
        new_college = self.add_program_ui.pcollege_info.currentText().strip()
        new_college_code = self.add_program_ui.pcollege_info.currentData() 
        new_pname = self.add_program_ui.pname_info.text().strip()
        new_pcode = self.add_program_ui.pcode_info.text().strip()

        if new_college == "Select College" or not new_pname or not new_pcode:
            QMessageBox.warning(None, "Incomplete Data", "Please fill out all fields before saving.")
            return

        df_programs = load_data("programs")

        if(df_programs["Program Name"].str.strip().str.lower() == new_pname.lower()).any() and new_pname.lower() != old_name.lower():
            QMessageBox.warning(None, "Duplicate Program", f"A program with the name '{new_pname}' already exists for this college.")
            return
        
        if(df_programs["Program Code"].str.strip().str.lower() == new_pcode.lower()).any() and new_pcode.lower() != old_code.lower():
            QMessageBox.warning(None, "Duplicate Program Code", f"A program with the code '{new_pcode}' already exists for this college.")
            return

        college_item = QTableWidgetItem(new_college_code)
        pname_item = QTableWidgetItem(new_pname)
        pcode_item = QTableWidgetItem(new_pcode)
        
        montserrat_font = QFont("Montserrat SemiBold")
        college_item.setFont(montserrat_font)
        pname_item.setFont(montserrat_font)
        pcode_item.setFont(montserrat_font)

        self.ui.prog_table.setItem(row, 0, college_item)
        self.ui.prog_table.setItem(row, 1, pname_item)
        self.ui.prog_table.setItem(row, 2, pcode_item)

        df_programs.loc[
            (df_programs["College"] == old_college) &
            (df_programs["Program Name"] == old_name) &
            (df_programs["Program Code"] == old_code),
            ["College", "Program Name", "Program Code"]
        ] = [new_college_code, new_pname, new_pcode]
        save_data(df_programs, "programs")

        df_students = load_data("students")
        df_students.loc[(df_students["Program"] == old_code), ["Program"]] = [new_pcode]
        save_data(df_students, "students")

        self.student_ops.load_students() 

        self.ui.program_table_format()
        self.load_programs()
        self.add_program_window.close()

    def delete_program(self, button):
        if not button:
            return

        index = self.ui.prog_table.indexAt(button.parentWidget().pos())
        row = index.row()

        if row == -1:
            return

        college_name = self.ui.prog_table.item(row, 0).text().strip()
        program_name = self.ui.prog_table.item(row, 1).text().strip()
        program_code = self.ui.prog_table.item(row, 2).text().strip()

        reply = QMessageBox.question(
            None,
            "Confirm Deletion",
            f"Are you sure you want to delete the program '{program_name}'?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.No:
            return

        self.ui.prog_table.setSortingEnabled(False)

        self.ui.prog_table.removeRow(row)

        df_programs = load_data("programs")
        df_students = load_data("students")

        df_programs = df_programs[~((df_programs["College"] == college_name) &
                                    (df_programs["Program Name"] == program_name) &
                                    (df_programs["Program Code"] == program_code))]
        save_data(df_programs, "programs")

        df_students.loc[df_students["Program"] == program_code, "Program"] = "Not Applicable"
        save_data(df_students, "students")

        self.student_ops.load_students()

        self.load_programs()

        self.ui.prog_table.setSortingEnabled(True)
        self.ui.prog_table.clearSelection()
        self.ui.prog_table.setCurrentCell(-1, -1)
        self.ui.prog_table.clearFocus()

    def load_programs(self):
        df = load_data("programs")

        search_term = self.ui.psearch_bar.text().strip().lower()

        self.ui.prog_table.setRowCount(0)

        header = self.ui.prog_table.horizontalHeader()
        self.ui.prog_table.setColumnWidth(0, 250)  # College
        header.setSectionResizeMode(1, QHeaderView.Stretch)  # Program Name
        self.ui.prog_table.setColumnWidth(2, 250)  # Program Code
        self.ui.prog_table.setColumnWidth(3, 200)  # Action

        for _, row in df.iterrows():
            college_code = row["College"]
            program_name = row["Program Name"]
            program_code = row["Program Code"]

            self.add_program_row(college_code, program_name, program_code)

        self.ui.prog_table.viewport().update()

        if search_term:
            self.search_programs()

    def setup_program_filter(self):
        self.ui.pfilter_bar.clear()
        self.ui.pfilter_bar.addItem("Sort by")
        self.ui.pfilter_bar.addItem("College")
        self.ui.pfilter_bar.addItem("Program")
        self.ui.pfilter_bar.addItem("Code")
        self.ui.pfilter_bar.setCurrentIndex(0)

        self.ui.pfilter_bar.currentIndexChanged.connect(self.sort_program_table)
        self.ui.psearchby_bar.currentIndexChanged.connect(self.search_programs)  
        self.ui.psearch_bar.textChanged.connect(self.search_programs)

        self.ui.prog_table.setSortingEnabled(True)

    def sort_program_table(self):
        """Sorts the program table based on the selected filter."""
        selected_sort = self.ui.pfilter_bar.currentText()

        if selected_sort == "Sort by":
            return

        col_index = 0 if selected_sort == "College" else 1 if selected_sort == "Program" else 2
        self.ui.prog_table.setSortingEnabled(True)
        self.ui.prog_table.sortItems(col_index, Qt.AscendingOrder)

    def get_ptable_row(self, button):
        """Finds the correct row index for a button after sorting."""
        index = self.ui.prog_table.indexAt(button.parentWidget().pos())
        return index.row()

    def search_programs(self):
        search_term = self.ui.psearch_bar.text().strip().lower()
        search_by = self.ui.psearchby_bar.currentText()

        df = load_data("programs")  

        if df.empty:
            QMessageBox.warning(None, "No Data", "No programs found.")
            return

        df = df.astype(str)

        if search_by == "College":
            filtered_df = df[df["College"].fillna("").str.lower().str.contains(search_term, na=False)]
        elif search_by == "Program":
            filtered_df = df[df["Program Name"].fillna("").str.lower().str.contains(search_term, na=False)]
        elif search_by == "Code":
            filtered_df = df[df["Program Code"].fillna("").str.lower().str.contains(search_term, na=False)]
        else:
            filtered_df = df[df.apply(lambda row: search_term in row.astype(str).str.lower().str.cat(sep=" "), axis=1)]

        self.ui.prog_table.setRowCount(0)
        
        for _, row in filtered_df.iterrows():
            self.add_program_row(row["College"], row["Program Name"], row["Program Code"])

        self.ui.prog_table.viewport().update()