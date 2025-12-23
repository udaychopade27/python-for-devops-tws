#try except block for handling errors in API requests
import requests
def get_dad_joke():
    api_url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "text/plain"}
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        joke_text = response.text
        print(f"Dad Joke: {joke_text}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
get_dad_joke()
# This code fetches a random dad joke from the icanhazdadjoke API using the requests library with a specific header to accept plain text.