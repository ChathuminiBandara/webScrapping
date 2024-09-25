import requests
from bs4 import BeautifulSoup


def extract_data_from_url(url, file_name):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        page_content = soup.get_text()
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(page_content)
        print(f"Data successfully written to {file_name}")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")



url = 'https://patpat.lk/vehicle'
file_name = 'extracted_data.txt'
extract_data_from_url(url, file_name)
