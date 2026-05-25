-- Medicines
INSERT INTO medicines (name, category, price) VALUES
('Paracetamol', 'Pain Relief', 50),
('Amoxicillin', 'Antibiotic', 120),
('Cough Syrup', 'Cold', 80);

-- Suppliers
INSERT INTO suppliers (name, contact) VALUES
('ABC Pharma', '9876543210'),
('XYZ Distributors', '9123456780');

-- Inventory
INSERT INTO inventory (medicine_id, supplier_id, quantity, last_updated) VALUES
(1, 1, 100, CURRENT_DATE),
(2, 2, 50, CURRENT_DATE),
(3, 1, 75, CURRENT_DATE);

-- Sales
INSERT INTO sales (medicine_id, quantity_sold, sale_date, total_price) VALUES
(1, 2, CURRENT_DATE, 100),
(2, 1, CURRENT_DATE, 120),
(3, 3, CURRENT_DATE, 240);
