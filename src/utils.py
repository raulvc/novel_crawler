import time

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager

from src.consts import DEFAULT_TIMEOUT


def get_driver():
    # emulates chrome
    options = webdriver.ChromeOptions()
    # using headless mode for better performance
    options.add_argument('--headless')

    # selenium detection countermeasures
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.implicitly_wait(DEFAULT_TIMEOUT)

    return driver


def link_has_gone_stale(link):
    try:
        # poll the link with an arbitrary call
        link.find_elements_by_id('doesnt-matter')
        return False
    except StaleElementReferenceException:
        return True


def wait_for_link_to_go_stale(link):
    start_time = time.time()
    while time.time() < start_time + 3:
        if link_has_gone_stale(link):
            return True
        else:
            time.sleep(0.1)
    raise Exception('Timeout waiting for link to go stale')
