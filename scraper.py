import requests
from bs4 import BeautifulSoup

# News website URL - you can change it
url = "https://www.bbc.com/news"

headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # BBC headlines are mostly in h2 tags
        headlines = soup.find_all('h2')
        
        with open("headlines.txt", "w", encoding="utf-8") as file:
            count = 0
            for h in headlines:
                text = h.text.strip()
                if text != "":
                    file.write(text + "\n")
                    print(text)
                    count += 1
            print(f"\nTotal {count} headlines saved in headlines.txt")
    else:
        print(f"Failed to fetch, Status Code: {response.status_code}")

except Exception as e:
    print("Error:", e)
