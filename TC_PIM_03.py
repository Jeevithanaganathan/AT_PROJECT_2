from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class OrangeHRM_create_new_employee():

  def test(self):
          driver = webdriver.Chrome()
          baseurl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

          # open the website
          driver.get(baseurl)
          # maximize the window
          driver.maximize_window()
          driver.implicitly_wait(3)

          """
                  1.Go to Admin page.
                  2.Validate the below MENU options (On side pane) are displaying on PIM page
                  3.Click (+Add)button on PIM
                  4.Toggle the "creation Login details on the Add Employee  and fill all the mandatory fields.
                  5.select Enabled - Radio Button
                  6.Click Save button
               """
          xpath_of_username = "//input[@name='username']"

          xpath_of_password = "//input[@name='password']"

          xpath_of_login = "//button[@type='submit']"

          driver.find_element(By.XPATH, xpath_of_username).send_keys("Admin")
          driver.find_element(By.XPATH, xpath_of_password).send_keys("admin123")
          driver.find_element(By.XPATH, xpath_of_login).click()

          # Validate the below MENU options (On side pane) are displaying on PIM page
          menu = driver.find_element(By.CSS_SELECTOR,
                "#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul")
          print("menu display status:", menu.is_displayed())
          print("menu enable status:", menu.is_enabled())
          time.sleep(2)

          # Click (+Add)button on PIM

          xpath_of_PIM = "//a[contains(@href,'viewPimModule')]"
          xpath_of_add_button = "//button[@type='button']/following::button[4]"
          xpath_of_firstName = "//input[@name='firstName']"
          xpath_of_middleName = "//input[@name='middleName']"
          xpath_of_lastName = "//input[@name='lastName']"

          PIM = driver.find_element(By.XPATH, xpath_of_PIM)
          PIM.click()
          Add = driver.find_element(By.XPATH, xpath_of_add_button).click()

          firstName = driver.find_element(By.XPATH, xpath_of_firstName)
          firstName.send_keys("Pradeepa")
          middleName = driver.find_element(By.XPATH, xpath_of_middleName)
          middleName.send_keys("Naganathan")
          lastName = driver.find_element(By.XPATH, xpath_of_lastName)
          lastName.send_keys("P")

          Employee_id = driver.find_element(By.XPATH,'//label[text()="Employee Id"]//following::input[1]')
          Employee_id.send_keys(Keys.CONTROL + "a")
          time.sleep(2)
          Employee_id.send_keys(Keys.BACK_SPACE)
          Employee_id.send_keys("51094")
          time.sleep(2)

          Create_login = driver.find_element(By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()
          time.sleep(2)
          username_1 = driver.find_element(By.XPATH, '//label[text()="Username"]//following::div[1]/input')
          username_1.send_keys("Prathi@001")
          time.sleep(2)
          Password_1 = driver.find_element(By.XPATH, '//label[text()="Password"]//following::div[1]/input')
          Password_1.send_keys("Prathi@5109")
          time.sleep(2)
          Confirm_password = driver.find_element(By.XPATH,
                                                 '//label[text()="Confirm Password"]//following::div[1]/input')
          Confirm_password.send_keys("Prathi@5109")
          time.sleep(2)
          driver.find_element(By.XPATH, '//button[@type="submit"]').click()
          time.sleep(5)



ab = OrangeHRM_create_new_employee()
ab.test()