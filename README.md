# Employee Anomaly Attendance Detection

## Project Type

Group Project (3 Members)

---

## Problem Statement

Employee attendance data often contains hidden anomalies such as irregular check-in times, unusual working hours, or unexpected absences. Detecting these anomalies manually is difficult and time-consuming.

This project detects such anomalies using **Machine Learning anomaly detection algorithms** to help HR identify unusual attendance behavior patterns and improve workforce management.

---

## My Contribution

* Data preprocessing and feature engineering
* Applied anomaly detection algorithms on attendance data
* Implemented Isolation Forest, Local Outlier Factor, and One-Class SVM models
* Model evaluation and comparison
* Data visualization using Matplotlib
* Documentation and report preparation

---

## Algorithms Used

Three anomaly detection algorithms were applied to the attendance dataset:

* **Local Outlier Factor (LOF)** – Detects anomalies based on local density differences
* **One-Class SVM** – Identifies anomalies by learning normal attendance behavior
* **Isolation Forest** – Detects anomalies using random data partitioning

**Results:**

* LOF → Detected **63 anomalies** and **1193 normal records**
* One-Class SVM → Detected **62 anomalies** and **1194 normal records**
* Isolation Forest → Detected **63 anomalies** and **1193 normal records**

---

## Project Structure

```
Employee-Anomaly-Attendance-Detection/
│
├── dataset/                # Attendance dataset
├── preprocessing.py        # Data preprocessing
├── lof_model.py            # Local Outlier Factor
├── ocsvm_model.py          # One-Class SVM
├── isolation_forest.py     # Isolation Forest
├── visualization.py        # Graphs and plots
├── main.py                 # Main file
└── README.md
```

---

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook

---

## How To Run

1. Install dependencies

```
pip install pandas numpy scikit-learn matplotlib seaborn
```

2. Run the project

```
python main.py
```

---

## Output

The system classifies attendance records into:

* Normal Attendance
* Anomalous Attendance

This helps HR to identify:

* Late arrivals
* Early departures
* Unusual work durations
* Frequent absences

---

## Future Improvements

* Real-time anomaly detection
* Web dashboard for HR
* Email alert for anomalies
* Integration with biometric system

---

## Conclusion

This project shows how machine learning can be used to detect unusual patterns in employee attendance data using anomaly detection algorithms like LOF, One-Class SVM, and Isolation Forest.

---
