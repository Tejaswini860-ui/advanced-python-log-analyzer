def parse_logs(file_path):
    info = 0
    warning = 0
    error = 0
    with open (file_path,'r') as file:
        for line in file:
            if 'INFO' in line:
                info += 1
            elif 'WARNING' in line:
                warning += 1
            elif 'ERROR' in line:
                error += 1
            elif 'DEBUG' in line:
                debug += 1
    return info,warning,error,debug

def extract_errors(file_path):
    errors = []
    with open (file_path,"r") as file:
        for line in file:
            if "ERROR" in line:
                error_message = line.replace("ERROR", "").strip()
                errors.append(error_message)
    return errors
def error_frequency(file_path):
    error_count = {}
    with open (file_path,'r') as file:
        for line in file:
            if "ERROR" in line:
                error_message = line.replace("ERROR","").strip()
                if error_message in error_count:
                    error_count[error_message] += 1
                else:
                    error_count[error_message ] = 1 
    return error_count
