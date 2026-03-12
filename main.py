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

