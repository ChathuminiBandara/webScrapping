import requests
from bs4 import BeautifulSoup


# Function to extract data from the given URL and save to a file
def extract_data_from_url(url, file_name):
    # Fetching the webpage content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract specific data (for example, all text content)
        page_content = soup.get_text()

        # Write the extracted content to a file
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(page_content)

        print(f"Data successfully written to {file_name}")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


# Example usage
url = 'https://patpat.lk/vehicle'  # Replace with the specific URL
file_name = 'extracted_data.txt'  # Output file name
extract_data_from_url(url, file_name)
