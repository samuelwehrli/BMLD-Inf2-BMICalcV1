import streamlit as st

st.set_page_config(page_title="Meine App", page_icon=":material/home:")

pg_home = st.Page("views/home.py", title="Home", icon=":material/home:", default=True)
pg_calculator = st.Page("views/calculator.py", title="BMI-Rechner", icon=":material/calculate:")

pg = st.navigation([pg_home, pg_calculator])
pg.run()
