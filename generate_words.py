# generate_words.py
import requests

url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(url)
words = [word.decode('utf-8').strip() for word in response.content.splitlines() if len(word) >= 3]

with open("words.txt", "w") as f:
    f.write("\n".join(words))
