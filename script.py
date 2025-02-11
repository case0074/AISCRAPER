from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def scrape_website(website):
    print("launching scraper..")

    chrome_driver_path = "./chromedriver.exe"

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page Loaded")
        html = driver.page_source
        return html
    finally:
        driver.quit()

def extract_body_content(html):

            soup = BeautifulSoup(html, "html.parser")
            body_content = soup.body
            if body_content:
                return str(body_content)
            else:
                return "No body content found"
            
def clean_body_content(body_content):
                soup = BeautifulSoup(body_content, "html.parser")
                for script_or_style in soup(["script", "style"]):
                    script_or_style.extract()

                    cleaned_content = soup.get_text(separator = "\n")
                    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
                    return cleaned_content
            
def split_dom_content(dom_content, max_length = 8000):
    return [
        dom_content [i: i + max_length]  for i in range (0, len(dom_content), max_length)]
