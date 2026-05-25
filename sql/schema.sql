-- Medicines Table
 CREATE TABLE IF NOT EXISTS medicines (
    medicine_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

-- Suppliers Table
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    contact VARCHAR(50)
);

-- Inventory Table
CREATE TABLE IF NOT EXISTS inventory (
    inventory_id SERIAL PRIMARY KEY,
    medicine_id INT REFERENCES medicines(medicine_id),
    supplier_id INT REFERENCES suppliers(supplier_id),
    quantity INT,
    last_updated DATE
);

-- Sales Table
CREATE TABLE IF NOT EXISTS sales (
    sale_id SERIAL PRIMARY KEY,
    medicine_id INT REFERENCES medicines(medicine_id),
    quantity_sold INT,
    sale_date DATE,
    total_price DECIMAL(10,2)
);
