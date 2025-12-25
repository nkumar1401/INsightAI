import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()


def get_gemini_response(user_query, df):
    # Setup Gemini API [cite: 308, 313]
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-3-pro-preview')

    # Prompt Engineering for safe code execution [cite: 313]
    prompt = f"""
    You are an expert Data Analyst. Given a dataframe 'df' with columns: {list(df.columns)}.
    The user asks: "{user_query}"
    
    Provide ONLY the Python pandas code to answer this. 
    If they ask for a chart, use Plotly and assign it to a variable 'fig'.
    Return the code inside ```python blocks.
    """
    response = model.generate_content(prompt)
    return response.text