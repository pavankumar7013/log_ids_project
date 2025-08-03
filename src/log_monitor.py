import os

def read_logs(log_dir):
    logs = []
    for filename in os.listdir(log_dir):
        if filename.endswith('.log') or filename.endswith('.txt'):
            with open(os.path.join(log_dir, filename), 'r') as f:
                logs.extend(f.readlines())
    return logs
