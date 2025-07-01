import requests
from bs4 import BeautifulSoup

def get_page_title(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else 'No title found'
        return title
    except requests.RequestException as e:
        return f"Error fetching the page: {e}"

def save_title(title, filename='page_title.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(title)
        print(f"Title saved to {filename}")

# Example usage:
url = input("Enter the URL: ")
page_title = get_page_title(url)
print("Webpage Title:", page_title)
save_title(page_title)

