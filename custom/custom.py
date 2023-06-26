import requests
import re

def check_robots_txt(url):
    # Add the 'robots.txt' suffix to the URL
    robots_url = url.rstrip('/') + '/robots.txt'
    
    # Send a GET request to fetch the robots.txt file
    response = requests.get(robots_url)
    
    if response.status_code == 200:
        # If the robots.txt file exists, check if scraping is allowed
        content = response.text
        
        # Use regular expressions to find 'User-agent' and 'Disallow' directives
        user_agents = re.findall(r'User-agent:\s*(.*?)\s*', content)
        disallowed_paths = re.findall(r'Disallow:\s*(.*?)\s*', content)
        
        # Check if there are any disallowed paths for the '*' user agent
        for user_agent, disallowed_path in zip(user_agents, disallowed_paths):
            if user_agent == '*' and disallowed_path == '/':
                return False
        
        # Scraping is allowed if no disallowed paths for '*' user agent are found
        return True
    
    # If the robots.txt file doesn't exist, assume scraping is allowed
    return True

# Example usage
website_url = 'https://www.example.com'  # Replace with your desired website URL
allowed = check_robots_txt(website_url)

if allowed:
    print("Web scraping is allowed.")
else:
    print("Web scraping is not allowed.")
