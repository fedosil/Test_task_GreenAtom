from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import time
from bs4 import BeautifulSoup


def main():
    base_dir = os.getcwd()
    executable_path = base_dir + r'\chromedriver_win32\chromedriver.exe'
    service = Service(executable_path=executable_path)
    driver = webdriver.Chrome(service=service)
    url = 'https://greenatom.ru'
    try:
        driver.get(url=url)
        time.sleep(4)
        html_text = driver.page_source
        tag_count, tag_attribute_count = parse_html(html_text)
        print('Кол-во HTML-тегов:', tag_count)
        print('Кол-во HTML-тегов с атрибутами:', tag_attribute_count)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def parse_html(html_text: str) -> tuple:
    soup = BeautifulSoup(html_text, "html.parser")
    tag_count = 0
    attribute_count = 0
    for tag in soup.find_all():
        tag_count += 1
        if tag.attrs:
            attribute_count += 1
    return tag_count, attribute_count


if __name__ == '__main__':
    main()
