## Advanced Python Log Analyzer

## Project Overview

The Advanced Python Log Analyzer is a Python-based tool that processes system log files and extracts meaningful insights.

It analyzes logs to identify log levels, detect errors, calculate error frequencies, and generate an analysis report automatically.

This project demonstrates practical Python concepts such as file handling, modular programming, data analysis, and report generation.

---

## Project Structure

advance_python_project
│
├── data
│   └── logs.txt              # Sample log file for analysis
│
├── outputs
│   └── log_report.txt        # Automatically generated analysis report
│
├── src
│   └── log_parser.py         # Log parsing and analysis functions
│
├── main.py                   # Main program to run the log analyzer
├── README.md                 # Project documentation
└── requirements.txt          # Project dependencies

---

## Features Implemented

1. Log Level Analysis

The analyzer reads the log file and counts occurrences of different log levels:

- INFO
- WARNING
- ERROR

Example output:

INFO Logs: 3
WARNING Logs: 3
ERROR Logs: 3

---

2. Total Log Count

The program calculates the total number of logs processed.

Example:

Total Logs Processed: 9

---

3. Error Detection

The tool extracts all log entries marked as ERROR.

Example:

## Detected Errors:
- Database connection failed
- Server timeout
- Failed authentication

This helps identify issues occurring in the system.

---

4. Error Frequency Analysis

The analyzer counts how many times each error occurs.

Example:

==== Error Frequency Report ====

Database connection failed : 1
Server timeout : 1
Failed authentication : 1

This helps determine the most common system failures.

---

5. Automatic Report Generation

The program automatically generates a report file after analysis.

Report location:

outputs/log_report.txt

The report contains:

- Log statistics
- Total logs processed
- Detected errors
- Error frequency analysis

This makes the tool useful for saving and reviewing log analysis results.

---

## How to Run the Project

Step 1: Navigate to the project folder

cd advance_python_project

Step 2: Run the log analyzer

python main.py

---

## Example Output

===== Log Analysis Report =====

INFO Logs: 3
WARNING Logs: 3
ERROR Logs: 3

Total Logs Processed: 9

Detected Errors:
- Database connection failed
- Server timeout
- Failed authentication

==== Error Frequency Report ====

Database connection failed : 1
Server timeout : 1
Failed authentication : 1

Log Analysis Completed Successfully
Report saved to outputs/log_report.txt

---

## Technologies Used

- Python 3
- File Handling
- Dictionaries
- Modular Programming

---

## Future Improvements

## Planned enhancements include:

- JSON report generation
- CSV report generation
- Log filtering by level
- Visualization of log statistics
- Real-time log monitoring

---

## Author

Tejaswini Chimekala