import os
os.makedirs("outputs",exist_ok = True)
from src.log_parser import parse_logs,extract_errors,error_frequency
file_path = 'data/logs.txt'
info,warning,error = parse_logs(file_path)
print("===== Log Analysis Report ==== ")
print()
print("INFO Logs:",info)
print("WARNING Logs:",warning)
print("ERROR Logs:",error)
total_logs = info + warning + error
print("\nTotal Logs Processed:",total_logs)
print("\n----------------------------------")
errors = extract_errors(file_path)
print("\nDetected Errors:")
for err in errors:
    print("-",err)
print("\n ==== Error Frequency Report ====")
freq = error_frequency(file_path)
for err,count in freq.items():
    print(err,":",count)
print("Log Analysis Completed Successfully")
report_path = "outputs/log_report.txt"

with open(report_path, "w") as file:

    file.write("===== Log Analysis Report =====\n\n")

    file.write(f"INFO Logs: {info}\n")
    file.write(f"WARNING Logs: {warning}\n")
    file.write(f"ERROR Logs: {error}\n\n")

    total_logs = info + warning + error

    file.write(f"Total Logs Processed: {total_logs}\n\n")

    file.write("Detected Errors:\n")

    for err in errors:
        file.write(f"- {err}\n")

    file.write("\n==== Error Frequency Report ====\n")

    for err, count in freq.items():
        file.write(f"{err} : {count}\n")
    print("\nReport saved to outputs/log_report.txt")

