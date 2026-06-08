PRAGMA foreign_keys = ON;

-- Kullanicilar
INSERT INTO users (id, name, email) VALUES
(1, 'Ali', 'ali@mail.com'),
(2, 'Ayse', 'ayse@mail.com'),
(3, 'Mehmet', 'mehmet@mail.com');

-- Urunler
INSERT INTO products (id, name, price) VALUES
(1, 'Python Kitabi', 150.00),
(2, 'USB Kablo', 45.00),
(3, 'Mouse', 200.00),
(4, 'Klavye', 350.00);

-- Siparisler
INSERT INTO orders (id, user_id, order_date, total_amount) VALUES
(1, 1, '2025-06-01', 285.00),  -- Ali: 1 kitap + 3 kablo
(2, 1, '2025-06-05', 200.00),  -- Ali: 1 mouse
(3, 2, '2025-06-03', 150.00),  -- Ayse: 1 kitap
(4, 3, '2025-06-06', 290.00);  -- Mehmet: 1 mouse + 2 kablo

-- Siparis esyalari
INSERT INTO order_items (id, order_id, product_id, quantity, unit_price) VALUES
(1, 1, 1, 1, 150.00),  -- Siparis 1: kitap
(2, 1, 2, 3,  45.00),  -- Siparis 1: 3 kablo
(3, 2, 3, 1, 200.00),  -- Siparis 2: mouse
(4, 3, 1, 1, 150.00),  -- Siparis 3: kitap
(5, 4, 3, 1, 200.00),  -- Siparis 4: mouse
(6, 4, 2, 2,  45.00);  -- Siparis 4: 2 kablo
