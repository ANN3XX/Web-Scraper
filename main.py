import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract specific data from the HTML
    # Example 1: Extract all links on the page
    links = soup.find_all("a")
    link_list = [link.get("href") for link in links]

    # Example 2: Extract all text from paragraph tags
    paragraphs = soup.find_all("p")
    text_list = [paragraph.text.strip() for paragraph in paragraphs]

    # Example 3: Extract all images and their source URLs
    images = soup.find_all("img")
    image_list = [image["src"] for image in images]

    # Example 4: Extract data from a specific element with a given class
    specific_element = soup.find("div", class_="specific-class")
    specific_data = specific_element.text.strip() if specific_element else None

    # Return the extracted data
    return {
        "links": link_list,
        "text": text_list,
        "images": image_list,
        "specific_data": specific_data
    }

# Usage
website_url = "https://example.com"  # Replace with the URL of the website you want to scrape
data = scrape_website(website_url)

# Access the extracted data
print("Links:")
for link in data["links"]:
    print(link)

print("\nText:")
for text in data["text"]:
    print(text)

print("\nImages:")
for image in data["images"]:
    print(image)

print("\nSpecific Data:")
print(data["specific_data"])
