import yfinance as yf
import streamlit
import pandas as pd

streamlit.write(
    """
# 1st- DataAPP (Simple Stock Price App)

Below are the stock **closing price** and ***volume*** of TESLA!

"""
)  # define the ticker symbol
tickerSymbol = "TSLA"
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period="1d", start="2000-5-31", end="2023-3-20")
# Open	High	Low	Close	Volume
streamlit.write(
    """
## Closing Price
"""
)
streamlit.line_chart(tickerDf.Close)
streamlit.line_chart(tickerDf.Open)
streamlit.line_chart(tickerDf.High)
streamlit.line_chart(tickerDf.Low)
streamlit.write(
    """
## Volume 
"""
)
streamlit.line_chart(tickerDf.Volume)
