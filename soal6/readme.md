---
__Requirment:__

- **python 3** keatas dan sudah terinstall flask, flask_restfull, flask_cors
- **visual studio code**
- pastikan port **8000** dan **5000** pada komputer anda tidak digunakan
- sudah terinstall **postgresql**

__Langkah membuat database:__

- buka file **query.pgsql** (jawaban nmr 6 Part A terdapat pada file ini)
- buat database arkademy dengan menjalankan 
``` 
CREATE DATABASE arkademy;
```
- create table users dan skills
```
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name varchar(255)
);
CREATE TABLE skills (
    id SERIAL PRIMARY KEY,
    name varchar(255),
    user_id INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
```
- masukan data pada tabel user dan skills
```
INSERT INTO users(name) VALUES('Robert');
INSERT INTO users(name) VALUES('Turah Marcel');

INSERT INTO skills(name,user_id) VALUES('Java',1);
INSERT INTO skills(name,user_id) VALUES('Python',1);
INSERT INTO skills(name,user_id) VALUES('Go',1);
INSERT INTO skills(name,user_id) VALUES('PHP',2);
INSERT INTO skills(name,user_id) VALUES('Ruby',2);
```
__Langkah membuat database:__
- masuk ke folder backend
- klik kanan, lalu pilih open new terminal
- jalankan script **"code ."**
- buka file **arkademy.py**
- Ganti config dibawah menyesuaikan **USER, PASS, HOST, PORT** yang anda gunakan untuk postgresql anda
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kumiskucing@localhost:5432/arkademy'
```
- setelah selesai, tekan F5 pada file "arkademy.py"

__Langkah menjalankan front-end:__
- masuk ke folder **frontend**
- klik kanan, lalu pilih open new terminal
- jalankan script 
```
python3 -m http.server
```
__Langkah untuk tes aplikasi:__
- buka browser anda
- masuk ke halaman localhost:8000
---
