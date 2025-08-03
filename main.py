from src.log_monitor import read_logs
from src.rules import detect_suspicious
from src.alert_generator import generate_alerts
from src.archiver import archive_logs
from src.report_generator import generate_weekly_report

def main():
    logs = read_logs("logs/")
    generate_alerts(logs, detect_suspicious, "alerts/alerts.csv")
    generate_weekly_report("alerts/alerts.csv")
    archive_logs("logs/", "archived_logs/")

if __name__ == "__main__":
    main()
