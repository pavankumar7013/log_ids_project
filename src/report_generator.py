import os
import pandas as pd
from datetime import datetime

def generate_weekly_report(alert_csv, output_dir='reports/'):
    df = pd.read_csv(alert_csv)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    df['Severity'] = df['Triggered Rules'].apply(lambda x: "High" if "Failed Login" in x else "Medium")

    week_str = datetime.now().strftime("%Y-%W")
    df.to_csv(os.path.join(output_dir, f"weekly_report_{week_str}.csv"), index=False)
