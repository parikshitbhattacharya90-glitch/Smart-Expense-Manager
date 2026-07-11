import streamlit as st

st.set_page_config(page_title = "Smart Expense Manager", layout = "wide")




with st.form("Login"):


    username = st.text_input("Username")

    password = st.text_input("Password", type = "password")
    login = st.form_submit_button("Login")



st.write("Don't have an account ?")

if st.button("Create Account"):
    st.switch_page("frontend/pages/registration.py")

