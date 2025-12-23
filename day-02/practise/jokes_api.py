# url = "https://official-joke-api.appspot.com/random_joke"
import requests
def get_jokes():
    api_url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        joke_data = response.json()
        print(f"Joke: {joke_data['setup']} - {joke_data['punchline']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        
get_jokes()
# This code fetches a random joke from the Official Joke API using the requests library.



 #curl -H "Accept: text/plain" https://icanhazdadjoke.com/ createa funcytion for ti url
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