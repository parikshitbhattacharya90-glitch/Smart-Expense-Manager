import streamlit as st
from src.frontend.api_client.router import Router

st.set_page_config(page_title = "Smart Expense Manager", layout = "wide")

st.title("Smart Expense Manager")
st.write("Welcome to your personal Expense Tracker")

router = Router()

with st.form("Registration"):

    username = st.text_input("Create a username")

    password = st.text_input("Create password", type = "password")    # type = "password" converts all letters into dots

    confirm_p = st.text_input("Confirm password", type = "password")

    register = st.form_submit_button("Register")


if register:
    r = router.register_user(username, password)