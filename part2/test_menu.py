from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_menu(browser):
    browser.get("http://192.168.27.17:8081/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 2, poll_frequency=1)

    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"content\"]/h2")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id=\"product-list\"]")))
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"product-list\"]/div[1]/div/div[2]/form/div/button[1]")))
    wait.until(EC.visibility_of_element_located((By.ID, "carousel-banner-0")))
    menu_items = browser.find_elements(By.CSS_SELECTOR, ".list-group-item")
    assert len(menu_items) == 10
