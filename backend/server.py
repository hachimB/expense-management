from fastapi import FastAPI, HTTPException
from datetime import date, datetime
import db_helper
from typing import List
from pydantic import BaseModel

app = FastAPI()


class Expense(BaseModel):
    amount: int
    category: str
    notes: str


class DateRange(BaseModel):
    start_date : date
    end_date: date


@app.get('/expenses/{expense_date}', response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    return expenses

@app.post('/expenses/{expense_date}')
def add_expenses(expense_date: date, expenses: List[Expense]):
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)
    return {"successfully inserted": f"{expenses}"}


@app.delete('/expenses/{expense_date}')
def delete_expenses(expense_date: date):
    db_helper.delete_expenses_for_date(expense_date)
    return {"successfully deleted": f"expenses of {expense_date} have been successfully deleted"}


@app.post("/analytics_by_category")
def get_analytics_by_category(date_range: DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to fetch data")

    total = sum([row["total"] for row in data])
    response = {}
    for row in data:
        response[row["category"]] = {"total": row["total"], "percentage": (row["total"]/total)*100 if total != 0 else 0}
    return response


@app.get("/analytics_by_months")
def get_analytics_by_months():
    data = db_helper.fetch_expense_by_month()
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to fetch data")
    for dt in data:
        dt['month'] = datetime.strptime(dt['month'], "%Y-%m").strftime("%B")

    return data
