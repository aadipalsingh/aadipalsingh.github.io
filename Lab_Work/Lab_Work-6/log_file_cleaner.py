'''Log File Cleaner

Given a log file:

Remove duplicate entries
Filter only ERROR logs
Count occurrences
Use:
set for uniqueness
file handling
'''
# Define the log file path
log_file_path = 'path/to/logfile.log'
# Create a set to store unique ERROR logs
unique_error_logs = set()
# Open the log file and process it
with open(log_file_path, 'r') as log_file:
    for line in log_file:
        # Check if the line contains an ERROR log
        if 'ERROR' in line:
            # Add the ERROR log to the set (duplicates will be ignored)
            unique_error_logs.add(line.strip())
# Count occurrences of each unique ERROR log
error_log_counts = {}
for error_log in unique_error_logs:
    error_log_counts[error_log] = error_log_counts.get(error_log, 0) + 1
# Print the unique ERROR logs and their counts
for error_log, count in error_log_counts.items():
    print(f'{error_log}: {count} occurrences')  
    