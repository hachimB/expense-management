# 💰 Expense Management System

A full-stack expense tracking application built with **FastAPI** and **Streamlit**, designed to help users manage their daily expenses with powerful analytics and visualizations.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Contact](#-contact)

---

## ✨ Features

### Core Functionality
- ✅ **Add/Update Expenses**: Record daily expenses with amount, category, and notes
- ✅ **Date-based Management**: Organize expenses by date for easy tracking
- ✅ **Category Classification**: Predefined categories (Rent, Food, Shopping, Entertainment, Other)
- ✅ **Bulk Operations**: Add or update multiple expenses at once

### Analytics & Insights
- 📊 **Category Analytics**: Breakdown of expenses by category with percentages
- 📈 **Monthly Trends**: Visualize spending patterns across months
- 🔍 **Date Range Filtering**: Custom date range analysis
- 📉 **Interactive Charts**: Bar charts for visual data representation

### Technical Features
- ⚡ **RESTful API**: FastAPI backend with automatic documentation
- 🎨 **Modern UI**: Streamlit frontend with intuitive interface
- 🗄️ **Database Integration**: Persistent storage with MySQL
- 🔒 **Data Validation**: Pydantic models for type safety
- 📱 **Responsive Design**: Works on desktop and tablet devices

---

### Quick Preview
```bash
# Clone and run in 2 minutes
git clone https://github.com/hachimB/expense-management.git
cd expense-management
pip install -r requirements.txt
# Start backend: uvicorn main:app --reload
# Start frontend: streamlit run app.py
```

---

## 🛠️ Tech Stack

### Backend
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern, fast web framework for building APIs
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Data validation using Python type annotations
- **[MySQL](https://www.mysql.com/)** - Relational database for data persistence
- **[Uvicorn](https://www.uvicorn.org/)** - ASGI server for FastAPI

### Frontend
- **[Streamlit](https://streamlit.io/)** - Python framework for data apps
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation and analysis
- **[Requests](https://requests.readthedocs.io/)** - HTTP library for API calls

### Development Tools
- **Python 3.9+**
- **Git** for version control
- **MySQL Workbench** for database management

---

## 🏗️ Architecture

```
┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
│   Streamlit     │  HTTP   │    FastAPI      │  SQL    │     MySQL       │
│   Frontend      │ ──────> │    Backend      │ ──────> │    Database     │
│   (Port 8501)   │ <────── │   (Port 8000)   │ <────── │                 │
└─────────────────┘         └─────────────────┘         └─────────────────┘
      │                              │                            │
      │                              │                            │
  User Interface              REST API Endpoints            Data Storage
  - Add/Update                - GET /expenses/{date}       - Expenses table
  - Analytics                 - POST /expenses/{date}      - Transactions
  - Visualizations            - DELETE /expenses/{date}    - Categories
                              - POST /analytics_by_category
                              - GET /analytics_by_months
```

---

## 📦 Installation

### Prerequisites
- Python 3.9 or higher
- MySQL Server 8.0+
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/hachimB/expense-management.git
cd expense-management
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Database Setup
```sql
-- Create database
CREATE DATABASE expense_manager;

-- Create expenses table
CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    category VARCHAR(50) NOT NULL,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create index for faster queries
CREATE INDEX idx_date ON expenses(date);
CREATE INDEX idx_category ON expenses(category);
```

### Step 5: Configure Database Connection
Create a `db_config.py` file:
```python
DB_CONFIG = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "expense_manager"
}
```

### Step 6: Update `db_helper.py`
```python
import mysql.connector
from db_config import DB_CONFIG

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# Add your database helper functions here
```

---

## 🚀 Usage

### Starting the Backend (FastAPI)
```bash
# Terminal 1
uvicorn main:app --reload

# The API will be available at: http://localhost:8000
# API docs available at: http://localhost:8000/docs
```

### Starting the Frontend (Streamlit)
```bash
# Terminal 2
streamlit run app.py

# The app will open automatically at: http://localhost:8501
```

### Using the Application

#### 1. Add/Update Expenses
- Select a date from the date picker
- Enter up to 5 expenses with amount, category, and notes
- Click "Submit" to save

#### 2. View Analytics by Category
- Choose a start and end date
- Click "Get analytics" to view breakdown
- See bar chart and percentage distribution

#### 3. View Monthly Analytics
- Automatically displays monthly expense totals
- Sorted by highest spending months
- Visual bar chart representation

---

## 📚 API Documentation

### Base URL
```
http://localhost:8000
```

### Endpoints

#### 1. Get Expenses for a Date
```http
GET /expenses/{expense_date}
```
**Parameters:**
- `expense_date` (date): Date in YYYY-MM-DD format

**Response:**
```json
[
  {
    "amount": 50,
    "category": "Food",
    "notes": "Lunch at restaurant"
  }
]
```

#### 2. Add/Update Expenses
```http
POST /expenses/{expense_date}
```
**Request Body:**
```json
[
  {
    "amount": 100,
    "category": "Shopping",
    "notes": "New shoes"
  }
]
```

**Response:**
```json
{
  "successfully inserted": "[{'amount': 100, 'category': 'Shopping', 'notes': 'New shoes'}]"
}
```

#### 3. Delete Expenses
```http
DELETE /expenses/{expense_date}
```
**Response:**
```json
{
  "successfully deleted": "expenses of 2024-08-02 have been successfully deleted"
}
```

#### 4. Analytics by Category
```http
POST /analytics_by_category
```
**Request Body:**
```json
{
  "start_date": "2024-08-01",
  "end_date": "2024-08-10"
}
```

**Response:**
```json
{
  "Food": {
    "total": 500,
    "percentage": 45.5
  },
  "Shopping": {
    "total": 300,
    "percentage": 27.3
  }
}
```

#### 5. Analytics by Months
```http
GET /analytics_by_months
```
**Response:**
```json
[
  {
    "month": "August",
    "total_amount": 1500
  }
]
```

### Interactive API Documentation
Access the auto-generated API docs:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 📞 Contact

**Hachim Boubacar**

- 📧 Email: boubacarhachim@gmail.com
- 💼 LinkedIn: [Hachim Boubacar](https://www.linkedin.com/in/hachim-boubacar-475831254/)
- 🐱 GitHub: [@hachimB](https://github.com/hachimB)