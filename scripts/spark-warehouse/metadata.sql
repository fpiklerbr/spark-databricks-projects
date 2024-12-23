CREATE TABLE metadata (
    last_run_date DATE PRIMARY KEY, 
    is_successful BOOLEAN, 
    error_message TEXT
);
