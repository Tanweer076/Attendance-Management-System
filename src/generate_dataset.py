import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# -----------------------------
# CONFIGURATION
# -----------------------------
NUM_EMPLOYEES = 30
START_DATE = "2024-01-01"
END_DATE = "2024-02-29"

SHIFT_START = 9 * 60   # 9:00 AM in minutes
SHIFT_END = 18 * 60   # 6:00 PM in minutes

np.random.seed(42)

# -----------------------------
# DATE RANGE
# -----------------------------
dates = pd.date_range(start=START_DATE, end=END_DATE)

data = []

# -----------------------------
# DATA GENERATION
# -----------------------------
for emp in range(1, NUM_EMPLOYEES + 1):
    emp_id = f"E{100 + emp}"
    
    for date in dates:
        day_of_week = date.weekday()  # 0 = Monday
        
        # Skip weekends
        if day_of_week >= 5:
            continue
        
        # Random absence (5%)
        if random.random() < 0.05:
            continue
        
        # Normal check-in and check-out
        check_in = int(np.random.normal(SHIFT_START + 15, 10))
        check_out = int(np.random.normal(SHIFT_END - 15, 15))
        
        # Inject anomaly (10%)
        if random.random() < 0.10:
            anomaly_type = random.choice(["late", "early_exit"])
            if anomaly_type == "late":
                check_in = int(np.random.normal(12 * 60, 15))
            elif anomaly_type == "early_exit":
                check_out = int(np.random.normal(15 * 60, 20))
        
        working_hours = max(0, (check_out - check_in) / 60)
        late_minutes = max(0, check_in - SHIFT_START)
        
        data.append([
            emp_id,
            date,
            check_in,
            check_out,
            round(working_hours, 2),
            late_minutes,
            day_of_week
        ])

# -----------------------------
# CREATE DATAFRAME
# -----------------------------
df = pd.DataFrame(data, columns=[
    "Employee_ID",
    "Date",
    "Check_In_Minutes",
    "Check_Out_Minutes",
    "Working_Hours",
    "Late_Minutes",
    "Day_Of_Week"
])

# -----------------------------
# SAVE AS EXCEL FILE
# (IMPORTANT: path relative to src/)
# -----------------------------
df.to_excel("../Data/employee_attendance_dataset.xlsx", index=False)

print("Excel dataset generated successfully!")
