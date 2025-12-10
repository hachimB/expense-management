import requests
from add_update import API_URL
import streamlit as st
import pandas as pd

def analytics_by_months():
    st.title("Expense breakdown by Month")
    res = requests.get(f"{API_URL}/analytics_by_months")
    res = res.json()
    df = pd.DataFrame({
        "Month Name": [dt["month"] for dt in res],
        "Total Amount": [dt["total_amount"] for dt in res]
    }).sort_values(by="Total Amount", ascending=False)
    st.bar_chart(data=df.set_index("Month Name"))
    st.table(df)