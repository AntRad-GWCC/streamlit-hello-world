import streamlit as st
import pandas as pd
import seaborn as sns
from pathlib import Path
import matplotlib as plt

st.write(Path.cwd())

BASE_DIR = Path(__file__).resolve().parent
files = [f.name for f in BASE_DIR.iterdir() if f.is_file()]

st.write("Files in current directory:", files)

# Reading pickle file
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
    Displaying the first 5 rows:
    """
)

st.write(stockData.head(5))

stockData.set_index('Date', inplace=True)
st.write(
    """
    After reindexing Date:
    """
)

st.write(stockData.head(5))

fridays = pd.date_range('01/01/2020','12/31/2020', freq='W-FRI')
stockDataFridays = stockData.reindex(fridays)
st.write(
    """
    Reindexing so data only contains Fridays
    """
)

st.write(stockDataFridays.head(5))

st.write(
    """
    Plotting time!!
    """
)

ax = stockDataFridays.Close.plot()
st.pyplot(ax.figure)

stockDataDown = stockData.resample(rule='ME').mean()
ax2 = stockDataDown.Close.plot()
st.write(
    """
    Downsampling to a monthly frequency
    """
)

st.pyplot(st.pyplot(ax2.figure))