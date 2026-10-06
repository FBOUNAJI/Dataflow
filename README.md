# 📊 Dataflow

Dataflow is a Python-based Excel data processing and analysis application.

It allows users to select an Excel file, clean and analyze the data, apply filters, generate statistics, create visualizations, and export the results into different formats.

This project was developed as a practical Python project to improve and demonstrate skills in data processing, Excel automation, data analysis, testing, and GUI development.

## 🚀 Features

- 📂 Select an Excel file through a graphical interface
- 🧹 Clean text values
- 🔎 Detect missing values
- 🔄 Detect and remove duplicate records
- 🔍 Filter data according to specific conditions
- 📊 Calculate salary statistics
- 🏢 Calculate average salary by department
- 📈 Generate data visualizations
- 📗 Export cleaned data to Excel
- 📄 Generate CSV reports
- 📝 Generate a complete analysis report
- 🖥️ Process files through a desktop GUI
- 🧪 Automated tests with Pytest

## 🛠️ Technologies

- Python
- OpenPyXL
- Matplotlib
- Tkinter
- CSV
- Pytest
- Git & GitHub

## 📁 Project Structure

```text
Dataflow/
│
├── app/
│   ├── excel/
│   │   ├── reader.py
│   │   └── writer.py
│   │
│   ├── cleaning/
│   │   ├── cleaner.py
│   │   ├── deduplicator.py
│   │   ├── duplicates.py
│   │   ├── pipeline.py
│   │   └── validator.py
│   │
│   ├── filtering/
│   │   └── filter.py
│   │
│   ├── analytics/
│   │   ├── statistics.py
│   │   ├── summary.py
│   │   └── departments.py
│   │
│   ├── visualization/
│   │   └── charts.py
│   │
│   ├── reports/
│   │   └── report.py
│   │
│   ├── processing/
│   │   └── processor.py
│   │
│   └── interface/
│       └── gui.py
│
├── data/
│   └── input/
│       └── employees.xlsx
│
├── tests/
│   ├── test_cleaning.py
│   ├── test_departments.py
│   ├── test_filter.py
│   ├── test_statistics.py
│   └── test_validator.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Dataflow
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

### 🖥️ Graphical Interface

Run the application with:

```bash
python -m app.interface.gui
```

Then:

1. Select an Excel file.
2. Choose the output directory.
3. Start the processing.
4. Open the generated results.

The application generates:

- A cleaned Excel file
- Salary statistics in CSV format
- Department salary analysis in CSV format
- A salary visualization
- A complete analysis report

### 💻 Command Line

The processing pipeline can also be executed with:

```bash
python main.py
```

## 📊 Example

Dataflow can process an Excel file containing employee information such as:

| ID | Name    | Department | Salary | Performance |
| -: | ------- | ---------- | -----: | ----------: |
|  1 | Ahmed   | IT         |   7500 |          85 |
|  2 | Sara    | HR         |   6500 |          90 |
|  3 | Youssef | IT         |   8200 |          78 |
|  4 | Fatima  | Finance    |   7000 |          92 |
|  5 | Omar    | IT         |   6000 |          65 |

The application can calculate:

- Average salary
- Minimum salary
- Maximum salary
- Total salary
- Average salary by department
- Employees with salary above a specified value

It also generates a visualization showing the average salary by department.

## 🧪 Testing

The project includes automated tests using Pytest.

Run the tests with:

```bash
pytest
```

The current test suite contains 10 tests.

## 🎯 Project Goals

The main goals of Dataflow are to practice and demonstrate:

- Python programming
- Modular application architecture
- Excel automation
- Data cleaning
- Data filtering
- Data analysis
- Data visualization
- File generation
- GUI development
- Automated testing
- Git and GitHub workflow

## 👨‍💻 Author

**Fathallah Bounaji**

Computer Science Student At University Mohammed V Rabat
