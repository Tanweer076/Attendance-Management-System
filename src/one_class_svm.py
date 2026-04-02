import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import OneClassSVM

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
# APPLY ONE-CLASS SVM
# --------------------------------
ocsvm = OneClassSVM(
    kernel="rbf",
    gamma="scale",
    nu=0.05
)

df["Anomaly"] = ocsvm.fit_predict(X_scaled)

# Convert labels: -1 → Anomaly, 1 → Normal
df["Anomaly"] = df["Anomaly"].map({1: "Normal", -1: "Anomaly"})

# --------------------------------
# SAVE RESULT
# --------------------------------
df.to_excel("../output/attendance_one_class_svm.xlsx", index=False)

print("One-Class SVM applied successfully!")
print(df["Anomaly"].value_counts())
