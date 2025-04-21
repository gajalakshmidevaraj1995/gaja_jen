from selenium import webdriver


def test_fb():
    driver=webdriver.Chrome()
    driver.get("https://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    act_title=driver.title
    assert act_title=="Facebook – log in or sign up"
    driver.close()
