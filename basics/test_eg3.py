from selenium import webdriver


def test_insta():
    driver=webdriver.Chrome()
    driver.get("https://www.instagram.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    act_title=driver.title
    assert act_title=="Instagram"
    driver.close()
