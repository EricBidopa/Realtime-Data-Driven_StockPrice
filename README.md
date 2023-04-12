# Realtime-Data-Driven_StockPrice
Simple Data App that shows the charting price of a specified stocks

This is a simple application that retrieves and displays the 
historical stock data of Tesla (TSLA) 
using the yfinance library and Streamlit
a Python web application framework. The application displays 
the closing price, as well as the volume, 
of the stock using line charts.

The yfinance library is used to retrieve historical
data for a particular stock by creating a Ticker object 
for the desired stock, then using the .history() method 
to get a pandas DataFrame of the stock data for a
specific period. In this case, the period is set to "1d"
to retrieve daily data, and the start and end dates 
are specified as "2000-5-31" and "2023-3-20", respectively.

The Streamlit library is then used to create a simple web 
application that displays the stock data 
in a user-friendly manner. The write() method is used to 
display some introductory text about
the application and the stock being displayed.
The line_chart() method is used to display the 
stock data in the form of line charts.

To use this code, you will need to have the yfinance
You can customize the source code to show the specific 
stock price that you need to see and the ticker duration.


# Getting Started
Clone the repository
## Install the required libraries:
pip install yfinance streamlit pandas
Run the app using streamlit run stockprice.py
Usage
The app displays the historical closing price 
and volume of Tesla's stock. 
The closing price is plotted on a line chart, and 
the volume is plotted on a bar chart. 
The date range can be customized by modifying the 
start and end variables in the yf.Ticker().history() function.

### Please feel free to PR to add any changes or fix errors.
# Cheers


