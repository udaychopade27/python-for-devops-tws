import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
def fetch_data_from_api(api_url):
    try:
        response = requests.get(url=api_url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data
        print("Data fetched from API:", data)   
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
fetch_data_from_api(api_url)
# response = requests.get(url)
# print(response)