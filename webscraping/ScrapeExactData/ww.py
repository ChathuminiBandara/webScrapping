import requests
from bs4 import BeautifulSoup


def extract_data_from_url(url, file_name):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        elements = soup.find_all('div', class_='quote')

        with open(file_name, 'w', encoding='utf-8') as file:
            for element in elements:
                file.write(element.get_text().strip() + '\n')

        print(f"Data successfully written to {file_name}")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


url = 'https://quotes.toscrape.com/'
file_name = 'ww.txt'
extract_data_from_url(url, file_name)
