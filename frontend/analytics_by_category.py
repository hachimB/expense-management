import streamlit as st
import requests
from datetime import datetime
from add_update import API_URL
import pandas as pd


def analytics_by_category():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("start date", datetime(2024, 8, 1))

    with col2:
        end_date = st.date_input("end date", datetime(2024, 8, 10))

    if st.button("Get analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }
        res = requests.post(f"{API_URL}/analytics_by_category", json=payload)
        response = res.json()

        data = {
            "Category": list(response.keys()),
            "Total": [response[category]["total"] for category in response],
            "Percentage": [response[category]["percentage"] for category in response]
        }

        df = pd.DataFrame(data).sort_values(by="Percentage", ascending=False)
        st.title("Expense breakdown by category")
        st.bar_chart(data=df.set_index("Category")["Percentage"])
        st.table(df)