import pandas as pd

# -------------------------------
# LOAD ORIGINAL DATA
# -------------------------------
base_df = pd.read_excel("../Data/employee_attendance_dataset.xlsx")

# -------------------------------
# LOAD ALGORITHM RESULTS
# -------------------------------
iso_df = pd.read_excel("../output/attendance_isolation_forest.xlsx")
svm_df = pd.read_excel("../output/attendance_one_class_svm.xlsx")
lof_df = pd.read_excel("../output/attendance_lof.xlsx")

# -------------------------------
# ADD RESULT COLUMNS
# -------------------------------
base_df["Isolation_Forest"] = iso_df["Anomaly"]
base_df["One_Class_SVM"] = svm_df["Anomaly"]
base_df["LOF"] = lof_df["Anomaly"]

# -------------------------------
# SAVE FINAL COMBINED FILE
# -------------------------------
base_df.to_excel("../output/final_attendance_anomaly_results.xlsx", index=False)

print("Final combined anomaly result file created successfully!")
