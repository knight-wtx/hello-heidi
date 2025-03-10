## Take-Home Task

A doctor’s clinic uses multiple data sources to track patients, their encounters, diagnoses, appointments, lab results, and staff activity. Your goal is to **unify** these sources into a single source of truth, then create a **simple Python dashboard** showing key metrics.

### What You’ll Do

1. **Load & Transform Data**  
   - You have **three SQL tables**: `patients`, `encounters`, and `diagnoses`.  
   - You have a **CSV file** (`appointments.csv`).  
   - You have a **JSON file** (`lab_results.json`).  
   - You have a **plain text log** (`staff_activity.log`).  
   - **Create a script** to load the three SQL tables into a database (SQLite or any RDBMS).  
   - Ensure your script also **parses/loads** the CSV, JSON, and log files.  

2. **Compute Key Metrics**  
   - **Average Length of Stay**: For inpatient encounters (where `encounter_type = 'inpatient'`) that have a non-null `discharge_date`.  
   - **Top 3 Diagnoses**: By frequency of the `code` field.  
   - **Appointment Completion Rate**: (Number of appointments with `status = 'completed'`) / (total number of appointments).  
   - **Abnormal Lab Results %**: (Number of lab results with `abnormal_flag = true`) / (total number of lab results).  

3. **Propose & Compute 2 Additional Metrics**  
   - Select two new metrics you believe are relevant.  
   - Briefly explain **why** they matter from a business or clinical standpoint.  

4. **Data Model Changes**  
   - Suggest any modifications to the schema or data structures that would make querying and maintenance more efficient or intuitive.

5. **Minimal Dashboard**  
   - Implement a Python-based interface (e.g., a simple console printout or a minimal web app) that displays **all** the final metrics.

6. **Submission**  
   - Provide a link to a **GitHub repository** containing:
     1. Your code (scripts, notebooks, etc.).  
     2. Instructions for how to run it and see the metrics in action.  

---

## Mock Data

The following sample data is provided to help you build and test your solution. You can copy these into separate files (`.sql`, `.csv`, `.json`, `.log`) or embed them directly in your code—whichever is easiest, so long as your script can load them.

---

### 1. SQL Tables

#### `patients`
| patient_id | name           | date_of_birth | registration_date |
|------------|----------------|---------------|-------------------|
| P001       | John Doe       | 1985-01-10    | 2025-02-28        |
| P002       | Jane Smith     | 1990-05-22    | 2025-02-20        |
| P003       | Bob Johnson    | 1972-08-15    | NULL              |
| P004       | Alice Kim      | 2000-07-12    | 2025-03-01        |
| P005       | Michael Brown  | 1960-01-01    | NULL              |

#### `encounters` (10 rows)
| encounter_id | patient_id | admission_date | discharge_date | encounter_type |
|--------------|-----------|----------------|----------------|----------------|
| E100         | P001      | 2025-02-25     | 2025-02-27     | inpatient      |
| E101         | P002      | 2025-02-21     | NULL           | inpatient      |
| E102         | P002      | 2025-03-01     | 2025-03-02     | ER             |
| E103         | P003      | 2025-02-28     | 2025-02-28     | outpatient     |
| E104         | P005      | 2025-03-01     | NULL           | inpatient      |
| E105         | P001      | 2025-03-05     | 2025-03-06     | inpatient      |
| E106         | P003      | 2025-03-02     | 2025-03-02     | outpatient     |
| E107         | P004      | 2025-03-03     | 2025-03-04     | ER             |
| E108         | P004      | 2025-03-06     | NULL           | inpatient      |
| E109         | P005      | 2025-03-02     | 2025-03-03     | inpatient      |

