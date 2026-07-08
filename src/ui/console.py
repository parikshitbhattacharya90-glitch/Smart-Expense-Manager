import streamlit as st
from src.processing.ExpenseManager import ExpenseManager

st.set_page_config(page_title="Smart Expense Manager")

st.title("💰 Smart Expense Manager")
st.write("Welcome! Let's get you started.")

em = ExpenseManager()


username = st.text_input("Username")

password = st.text_input("Password")


if st.button("Enter"):
    em = em.create_user(username, password)


    


    


