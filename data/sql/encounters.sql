DROP TABLE IF EXISTS encounters;
CREATE TABLE encounters (
    encounter_id TEXT
    , patient_id TEXT
    , admission_date TEXT
    , discharge_date TEXT
    , encounter_type TEXT
);
INSERT INTO encounters (
    encounter_id
    , patient_id 
    , admission_date
    , discharge_date
    , encounter_type
) VALUES 
('E100', 'P001', '2025-02-25', '2025-02-27', 'inpatient'),
('E101', 'P002', '2025-02-21', NULL, 'inpatient'),
('E102', 'P002', '2025-03-01', '2025-03-02', 'ER'),
('E103', 'P003', '2025-02-28', '2025-02-28', 'outpatient'),
('E104', 'P005', '2025-03-01', NULL, 'inpatient'),
('E105', 'P001', '2025-03-05', '2025-03-06', 'inpatient'),
('E106', 'P003', '2025-03-02', '2025-03-02', 'outpatient'),
('E107', 'P004', '2025-03-03', '2025-03-04', 'ER'),
('E108', 'P004', '2025-03-06', NULL, 'inpatient'),
('E109', 'P005', '2025-03-02', '2025-03-03', 'inpatient');