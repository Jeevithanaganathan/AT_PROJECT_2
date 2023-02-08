from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class OrangeHRM_Activation_Job_deatils():

  def test(self):
      driver = webdriver.Chrome()
      baseurl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

      # open the website
      driver.get(baseurl)
      # maximize the window
      driver.maximize_window()
      #driver.implicitly_wait(3)
      time.sleep(2)
      """
                        1.Go to job details
                        2.Click Activate employment
                        3.Validate Employee job Activated
                      """
      driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
      driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
      driver.find_element(By.XPATH, "//button[@type='submit']").click()
      time.sleep(3)

      xpath_of_PIM = "//a[contains(@href,'viewPimModule')]"
      PIM = driver.find_element(By.XPATH, xpath_of_PIM)
      PIM.click()
      time.sleep(3)

      Employee_list = driver.find_element(By.XPATH, "//a[normalize-space()='Employee List']").click()
      time.sleep(3)
      Employee_name = driver.find_element(By.XPATH, "//label[text()='Employee Name']//following::input[1]").send_keys(
          "Pradeepa")
      time.sleep(3)
      search = driver.find_element(By.XPATH, "//button[@type='submit']").click()
      time.sleep(3)
      Record = driver.find_element(By.XPATH, "//div[text()='Pradeepa Naganathan']").click()
      time.sleep(3)

      Job = driver.find_element(By.XPATH, '//a[text()="Job"]').click()
      Activate_employment = driver.find_element(By.XPATH, '//h6[text()="Employee Termination / Activiation"]//following::button[@type="button"][1]').click()
      confirm_text = driver.find_element(By.XPATH, '//h6[text()="Employee Termination / Activiation"]//following::button[@type="button"][1]')
      print("Employee job is activate status:",confirm_text.text)

ab= OrangeHRM_Activation_Job_deatils()
ab.test()
