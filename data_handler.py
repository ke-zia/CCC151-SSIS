import pandas as pd
import os

# Define CSV filenames
COLLEGE_FILE = "colleges.csv"
PROGRAM_FILE = "programs.csv"
STUDENT_FILE = "students.csv"

# Ensure CSV files exist
def initialize_files():
    file_headers = {
        COLLEGE_FILE: ["College Name", "College Code"],
        PROGRAM_FILE: ["College", "Program Name", "Program Code"],
        STUDENT_FILE: ["First Name", "Last Name", "ID Number", "Year Level", "Gender", "Program"]
    }
    
    for file, headers in file_headers.items():
        if not os.path.exists(file):
            pd.DataFrame(columns=headers).to_csv(file, index=False)

# Load data from CSV files
def load_data(file_type):
    file_map = {
        "colleges": COLLEGE_FILE,
        "programs": PROGRAM_FILE,
        "students": STUDENT_FILE,
    }
    file_path = file_map.get(file_type)

    file_headers = {
        COLLEGE_FILE: ["College Name", "College Code"],
        PROGRAM_FILE: ["College", "Program Name", "Program Code"],
        STUDENT_FILE: ["First Name", "Last Name", "ID Number", "Year Level", "Gender", "Program"]
    }
    
    if file_path and os.path.exists(file_path):
        try:
            df = pd.read_csv(file_path)
            # Ensure the DataFrame has the correct columns
            if df.empty:
                # Return an empty DataFrame with the correct columns
                return pd.DataFrame(columns=file_headers[file_path])
            return df
        except pd.errors.EmptyDataError:
            # Return an empty DataFrame with the correct columns
            return pd.DataFrame(columns=file_headers[file_path])
    else:
        # Return an empty DataFrame with the correct columns
        return pd.DataFrame(columns=file_headers[file_map[file_type]])

# Save data to CSV files
def save_data(df, file_type):
    file_map = {
        "colleges": COLLEGE_FILE,
        "programs": PROGRAM_FILE,
        "students": STUDENT_FILE,
    }
    file_path = file_map.get(file_type)
    
    if file_path:
        df.to_csv(file_path, index=False)