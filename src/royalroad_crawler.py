import os

from bs4 import BeautifulSoup

from src.utils import get_driver
from selenium.common.exceptions import ElementClickInterceptedException


class RoyalRoadCrawler:

    def __init__(self, start_url, output, append):
        self.start_url = start_url
        self.output = os.path.abspath(os.path.expanduser(output))
        self.append = append
        self.driver = get_driver()
        self.has_next = True
        self.file = None

    def run(self):
        self.open_file()
        self.driver.get(self.start_url)
        while self.has_next:
            self.write(self.load_page())
            self.next_page()
        self.file.close()

    def next_page(self):
        next_button = self.driver.find_elements_by_partial_link_text("Next")[1]
        next_button_html = next_button.get_attribute('outerHTML')
        parser = BeautifulSoup(next_button_html, 'html.parser')
        self.has_next = "disabled" not in parser.find({}).attrs
        if self.has_next:
            while True:
                try:
                    next_button.click()
                    break
                except ElementClickInterceptedException:
                    print("banner in the way, closing...")
                    banner_accept = self.driver.find_elements_by_class_name("ncmp__btn")[1]
                    banner_accept.click()


    def load_page(self):
        # extracts text from page
        title_span = self.driver.find_element_by_xpath("//div/h1")
        title = "\n\n%s\n\n" % title_span.text
        print(title)

        content_container = self.driver.find_element_by_class_name("chapter-content")
        content_parser = BeautifulSoup(content_container.get_attribute('innerHTML'), 'html.parser')
        content = [("%s\n\n" % c.text) for c in content_parser.find_all('p')]
        return [title] + content

    def open_file(self):
        if not self.append:
            os.truncate(self.output, 0)  # truncates file to 0 bytes
        self.file = open(self.output, "a+")

    def write(self, content):
        for line in content:
            self.file.write(line)
        self.file.flush()  # dumps to disk on every page
