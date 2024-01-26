import streamlit as st
def load_tailwind():
    return st.markdown(
        """
        <style>
            @import url('https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css');
        </style>
        """,
        unsafe_allow_html=True
        )