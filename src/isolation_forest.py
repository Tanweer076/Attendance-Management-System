import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# --------------------------------
# LOAD DATASET
# --------------------------------
df = pd.read_excel("../Data/employee_attendance_dataset.xlsx")

# --------------------------------
# SELECT FEATURES (5 ATTRIBUTES)
# --------------------------------
features = [
    "Check_In_Minutes",
    "Check_Out_Minutes",
    "Working_Hours",
    "Late_Minutes",
    "Day_Of_Week"
]

X = df[features]

# --------------------------------
# SCALE DATA
# --------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --------------------------------
# APPLY ISOLATION FOREST
# --------------------------------
iso_forest = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

df["Anomaly"] = iso_forest.fit_predict(X_scaled)

# Convert labels: -1 → Anomaly, 1 → Normal
df["Anomaly"] = df["Anomaly"].map({1: "Normal", -1: "Anomaly"})

# --------------------------------
# SAVE RESULT
# --------------------------------
df.to_excel("../output/attendance_isolation_forest.xlsx", index=False)

print("Isolation Forest applied successfully!")
print(df["Anomaly"].value_counts())
