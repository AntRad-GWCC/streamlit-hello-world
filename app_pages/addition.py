import streamlit as st
import pandas as pd
import seaborn as sns
from pathlib import Path

st.write(Path.cwd())

BASE_DIR = Path(__file__).resolve().parent
files = [f.name for f in BASE_DIR.iterdir() if f.is_file()]

st.write("Files in current directory:", files)

st.write("Read pkl file:")
CURRENT_DIR = Path(__file__).resolve().parent
pkl_path = CURRENT_DIR / "stocks.pkl"
stockData = pd.read_pickle(pkl_path)

st.write(
    """
    This page is a pull of our Seaborn and Pandas work in Exercise 18, to demonstrate
    the crossover between work previously completed and putting this all in 
    a Streamlit Web Application
    """
)

st.write(
    """
    Displaying the first 5 rows
    """
)
st.write(stockData.head(5))

