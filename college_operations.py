from PySide2.QtWidgets import QTableWidgetItem, QPushButton, QWidget, QHBoxLayout, QMessageBox, QMainWindow, QHeaderView
from PySide2.QtGui import QIcon, QFont
from PySide2.QtCore import Qt
from data_handler import load_data, save_data
from ui_addcollege import Ui_AddCollege_Window

class CollegeOperations:
    def __init__(self, ui, program_ops):
        self.ui = ui
        self.program_ops = program_ops

    def open_add_college(self):
        self.add_college_window = QMainWindow()
        self.add_college_ui = Ui_AddCollege_Window()
        self.add_college_ui.setupUi(self.add_college_window, self)
        self.add_college_window.show()

    def add_college_row(self, name, code):
        search_term = self.ui.csearch_bar.text().strip().lower()
        search_by = self.ui.csearchby_bar.currentText()

        if search_term:
            if search_by == "Name" and search_term not in name.lower():
                return
            elif search_by == "Code" and search_term not in code.lower():
                return

        self.ui.college_table.setSortingEnabled(False)
        row_position = self.ui.college_table.rowCount()
        self.ui.college_table.insertRow(row_position)

        font = QFont("Montserrat SemiBold")
        name_item = QTableWidgetItem(name)
        name_item.setFont(font)
        code_item = QTableWidgetItem(code)
        code_item.setFont(font)

        self.ui.college_table.setItem(row_position, 0, name_item)
        self.ui.college_table.setItem(row_position, 1, code_item)

        update_btn = QPushButton()
        update_btn.setIcon(QIcon("icons/edit.svg"))
        update_btn.setStyleSheet("border: none; background: transparent;")
        update_btn.clicked.connect(lambda: self.update_college(self.get_ctable_row(update_btn)))

        delete_btn = QPushButton()
        delete_btn.setIcon(QIcon("icons/trash-2.svg"))
        delete_btn.setStyleSheet("border: none; background: transparent;")
        delete_btn.clicked.connect(lambda: self.delete_college(delete_btn))

        action_widget = QWidget()
        action_layout = QHBoxLayout(action_widget)
        action_layout.addWidget(update_btn)
        action_layout.addWidget(delete_btn)
        action_layout.setContentsMargins(0, 0, 0, 0)
        action_widget.setLayout(action_layout)

        self.ui.college_table.setCellWidget(row_position, 2, action_widget)
        self.ui.college_table_format()
        self.ui.college_table.setSortingEnabled(True)

    def update_college(self, row):

        old_name = self.ui.college_table.item(row, 0).text()
        old_code = self.ui.college_table.item(row, 1).text()

        self.add_college_window = QMainWindow()
        self.add_college_ui = Ui_AddCollege_Window()
        self.add_college_ui.setupUi(self.add_college_window, self)

        self.add_college_ui.cname_info.setText(old_name)
        self.add_college_ui.ccode_info.setText(old_code)

        self.add_college_ui.cadd_btn.clicked.disconnect()
        self.add_college_ui.cadd_btn.clicked.connect(lambda: self.save_college_update(row, old_name, old_code))

        self.add_college_window.show()

    def save_college_update(self, row, old_name, old_code):
        new_name = self.add_college_ui.cname_info.text().strip()
        new_code = self.add_college_ui.ccode_info.text().strip()

        if not new_name or not new_code:
            QMessageBox.warning(None, "Incomplete Data", "Please fill out all fields before saving.")
            return

        df_colleges = load_data("colleges")

        if (df_colleges["College Name"].str.strip().str.lower() == new_name.lower()).any() and new_name.lower() != old_name.lower():
            QMessageBox.warning(None, "Duplicate College", f"A college with the name '{new_name}' already exists.")
            return

        if (df_colleges["College Code"].str.strip().str.lower() == new_code.lower()).any() and new_code.lower() != old_code.lower():
            QMessageBox.warning(None, "Duplicate College Code", f"A college with the code '{new_code}' already exists.")
            return

        name_item = QTableWidgetItem(new_name)
        code_item = QTableWidgetItem(new_code)

        montserrat_font = QFont("Montserrat SemiBold")
        name_item.setFont(montserrat_font)
        code_item.setFont(montserrat_font)

        self.ui.college_table.setItem(row, 0, name_item)
        self.ui.college_table.setItem(row, 1, code_item)

        df_colleges.loc[(df_colleges["College Name"] == old_name) & 
                        (df_colleges["College Code"] == old_code), 
                        ["College Name", "College Code"]] = [new_name, new_code]
        save_data(df_colleges, "colleges")

        df_programs = load_data("programs")
        df_programs.loc[df_programs["College"] == old_code, "College"] = new_code
        save_data(df_programs, "programs")

        self.program_ops.load_programs() 
        
        self.ui.college_table_format()
        self.load_colleges()
        self.add_college_window.close()

    def delete_college(self, button):
        if not button:
            return

        index = self.ui.college_table.indexAt(button.parent().pos())
        row = index.row()

        if row == -1:
            return

        college_name = self.ui.college_table.item(row, 0).text().strip()
        college_code = self.ui.college_table.item(row, 1).text().strip()

        reply = QMessageBox.question(
            None,
            "Confirm Deletion",
            f"Are you sure you want to delete {college_name}?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.No:
            return

        self.ui.college_table.setSortingEnabled(False)
        self.ui.college_table.removeRow(row)

        df_colleges = load_data("colleges")
        df_programs = load_data("programs")

        df_colleges = df_colleges[~((df_colleges["College Name"] == college_name) &
                                    (df_colleges["College Code"] == college_code))]
        save_data(df_colleges, "colleges")

        df_programs.loc[df_programs["College"] == college_code, "College"] = "Not Applicable"
        save_data(df_programs, "programs")

        self.program_ops.load_programs()

        search_term = self.ui.csearch_bar.text().strip().lower()
        search_by = self.ui.csearchby_bar.currentText()

        self.load_colleges()
        self.ui.csearch_bar.setText(search_term)
        self.ui.csearchby_bar.setCurrentText(search_by)
        self.search_colleges()

        self.ui.college_table.setSortingEnabled(True)
        self.ui.college_table.clearSelection()
        self.ui.college_table.setCurrentCell(-1, -1)
        self.ui.college_table.clearFocus()

    def load_colleges(self):
        df = load_data("colleges")

        search_term = self.ui.csearch_bar.text().strip().lower()

        self.ui.college_table.setRowCount(0)

        header = self.ui.college_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)  # College Name
        self.ui.college_table.setColumnWidth(1, 250)  # College Code
        self.ui.college_table.setColumnWidth(2, 200)  # Action

        for _, row in df.iterrows():
            name = row["College Name"]
            code = row["College Code"]

            self.add_college_row(name, code)

        self.ui.college_table.viewport().update()

        if search_term:
            self.search_colleges()

    def setup_college_filter(self):
        self.ui.cfilter_bar.clear()
        self.ui.setComboBoxPlaceholders()
        self.ui.cfilter_bar.addItem("Name")
        self.ui.cfilter_bar.addItem("Code")
        self.ui.cfilter_bar.setCurrentIndex(0)

        self.ui.cfilter_bar.currentIndexChanged.connect(self.sort_college_table)
        self.ui.csearchby_bar.currentIndexChanged.connect(self.search_colleges)
        self.ui.csearch_bar.textChanged.connect(self.search_colleges)
        self.ui.college_table.setSortingEnabled(True)

    def sort_college_table(self):        
        selected_sort = self.ui.cfilter_bar.currentText()

        if selected_sort == "Sort by":
            return

        col_index = 0 if selected_sort == "Name" else 1
        self.ui.college_table.sortItems(col_index, Qt.AscendingOrder)

    def get_ctable_row(self, button):
        """Finds the correct row index for a button after sorting."""
        index = self.ui.college_table.indexAt(button.parentWidget().pos())
        return index.row()

    def search_colleges(self):
        search_term = self.ui.csearch_bar.text().strip().lower()  
        search_by = self.ui.csearchby_bar.currentText()

        df = load_data("colleges")  

        if df.empty:
            QMessageBox.warning(None, "No Data", "No colleges found.")
            return

        if search_by == "Name":
            filtered_df = df[df["College Name"].fillna("").str.lower().str.contains(search_term, na=False)]
        elif search_by == "Code":
            filtered_df = df[df["College Code"].fillna("").str.lower().str.contains(search_term, na=False)]
        else:
            filtered_df = df[df.apply(lambda row: search_term in row.astype(str).str.lower().str.cat(sep=" "), axis=1)]

        self.ui.college_table.setRowCount(0)

        for _, row in filtered_df.iterrows():
            self.add_college_row(row["College Name"], row["College Code"])

        self.ui.college_table.viewport().update()