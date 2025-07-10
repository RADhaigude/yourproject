from selenium import webdriver

def test_open_app():
    driver = webdriver.Chrome()
    driver.get("http://example.com")
    assert "Example Domain" in driver.title
    driver.quit()
