import streamlit as st
from src.processing.ExpenseManager import ExpenseManager


if "em" not in st.session_state:
    st.session_state.em = ExpenseManager()