#### `diagnoses` (15 rows)
| diagnosis_id | encounter_id | code | description             |
|--------------|--------------|------|-------------------------|
| D001         | E100         | I10  | Hypertension            |
| D002         | E100         | E11  | Type 2 Diabetes         |
| D003         | E101         | J20  | Acute Bronchitis        |
| D004         | E102         | S06  | Concussion              |
| D005         | E104         | I50  | Heart Failure           |
| D006         | E105         | I10  | Hypertension            |
| D007         | E105         | E11  | Type 2 Diabetes         |
| D008         | E106         | Z00  | General Exam            |
| D009         | E107         | S93  | Ankle Sprain            |
| D010         | E107         | E86  | Dehydration             |
| D011         | E108         | I48  | Atrial Fibrillation     |
| D012         | E108         | E78  | Hyperlipidemia          |
| D013         | E109         | I20  | Angina                  |
| D014         | E109         | E11  | Type 2 Diabetes         |
| D015         | E103         | J45  | Asthma                  |

---

### 2. Appointments (CSV)

**`appointments.csv`**  
```
appointment_id,patient_id,appointment_date,clinic_department,status
A100,P001,2025-03-02,Cardiology,completed
A101,P002,2025-03-03,Orthopedics,canceled
A102,P002,2025-03-03,Orthopedics,completed
A103,P003,2025-03-04,General Medicine,completed
A104,P999,2025-03-05,Neurology,completed
```
> *Note: `P999` does not appear in the `patients` table.*

---

### 3. Lab Results (JSON)

**`lab_results.json`**  
```json
[
  {
    "lab_result_id": "L001",
    "encounter_id": "E100",
    "test_name": "CBC",
    "result_value": 4.5,
    "result_units": "10^3/uL",
    "abnormal_flag": false
  },
  {
    "lab_result_id": "L002",
    "encounter_id": "E101",
    "test_name": "Glucose",
    "result_value": 200,
    "result_units": "mg/dL",
    "abnormal_flag": true
  },
  {
    "lab_result_id": "L003",
    "encounter_id": "E999",
    "test_name": "Lipase",
    "result_value": 300,
    "result_units": "U/L",
    "abnormal_flag": false
  },
  {
    "lab_result_id": "L004",
    "encounter_id": "E102",
    "test_name": "CT Scan",
    "result_value": 1,
    "result_units": "findings",
    "abnormal_flag": false
  },
  {
    "lab_result_id": "L005",
    "encounter_id": "E104",
    "test_name": "BNP",
    "result_value": 800,
    "result_units": "pg/mL",
    "abnormal_flag": true
  }
]
```
> *Note: `E999` does not appear in the `encounters` table.*

---

### 4. Staff Activity Log (Text)

**`staff_activity.log`**  
```
[2025-03-02 09:00:00] user=DrAlice event="LOGIN"
[2025-03-02 09:05:12] user=DrAlice event="VIEWED_PATIENT" patient_id="P001"
[2025-03-03 10:00:00] user=NurseBob event="LOGIN"
[2025-03-03 10:20:11] user=NurseBob event="UPDATED_ENCOUNTER" encounter_id="E100"
[2025-03-04 08:15:00] user=DrEve event="LOGIN"
[2025-03-04 08:18:00] user=DrEve event="VIEWED_PATIENT" patient_id="P003"
```

---

## Final Deliverables

1. **A Script** (or set of scripts) that:
   - Loads the SQL tables (`patients`, `encounters`, `diagnoses`) into a database.  
   - Parses/loads the CSV, JSON, and log files.  
   - Merges/joins data as needed (resolve `patient_id` or `encounter_id`).  

2. **Metrics**:
   - Average Length of Stay  
   - Top 3 Diagnoses  
   - Appointment Completion Rate  
   - Percentage of Abnormal Lab Results  
   - **Your 2 Additional Metrics** (with an explanation of their importance).  

3. **Data Model Changes**: Proposed schema improvements.

4. **Minimal Python Dashboard**: Display all final metrics.

5. **GitHub Repo Link**: Provide clear instructions on how to run your solution.