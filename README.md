**1. Buatlah terlebih dahulu database dari PostgreSQL berikut merupakan contoh dari variabel yang digunakan dalam program ini :**

CREATE TABLE vendor (
    id_vendor SERIAL PRIMARY KEY,
    nama_vendor VARCHAR(100) NOT NULL,
    alamat TEXT,
    telepon VARCHAR(20),
    email VARCHAR(100),
    kota VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE produk (
    id_produk SERIAL PRIMARY KEY,
    nama_produk VARCHAR(100) NOT NULL,
    deskripsi TEXT,
    harga NUMERIC(10,2) NOT NULL,
    stok INTEGER DEFAULT 0,
    id_vendor INTEGER,
    kategori VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_vendor 
        FOREIGN KEY (id_vendor) 
        REFERENCES vendor(id_vendor) 
        ON DELETE SET NULL
);


CREATE INDEX idx_produk_vendor ON produk(id_vendor);
CREATE INDEX idx_produk_kategori ON produk(kategori);

-- Insert data contoh untuk Vendor
INSERT INTO vendor (nama_vendor, alamat, telepon, email, kota) VALUES
('PT Maju Jaya', 'Jl. Sudirman No. 123', '021-1234567', 'info@majujaya.com', 'Jakarta'),
('CV Berkah Abadi', 'Jl. Gatot Subroto No. 45', '021-7654321', 'contact@berkah.com', 'Jakarta'),
('UD Sejahtera', 'Jl. Ahmad Yani No. 78', '031-9876543', 'admin@sejahtera.com', 'Surabaya');

-- Insert data contoh untuk Produk
INSERT INTO produk (nama_produk, deskripsi, harga, stok, id_vendor, kategori) VALUES
('Laptop ASUS ROG', 'Laptop gaming dengan spesifikasi tinggi', 15000000.00, 25, 1, 'Elektronik'),
('Mouse Logitech MX', 'Mouse wireless ergonomis', 850000.00, 150, 1, 'Elektronik'),
('Keyboard Mechanical', 'Keyboard gaming RGB', 1200000.00, 80, 2, 'Elektronik'),
('Monitor LG 27 inch', 'Monitor 4K UHD', 4500000.00, 40, 2, 'Elektronik'),
('Headset Gaming', 'Headset dengan mic noise cancelling', 650000.00, 100, 3, 'Elektronik');

**2. Setelah membuat database, ubah config.py sesuai dengan properties dari database di PC anda **
**3. Jalankan program melalui main.py**
