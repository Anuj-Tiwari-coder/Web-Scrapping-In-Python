import requests
from bs4 import BeautifulSoup
import json

# Define the URL
url = [
    "https://www.investopedia.com/terms/m/mutualfund.asp",
    " https://www.amfiindia.com/investor-corner/knowledge-center/what-are-mutual-funds-new.html",
    "https://zerodha.com/varsity/chapter/introduction-to-mutual-funds/",
    "https://en.wikipedia.org/wiki/Mutual_fund"

]

# Function to fetch and parse data
def scrape_data(url):
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        
        # Parse the webpage content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract relevant sections
        overview = soup.find('div', {'id': 'article-heading_1-0'}).text.strip() if soup.find('div', {'id': 'article-heading_1-0'}) else "N/A"
        summary = soup.find('p').text.strip() if soup.find('p') else "N/A"
        description = soup.find('div', {'id': 'mntl-sc-block_2-0'}).text.strip() if soup.find('div', {'id': 'mntl-sc-block_2-0'}) else "N/A"
        keywords = "mutual funds, investment, finance"  # Manually added as example
        
        # Structure data into JSON format
        data = {
            "Overview": overview,
            "Summary": summary,
            "Description": description,
            "Keywords": keywords,
            "Link": url
        }
        return data

    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Call the function and get the JSON data
data = scrape_data(url)

# Save the JSON data to a file
if data:
    with open('mutual_funds_data.json', 'w') as file:
        json.dump(data, file, indent=4)
    print("Data successfully scraped and saved as 'mutual_funds_data.json'")