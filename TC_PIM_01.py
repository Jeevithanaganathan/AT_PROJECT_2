from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class OrangeHRM_search_box():

    def test(self):
        driver = webdriver.Chrome()

        baseurl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

        # Open_the_website:
        driver.get(baseurl)

        # maximize the window
        driver.maximize_window()
        time.sleep(4)

        driver.implicitly_wait(5)

        """
               1.Go to Admin page.
               2.Validate the below MENU options (On side pane) are displaying on Admin page
               3.Validate the search (Text Box) is displaying on Admin Homepage
               4.Click on search Box and search with below text in (Both Lower and Upper case)
                        A)Admin
                        B)PIM
                        C)Leave
                        D)Time
                        E)Recruitment
                        F)My info
                        G)Performance
                        H)Dashboard
                        I)Directory
                        J)Maintenance
                        K)Buzz
                        
               """

        xpath_of_username = "//input[@name='username']"

        xpath_of_password = "//input[@name='password']"

        xpath_of_login = "//button[@type='submit']"

        driver.find_element(By.XPATH, xpath_of_username).send_keys("Admin")
        driver.find_element(By.XPATH, xpath_of_password).send_keys("admin123")
        driver.find_element(By.XPATH, xpath_of_login).click()
        time.sleep(3)

        # validate menu are displaying on admin page

        menu = driver.find_element(By.XPATH, "//ul[@class='oxd-main-menu']")
        print(menu.is_displayed())
        print(menu.text)
        time.sleep(2)

        # Validate the search (Text Box) is displaying on Admin Homepage
        xpath_of_search = "//input[@placeholder='Search']"
        search_box = driver.find_element(By.XPATH, xpath_of_search)
        print("Textbox display status:", search_box.is_displayed())
        print("Textbox enable status:", search_box.is_enabled())

        # Click on search Box and search with below text in (Both Lower and Upper case)

        list_1 = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory",
                  "Maintenance", "Buzz"]
        for a in list_1:
            search_box.send_keys(a.upper())
            time.sleep(2)
            search_box.send_keys(Keys.CONTROL,'a')
            search_box.send_keys(Keys.BACK_SPACE)
            time.sleep(3)
       # print(a.upper().text)


        for a in list_1:
            search_box.send_keys(a.lower())
            time.sleep(2)
            search_box.send_keys(Keys.CONTROL, 'a')
            search_box.send_keys(Keys.BACK_SPACE)
            time.sleep(3)



ab = OrangeHRM_search_box()
ab.test()
