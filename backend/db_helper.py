import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger("db_helper", 'server.log')


@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    print("Closing cursor")
    cursor.close()
    connection.close()


def fetch_all_records():
    query = "SELECT * from expenses"

    with get_db_cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()
        return expenses


def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses


def insert_expense(expense_date, amount, category, notes):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )


def delete_expenses_for_date(expense_date):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))


def fetch_expense_summary(start_date, end_date):
    with get_db_cursor() as cursor:
        cursor.execute('''SELECT category, sum(amount) as total
        FROM expenses WHERE expense_date BETWEEN %s AND %s
        GROUP BY category;''', (start_date, end_date))
        data = cursor.fetchall()
        return data

def fetch_expense_by_month():
    query = '''SELECT DATE_FORMAT(expense_date, '%Y-%m') as month, SUM(amount) AS total_amount 
    FROM expense_manager.expenses GROUP BY month ORDER BY month; '''
    with get_db_cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
        return data



if __name__ == "__main__":
    # fetch_all_records()
    #fetch_expenses_for_date("2024-08-01")
    # insert_expense("2024-08-20", 300, "Food", "Panipuri")
    # delete_expenses_for_date("2024-08-20")
    # fetch_expenses_for_date("2024-08-20")


    summary = fetch_expense_summary("2024-08-01", "2024-09-01")
    for s in summary:
        print(s)