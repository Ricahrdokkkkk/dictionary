from bs4 import BeautifulSoup
import requests

word = str(input("Define "))
url = f"https://www.merriam-webster.com/dictionary/{word}"
results = requests.get(url).content
soup = BeautifulSoup(results, "lxml")
first = soup.find("a", class_="important-blue-link")
partofSpeech= first.text
seconds = soup.find("span", class_="dtText")
definition = seconds.text
print(f"\n\n{word.capitalize()} ({partofSpeech.capitalize()})\n{definition}\n")
