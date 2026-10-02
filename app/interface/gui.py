import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
from app.processing.processor import process_file


selected_file = None
output_directory = None


def select_file():
    global selected_file

    file_path = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=[
            ("Excel files", "*.xlsx"),
            ("All files", "*.*")
        ]
    )

    if file_path:
        selected_file = file_path

        file_label.config(
            text=os.path.basename(file_path)
        )

        status_label.config(
            text="File selected. Ready to process."
        )


def process_selected_file():
    global output_directory

    if not selected_file:
        messagebox.showwarning(
            "No file selected",
            "Please select an Excel file first."
        )
        return

    try:
        # Ask the user where to save the results
        output_directory = filedialog.askdirectory(
            title="Choose where to save the results"
        )

        if not output_directory:
            return

        result = process_file(
            selected_file,
            output_directory
        )

        summary = result["cleaning_summary"]

        status_label.config(
            text="Processing completed successfully!"
        )

        result_label.config(
            text=(
                f"Records processed: {result['total_employees']}\n"
                f"Duplicates removed: "
                f"{summary['duplicates_removed']}\n"
                f"Missing values: "
                f"{summary['missing_values']}"
            )
        )

        messagebox.showinfo(
            "Dataflow",
            "Excel file processed successfully!"

        )

    except Exception as error:
        status_label.config(
            text="An error occurred."
        )

        messagebox.showerror(
            "Error",
            f"Could not process the file.\n\n{error}"
        )

def open_results_folder():
    if not output_directory:
        messagebox.showwarning(
            "No results",
            "Please process an Excel file first."
        )
        return

    os.startfile(output_directory)


def open_cleaned_file():
    if not output_directory:
        messagebox.showwarning(
            "No results",
            "Please process an Excel file first."
        )
        return

    cleaned_file = os.path.join(
        output_directory,
        "cleaned_data.xlsx"
    )

    if os.path.exists(cleaned_file):
        os.startfile(cleaned_file)
    else:
        messagebox.showwarning(
            "File not found",
            "The cleaned Excel file has not been generated yet."
        )

# Main window
window = tk.Tk()

window.title("Dataflow")
window.geometry("700x500")

# Title
title_label = tk.Label(
    window,
    text="DATAFLOW",
    font=("Arial", 24, "bold")
)

title_label.pack(pady=30)

# Description
description_label = tk.Label(
    window,
    text="Excel Data Cleaning & Analysis",
    font=("Arial", 14)
)

description_label.pack(pady=10)

# Select button
select_button = tk.Button(
    window,
    text="Choose Excel File",
    command=select_file,
    font=("Arial", 12),
    width=20
)

select_button.pack(pady=20)

# Selected file
file_label = tk.Label(
    window,
    text="No file selected",
    font=("Arial", 10)
)

file_label.pack(pady=5)

# Process button
process_button = tk.Button(
    window,
    text="Process File",
    command=process_selected_file,
    font=("Arial", 12, "bold"),
    width=20
)

process_button.pack(pady=20)

# Status
status_label = tk.Label(
    window,
    text="Select an Excel file to begin.",
    font=("Arial", 11)
)

status_label.pack(pady=10)

# Results
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 11),
    justify="left"
)

result_label.pack(pady=10)

# Open results folder button
open_folder_button = tk.Button(
    window,
    text="Open Results Folder",
    command=open_results_folder,
    font=("Arial", 11),
    width=20
)

open_folder_button.pack(pady=5)

# Open cleaned Excel button
open_excel_button = tk.Button(
    window,
    text="Open Cleaned Excel",
    command=open_cleaned_file,
    font=("Arial", 11),
    width=20
)

open_excel_button.pack(pady=5)

# Start application
window.mainloop()