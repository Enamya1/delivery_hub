-- Use the database
USE food_hub;

-- Insert test data into food_categories
INSERT INTO food_categories (name) VALUES
('Pizza'),
('Burgers'),
('Sushi'),
('Pasta'),
('Salads');

-- Insert test data into food_items
INSERT INTO food_items (name, description, price, image_url, category_id) VALUES
('Margherita Pizza', 'Classic pizza with tomatoes, mozzarella, and basil', 10.00, 'http://example.com/images/margherita_pizza.jpg', 1),
('Cheeseburger', 'Juicy beef patty with cheese and lettuce', 5.50, 'http://example.com/images/cheeseburger.jpg', 2),
('California Roll', 'Fresh sushi with avocado, crab, and cucumber', 12.00, 'http://example.com/images/california_roll.jpg', 3),
('Spaghetti Carbonara', 'Traditional pasta with creamy sauce, pancetta, and cheese', 8.00, 'http://example.com/images/spaghetti_carbonara.jpg', 4),
('Caesar Salad', 'Crisp lettuce with Caesar dressing, croutons, and Parmesan', 7.50, 'http://example.com/images/caesar_salad.jpg', 5);

-- Insert test data into users
INSERT INTO users (username, password, email, role) VALUES
('john_doe', 'password123', 'john.doe@example.com', 'customer'),
('admin_user', 'adminpassword', 'admin@example.com', 'admin'),
('jane_smith', 'password456', 'jane.smith@example.com', 'customer');

-- Insert test data into orders
INSERT INTO orders (user_id, total_amount, status) VALUES
(1, 22.50, 'pending'),
(2, 25.50, 'preparing'),
(3, 15.00, 'delivered');

-- Insert test data into order_items
INSERT INTO order_items (order_id, food_item_id, quantity, price) VALUES
(1, 1, 1, 10.00),
(1, 2, 1, 5.50),
(2, 3, 1, 12.00),
(3, 4, 1, 8.00);

-- Insert test data into workers
INSERT INTO workers (name, vehicle_type, status, last_known_latitude, last_known_longitude) VALUES
('Alice', 'Car', 'available', 37.7749, -122.4194),
('Bob', 'Motorcycle', 'on delivery', 34.0522, -118.2437),
('Charlie', 'Bicycle', 'unavailable', 40.7128, -74.0060);

-- Insert test data into deliveries
INSERT INTO deliveries (order_id, delivery_address, delivery_time, delivery_status, worker_id) VALUES
(1, '123 Main St, San Francisco', '2024-11-22 14:30:00', 'pending', 1),
(2, '456 Oak St, Los Angeles', '2024-11-22 15:00:00', 'out for delivery', 2),
(3, '789 Pine St, New York', '2024-11-22 13:00:00', 'delivered', 3);

-- Insert test data into payments
INSERT INTO payments (order_id, payment_status, payment_method) VALUES
(1, 'pending', 'credit_card'),
(2, 'paid', 'paypal'),
(3, 'paid', 'cash_on_delivery');

-- Insert test data into shopping_cart
INSERT INTO shopping_cart (user_id, food_item_id, quantity) VALUES
(1, 1, 2),
(2, 2, 1),
(3, 3, 3);
