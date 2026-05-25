# 💊 Pharmacy Data Engineering Project

## 📌 Project Overview
This project is a Pharmacy Data Engineering system that demonstrates:
- Database design and relationships
- Object-Oriented Programming implementation
- ETL (Extract, Transform, Load) pipeline
- API development using FastAPI for real-time operations

---

## ⚙️ Technologies Used

- Python
- PostgreSQL (Database)
- FastAPI (API development)
- Pandas (Data processing)
- Git & GitHub (Version control)

---

## 🧩 Platforms Used

- Visual Studio Code (Development)
- PostgreSQL (Database management)
- Postman (API testing)
- GitHub (Project hosting)

---

## 📂 Project Structure

How to Run the Project

### ✅ Step 1: Install dependencies
```bash
pip install -r requirements.txt

Setup PostgreSQL Database:

CREATE DATABASE pharma_database;

Run ETL Pipeline:

python main.py

Run API:

uvicorn api:app --reload

Test API (Postman)
POST request:

http://127.0.0.1:8000/add-sale?medicine_id=3&quantity=2&price=80

..
``
