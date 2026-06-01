"""
===================================
Mini Project: Log File Reader
===================================
Features:

Read large log files efficiently
Yield one log line at a time
Filter ERROR logs
Filter WARNING logs
Count total ERROR entries

Concepts Used:

Generators
yield
File Handling
Lazy Evaluation
Generator Pipeline

Author: Mohammad Faizan
 
"""

from datetime import datetime

logs = """
INFO User login successful
INFO Payment started
ERROR Database connection failed
INFO Product viewed
ERROR Invalid password
WARNING Disk usage high
ERROR API timeout
INFO Logout success
"""

with open("server_logs.txt", "w") as file:

    for log in logs.splitlines():

        if log.strip():

            timestamp = datetime.now().strftime("%y-%m-%d %H:%M:%S")

            file.write(f"[{timestamp}] {log}\n")
            
            
def read_logs(filename):
    with open(filename, "r") as file:
        for log in file:
            yield log.strip()

def find_errors(logs):
    for log in logs:
        if "ERROR" in log:
            yield log

def find_warning(logs):
    for log in logs:
        if "WARNING" in log:
            yield log

def count_errors(logs):
    count = 0
    for log in logs:
        if "ERROR" in log:
            count +=1

    return count


if __name__ == "__main__":
    # ----all logs---
    print("==== All LOGS ====")
    all_logs = read_logs("server_logs.txt")
    for log in all_logs:
      print(log)

    # ----- Error Logs ---
    print("\n=== ERROR LOGS ===")
    logs = read_logs("server_logs.txt")
    errors = find_errors(logs)
    for error in errors:
        print(error)
        
    # ---- warning log ---
    print("\n=== WARNING LOGS ===")
    warning_log = read_logs("server_logs.txt")
    warnings = find_warning(warning_log)
    for warning in warnings:
        print(warning)

    # -----COUNT ERRORS -----
    print("\n=== COUNT ERRORS ===")
    errors = read_logs("server_logs.txt")
    total_errors = count_errors(errors)
    print("Total ERRORS:",total_errors)

