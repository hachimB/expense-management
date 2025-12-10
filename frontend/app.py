import streamlit as st
from add_update import add_update
from analytics_by_category import analytics_by_category
from analytics_by_months import analytics_by_months


st.title("Expense management project")
tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics By Category", "Analytics By Months"])

with tab1:
    add_update()
with tab2:
    analytics_by_category()
with tab3:
    analytics_by_months()
