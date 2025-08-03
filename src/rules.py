import re
from datetime import datetime

def detect_suspicious(log_line):
    rules_triggered = []

    if "failed login" in log_line.lower():
        rules_triggered.append("Failed Login")

    if re.search(r'\b192\.168\.\d+\.\d+\b', log_line):
        rules_triggered.append("Internal IP Access")

    if re.search(r'\b[0-9]{2}:[0-9]{2}:[0-9]{2}\b', log_line):
        time_match = re.search(r'(\d{2}):(\d{2}):(\d{2})', log_line)
        if time_match:
            hour = int(time_match.group(1))
            if hour < 6 or hour > 22:
                rules_triggered.append("Abnormal Access Time")

    return rules_triggered
