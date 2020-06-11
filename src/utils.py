from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from src.consts import DEFAULT_TIMEOUT


def get_driver():
    # emulates chrome
    options = webdriver.ChromeOptions()
    # using headless mode for better performance
    options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.implicitly_wait(DEFAULT_TIMEOUT)
    return driver