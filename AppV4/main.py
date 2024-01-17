import streamlit as st
import yfinance as yf
import pandas as pd
from langchain.agents import create_pandas_dataframe_agent
from langchain.chat_models import ChatOpenAI
import re
from dotenv import load_dotenv
import sqlite3
from htmlTemplates import css, user_template, bot_template

def main():
    st.set_page_config(page_title="Stock Price AI Bot", page_icon=":chart:")
    st.write(css, unsafe_allow_html=True)
    create_users_db()
    init_ses_states()
    st.title("Stock Price AI Bot")
    st.caption("Visualizations and OpenAI Chatbot for Multiple Stocks Over A Specified Period")

def create_users_db():
    conn = sqlite3.connect('MASTER.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_user_to_db(email, password):
    conn = sqlite3.connect('MASTER.db')
    cursor = conn.cursor()
    insert_query = """
        INSERT INTO Users (email, password)
        VALUES (?, ?)
    """
    cursor.execute(insert_query, (email, password))
    conn.commit()
    conn.close()

def authenticate_user(email, password):
    conn = sqlite3.connect('MASTER.db')
    cursor = conn.cursor()
    select_query = """
        SELECT * FROM Users WHERE email = ? AND password = ?
    """
    cursor.execute(select_query, (email, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        return True
    else:
        return False

def init_ses_states():
    st.session_state.setdefault('chat_history', [])
    st.session_state.setdefault('user_authenticated', False)

# ... (Other functions remain the same)

if __name__ == '__main__':
    load_dotenv()
    # Add a sample user for testing purposes
    add_user_to_db(email='sample@example.com', password='SamplePassword123')
    main()
