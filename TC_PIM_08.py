from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class OrangeHRM_updating_Dependency_deatils():

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
                        1.Go to Dependency details and click(Add+).
                        2.Fill out all fields in Dependency details page
                        3.Click save and validate filled details are present under Dependency details

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

      driver.find_element(By.XPATH, '//div[text()="47573"]//following::i[@class="oxd-icon bi-pencil-fill"]').click()
      dependents = driver.find_element(By.XPATH, '//a[text()="Dependents"]').click()
      Add = driver.find_element(By.XPATH, '//h6[text()="Assigned Dependents"]//following::button[1]').click()
      Name = driver.find_element(By.XPATH, '//label[text()="Name"]//following::div[1]/input').send_keys("BALA")
      Relationship = driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"]').click()
      other = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div').click()
      save = driver.find_element(By.XPATH, '//p[text()=" * Required"]//following::button[2]').click()
      print("Testcase8:", "Updated contact details under Assigned Dependents")

      #Validation:
      Name = driver.find_element(By.XPATH, '//label[text()="Name"]//following::div[1]/input')
      print("Name is displayed:", Name.is_displayed(), "Name:", Name.text)
      Relationship = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div')
      print("Relationship is displayed:", Relationship.is_displayed(), "Name:", Relationship.text)


ab= OrangeHRM_updating_Dependency_deatils()
ab.test()
