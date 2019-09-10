from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from info import driver_path, boj_id, boj_password


class Submit:
    def __init__(self, driver_path, boj_id, boj_password):
        self.__boj_id = boj_id
        self.__boj_password = boj_password
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument('disable-infobars')
        options.add_argument('disable-extensions')
        options.add_argument('disable-gpu')
        options.add_argument('no-sandbox')
        options.add_argument('disable-dev-shm-usage')
        self.driver = webdriver.Chrome(driver_path, chrome_options=options)
        try:
            self.driver = webdriver.Chrome(driver_path, chrome_options=options)
        except Exception as msg:
            print(msg)
            exit()
        self.driver.implicitly_wait(3)
        
    def signin(self):
        try:
            self.driver.get('https://www.acmicpc.net/login?next=%2F')
            self.driver.find_element_by_name('login_user_id').send_keys(self.__boj_id)
            self.driver.find_element_by_name('login_password').send_keys(self.__boj_password)
            self.driver.find_element_by_name('login_password').send_keys(Keys.RETURN)
            ret = self.driver.find_element_by_css_selector('body>div.wrapper>div.header.no-print>div.topbar>div>ul>li:nth-child(1)>a').text == self.__boj_id
        except Exception as msg:
            print(msg)
            self.driver.close()
            exit()
        return ret


if __name__ == '__main__':
    test = Submit(driver_path, boj_id, boj_password)
    print(test.signin())
    test.driver.close()
