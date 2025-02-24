from selenium.webdriver.common.by import By

def test_main(browser,base_url):
    browser.get(base_url)
    browser.find_element(By.CSS_SELECTOR,"img[title=\"Your Store\"]")
    browser.find_element(By.ID, "narbar-menu")
    browser.find_element(By.CSS_SELECTOR, "button[data-bs-toggle=\"dropdown\"][class=\"btn btn-lg btn-inverse btn-block dropdown-toggle\"]")
    browser.find_element(By.CSS_SELECTOR, "a[href=\"http://192.168.27.17:8081/en-gb?route=information/contact\"]")
    browser.find_element(By.CSS_SELECTOR, "#carousel-banner-0")
