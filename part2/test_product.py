from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_product(browser):
    browser.get("http://192.168.27.17:8081/en-gb/product/desktops/mac/imac")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"content\"]/div[1]/div[2]/h1")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.price-new")))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-cart")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#tab-description")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img.img-thumbnail.mb-3")))