# Import the required libraries
import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.google.com/"

# Step 1: Get the HTML content of the webpage
try:
    response = requests.get(url)  # Send a request to the URL
    response.raise_for_status()  # Check if the request was successful
    html_content = response.text  # Get the content of the page as text
except requests.exceptions.RequestException as e:
    print("There was an error fetching the webpage:", e)
    exit()  # Exit the program if there's an error

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Extract content from the webpage

# 1. Get the title of the webpage
title = soup.title  # Find the <title> tag
if title:
    print("Page Title:", title.string)  # Get the text inside the <title> tag
else:
    print("No title found on this page.")

# 2. Get all headings (h1, h2, h3, etc.)
print("\nHeadings Found:")
for i in range(1, 7):  # Loop through h1 to h6
    headings = soup.find_all(f'h{i}')
    for heading in headings:
        print(f"h{i}: {heading.get_text()}")

# 3. Get all paragraph tags (<p>)
print("\nParagraphs Found:")
paragraphs = soup.find_all('p')  # Find all <p> tags
for i, para in enumerate(paragraphs, start=1):
    print(f"{i}. {para.get_text()}")  # Print the text inside each paragraph

# 4. Get all links (anchor tags <a>)
print("\nLinks Found:")
anchors = soup.find_all('a')  # Find all <a> tags
for i, anchor in enumerate(anchors, start=1):
    href = anchor.get('href')  # Get the 'href' attribute (the link)
    if href and href != '#':  # Ignore empty or placeholder links
        print(f"{i}. {href}")

# 5. Get all images
print("\nImages Found:")
images = soup.find_all('img')  # Find all <img> tags
for i, img in enumerate(images, start=1):
    src = img.get('src')  # Get the 'src' attribute (the image link)
    alt = img.get('alt', 'No alt text')  # Get the 'alt' attribute, default to 'No alt text'
    if src:
        print(f"{i}. Source: {src}, Alt Text: {alt}")

# 6. Get all text from the entire page
print("\nFull Page Text:")
print(soup.get_text())  # Print all the text content on the page

# 7. Save the scraped content to a file (optional)
with open("scraped_content.txt", "w", encoding="utf-8") as file:
    file.write("Page Title:\n")
    file.write(title.string if title else "No title found\n")
    file.write("\nHeadings:\n")
    for i in range(1, 7):
        headings = soup.find_all(f'h{i}')
        for heading in headings:
            file.write(f"h{i}: {heading.get_text()}\n")
    file.write("\nParagraphs:\n")
    for para in paragraphs:
        file.write(f"{para.get_text()}\n")
    file.write("\nLinks:\n")
    for anchor in anchors:
        href = anchor.get('href')
        if href and href != '#':
            file.write(f"{href}\n")
    file.write("\nImages:\n")
    for img in images:
        src = img.get('src')
        alt = img.get('alt', 'No alt text')
        if src:
            file.write(f"Source: {src}, Alt Text: {alt}\n")
    file.write("\nFull Page Text:\n")
    file.write(soup.get_text())

print("\nScraping complete! The content has been saved to 'scraped_content.txt'.")
