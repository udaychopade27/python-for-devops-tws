API_URL = "https://www.alphavantage.co/"

API_KEY = "K724VH4XV3UN4RSH"
symbol = "AMZN"
function = "TIME_SERIES_DAILY"
interval = "5min"
query = f"query?function={function}&symbol={symbol}&interval={interval}&apikey={API_KEY}"
api_url = API_URL + query
print(api_url)

def get_stock_data():
    import requests
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error fetching data: {response.status_code}")
      
get_stock_data()
# This code constructs a URL to fetch daily stock data for IBM from the Alpha Vantage API using the requests library.
# It defines the base API URL, API key, stock symbol, function, and interval, then builds the complete query URL.
# The get_stock_data function sends a GET request to the API and prints the JSON response if successful, or an error message if not.    