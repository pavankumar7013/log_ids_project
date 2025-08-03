# 🔐 Log Monitoring and Intrusion Detection System (IDS)

This project is a Python-based Log Monitoring and Intrusion Detection System that scans system logs for suspicious activity—such as multiple failed SSH login attempts—and raises alerts based on predefined rules.

---

## 📂 Project Structure

log_ids_project/
├── logs/
│ └── system.log # Sample log file
├── alerts/
│ └── alerts.csv # Generated alerts saved here
├── log_monitor.py # Main Python script
└── README.md # Project documentation


---

## ⚙️ Configuration

You can configure the detection threshold and time window inside `log_monitor.py`:

```python
FAILED_LOGIN_THRESHOLD = 5          # Number of failed logins to trigger alert
FAILED_WINDOW_MINUTES = 10          # Time window in minutes
LOG_FILE = 'logs/system.log'        # Log file path
ALERT_FILE = 'alerts/alerts.csv'    # Output file for alerts

🧪 Sample Log Format

Jul 31 08:12:45 myserver sshd[12345]: Failed password for invalid user admin from 192.168.1.10 port 22 ssh2

👨‍💻 Author
Pavan Kumar
Email: 22jr1a04e9@gmail.com

