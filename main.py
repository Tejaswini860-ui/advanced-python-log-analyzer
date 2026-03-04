from src.log_parser import parse_logs
file_path = 'data/logs.txt'
info,warning,error = parse_logs(file_path)
print("===== Log Analysis Report ==== ")
print()
print("INFO Logs:",info)
print("WARNING Logs:",warning)
print("ERROR Logs:",error)
total_logs = info + warning + error
print()
print("Total Logs Processed:",total_logs)