CREATE TABLE exchange_rates (
    currency_code VARCHAR(10), 
    exchange_rate DECIMAL(15, 6), 
    valid_date DATE, 
    source TEXT, 
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
