DROP TABLE IF EXISTS patients;
CREATE TABLE patients (
    patient_id TEXT
    , name TEXT
    , date_of_birth TEXT
    , registration_date TEXT
);
INSERT INTO patients (
    patient_id
    , name
    , date_of_birth
    , registration_date
) VALUES
('P001', 'John Doe', '1985-01-10', '2025-02-28'),
('P002', 'Jane Smith', '1990-05-22', '2025-02-20'),
('P003', 'Bob Johnson', '1972-08-15', NULL),
('P004', 'Alice Kim', '2000-07-12', '2025-03-01'),
('P005', 'Michael Brown', '1960-01-01', NULL);