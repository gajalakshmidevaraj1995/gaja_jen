from selenium import webdriver


def test_google():
    driver=webdriver.Chrome()
    driver.get("https://www.google.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    act_title=driver.title
    assert act_title=="Google"
    driver.close()