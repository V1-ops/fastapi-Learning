A FastAPI + Database application is usually divided like this:

FastAPI Project
│
├── database.py    -> Database connection setup
├── models.py      -> Database table structure
├── schemas.py     -> Request/Response validation
├── dependency.py  -> Database session provider
├── main.py        -> API endpoints

Understanding the Whole Flow First

Suppose user sends:

{
  "name":"Vansh",
  "email":"vansh@gmail.com",
  "age":20
}

FastAPI flow:

Client
   ↓
Schema validates data
   ↓
Main.py receives data
   ↓
Model converts data into DB object
   ↓
Dependency provides DB session
   ↓
Database.py connects to MySQL
   ↓
Data stored in MySQL

1. database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Imports SQLAlchemy tools.

DATABASE_URL
DATABASE_URL = "mysql+pymysql://root:MY%401234@localhost/fastapi_db"

This tells SQLAlchemy:

Use MySQL
↓
Use pymysql driver
↓
Username = root
↓
Password = MY@1234
↓
Host = localhost
↓
Database = fastapi_db
Structure
mysql+pymysql://username:password@host/database