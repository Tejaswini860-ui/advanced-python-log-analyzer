## Advanced Python Log Analyzer

## Project Overview

The Advanced Python Log Analyzer is a Python-based tool designed to analyze system log files.
It processes log data to extract useful insights such as log level statistics, detected errors, and error frequency.

This project helps demonstrate practical Python skills including file handling, string processing, data analysis, and modular programming.

---

## Project Structure

advance_python_project
│
├── data
│   └── logs.txt                # Sample log file used for analysis
│
├── src
│   └── log_parser.py           # Functions for parsing and analyzing logs
│
├── outputs                     # Directory for future generated reports
│
├── main.py                     # Main script that runs the log analyzer
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies

---

## Features Implemented

1. Log Level Analysis

The program reads the log file and counts different log levels:

- INFO
- WARNING
- ERROR

This helps in understanding the distribution of log events.

---

2. Total Log Count

The analyzer calculates the total number of logs processed in the file.

Example output:

Total Logs Processed: 9

---

3. Error Detection

The program extracts all log entries marked as ERROR and displays them clearly.

Example:

Detected Errors:

- Database connection failed
- Server timeout
- Failed authentication

---

4. Error Frequency Analysis

The analyzer counts how many times each error appears in the log file.

## Example:

Error Frequency Report:

Database connection failed : 1
Server timeout : 1
Failed authentication : 1

This helps identify common system issues quickly.

---

How to Run the Project

Step 1: Navigate to the Project Folder

cd advance_python_project

Step 2: Run the Analyzer

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

---

## Technologies Used

- Python 3
- File Handling
- Dictionary Data Structures
- Modular Programming

---

## Future Improvements

Planned enhancements include:

- Export analysis results to report files
- Generate structured reports in the "outputs" folder
- Add log filtering capabilities
- Improve error pattern detection
- Build visualization dashboards for log analysis

---

## Author

Tejaswini Chimekala