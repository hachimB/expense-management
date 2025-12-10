from backend import db_helper
import pytest

def test_fetch_expensive_for_date():
    data = db_helper.fetch_expenses_for_date("2024-08-15")
    print(data)
    assert len(data) == 1
    assert data[0]["amount"] == 10
    assert data[0]["category"] == "Shopping"

def test_fetch_all_records():
    data = db_helper.fetch_all_records()
    assert len(data) == 54

