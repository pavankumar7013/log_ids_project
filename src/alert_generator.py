import csv
from datetime import datetime

def generate_alerts(logs, rule_func, output_path='alerts/alerts.csv'):
    alerts = []
    for line in logs:
        rules = rule_func(line)
        if rules:
            alerts.append([datetime.now().isoformat(), line.strip(), ", ".join(rules)])

    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', 'Log Line', 'Triggered Rules'])
        writer.writerows(alerts)
