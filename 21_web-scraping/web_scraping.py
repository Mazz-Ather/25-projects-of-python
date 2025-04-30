import requests
from bs4 import BeautifulSoup

try:
    req = requests.get('https://zentry.com')
    req.raise_for_status()  # Raise an error for bad responses
    soup = BeautifulSoup(req.text, 'html.parser')

    # Extract and print the title
    title = soup.title.string if soup.title else 'No title found'
    print(f"Title: {title}\n")

    # Extract and print all headings
    print("Headings:")
    for heading in soup.find_all(['h1', 'h2', 'h3']):
        print(f"  {heading.name}: {heading.get_text(strip=True)}")

    # Extract and print all paragraphs
    print("\nParagraphs:")
    for paragraph in soup.find_all('p'):
        print(f"  {paragraph.get_text(strip=True)}")

    # Extract and print all links
    print("\nLinks:")
    for link in soup.find_all('a', href=True):
        print(f"  {link.get_text(strip=True)}: {link['href']}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")