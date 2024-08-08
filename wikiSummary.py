import requests
from bs4 import BeautifulSoup
import requests
import google.generativeai as genai

url = input("Paste wiki URL > ")

# url = "https://en.wikipedia.org/wiki/Franz_S._Leichter"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")


text = ""

article = soup.find("div", {"class": "mw-parser-output"})

for articles in article:

    content = article.find_all("p")

    for p in content:
        text += p.text

# todo - send this text to gemini for summary

API_KEY = "AIzaSyBOu1Ek1fNT9spoXr9T14i4eSex0DMnklw"


prompt = f"Summarize the text below in no more than 3 paragraphs. {text}"
def summarize_news():
    print()
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"
    

def main():
    print()
    summary = summarize_news()
    print(summary)

if __name__ == "__main__":
    main()



refs = soup.find_all("ol", {"class": "references"})
for ref in refs:
    print(ref.text.replace("^ ", ""))
