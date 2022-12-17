CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    first_name TEXT, 
    last_name TEXT,phone INTEGER, 
    email TEXT NOT NULL, 
    password TEXT, 
    active INTEGER, 
    date_created TEXT, 
    hire_date INTEGER, 
    user_type TEXT)

CREATE TABLE IF NOT EXISTS Competencies (
    Competency_id INTEGER PRIMARY KEY,
    comp_name TEXT, 
    date_created INTEGER,
    competency_scale INTEGER)

CREATE TABLE IF NOT EXISTS Assessments (
    assessment_id INTEGER PRIMARY KEY, 
    date_created INTEGER,
    assessment_name TEXT)

CREATE TABLE IF NOT EXISTS Assessment_Results (
    user_id INTEGER,
    assessment_result_name TEXT, 
    assessment_id INTEGER,
    assessment_result_id INTEGER, 
    score INTEGER, date_taken INTEGER, 
    manager TEXT,PRIMARY KEY (user_id, assessment_result_id),
    FOREIGN KEY (user_id) 
        REFERENCES Users (user_id),
    FOREIGN KEY (assessment_id) 
        REFERENCES Assessments (assessment_id)