-- Create the Database
CREATE DATABASE hotel_management_db;

-- Switch to the Database
USE hotel_management_db;

-- Create the 'hotel' table
CREATE TABLE hotel (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    zip_code VARCHAR(10),
    phone_number VARCHAR(15),
    email VARCHAR(100),
    star_rating DECIMAL(2, 1) DEFAULT 0.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the 'room' table
CREATE TABLE room (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hotel_id INT NOT NULL,
    room_number VARCHAR(10) NOT NULL,
    room_type VARCHAR(50),
    price_per_night DECIMAL(10, 2) NOT NULL,
    available_from DATE,
    available_to DATE,
    max_guests INT,
    FOREIGN KEY (hotel_id) REFERENCES hotel(id) ON DELETE CASCADE
);

-- Create the 'customer' table
CREATE TABLE customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone_number VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the 'booking' table
CREATE TABLE booking (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_id INT NOT NULL,
    customer_id INT NOT NULL,
    check_in DATE NOT NULL,
    check_out DATE NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    booking_status ENUM('CONFIRMED', 'CANCELLED', 'PENDING') DEFAULT 'PENDING',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES room(id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
);

-- Create the 'payment' table
CREATE TABLE payment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT NOT NULL,
    payment_method ENUM('CASH', 'CREDIT_CARD', 'PAYPAL') NOT NULL,
    amount_paid DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES booking(id) ON DELETE CASCADE
);

-- Insert dummy data into the 'hotel' table
INSERT INTO hotel (name, address, city, state, zip_code, phone_number, email, star_rating)
VALUES 
('Ocean View Hotel', '123 Beach Ave', 'Los Angeles', 'California', '90001', '555-1234', 'info@oceanview.com', 4.5),
('Mountain Retreat', '456 Hillside Dr', 'Denver', 'Colorado', '80014', '555-5678', 'contact@mountainretreat.com', 4.2);

-- Insert dummy data into the 'room' table
INSERT INTO room (hotel_id, room_number, room_type, price_per_night, available_from, available_to, max_guests)
VALUES 
(1, '101', 'Deluxe', 150.00, '2024-09-10', '2024-09-20', 2),
(1, '102', 'Suite', 250.00, '2024-09-15', '2024-09-25', 4),
(2, '201', 'Standard', 120.00, '2024-09-05', '2024-09-15', 2);

-- Insert dummy data into the 'customer' table
INSERT INTO customer (first_name, last_name, email, phone_number)
VALUES 
('John', 'Doe', 'john.doe@example.com', '555-9876'),
('Jane', 'Smith', 'jane.smith@example.com', '555-6543');

-- Insert dummy data into the 'booking' table
INSERT INTO booking (room_id, customer_id, check_in, check_out, total_price, booking_status)
VALUES 
(1, 1, '2024-09-12', '2024-09-14', 300.00, 'CONFIRMED'),
(2, 2, '2024-09-18', '2024-09-20', 500.00, 'PENDING');

-- Insert dummy data into the 'payment' table
INSERT INTO payment (booking_id, payment_method, amount_paid)
VALUES 
(1, 'CREDIT_CARD', 300.00),
(2, 'PAYPAL', 500.00);
