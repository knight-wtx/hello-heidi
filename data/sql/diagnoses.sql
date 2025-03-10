DROP TABLE IF EXISTS diagnoses;
CREATE TABLE diagnoses (
    diagnosis_id TEXT
    , encounter_id TEXT
    , code TEXT
    , description TEXT
);
INSERT INTO diagnoses (
    diagnosis_id
    , encounter_id
    , code
    , description
) VALUES 
('D001', 'E100', 'I10', 'Hypertension'),
('D002', 'E100', 'E11', 'Type 2 Diabetes'),
('D003', 'E101', 'J20', 'Acute Bronchitis'),
('D004', 'E102', 'S06', 'Concussion'),
('D005', 'E104', 'I50', 'Heart Failure'),
('D006', 'E105', 'I10', 'Hypertension'),
('D007', 'E105', 'E11', 'Type 2 Diabetes'),
('D008', 'E106', 'Z00', 'General Exam'),
('D009', 'E107', 'S93', 'Ankle Sprain'),
('D010', 'E107', 'E86', 'Dehydration'),
('D011', 'E108', 'I48', 'Atrial Fibrillation'),
('D012', 'E108', 'E78', 'Hyperlipidemia'),
('D013', 'E109', 'I20', 'Angina'),
('D014', 'E109', 'E11', 'Type 2 Diabetes'),
('D015', 'E103', 'J45', 'Asthma');