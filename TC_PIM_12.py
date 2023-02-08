from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class OrangeHRM_Update_salary_deatils():

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
                        2.Click terminate employment
                        3.fill out Terminate date and reason and click
                        4.Validate Terminate date
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

      salary = driver.find_element(By.XPATH, '//a[text()="Salary"]').click()
      Add =  driver.find_element(By.XPATH, '//h6[text()="Assigned Salary Components"]//following::button[1]').click()
      salary_component = driver.find_element(By.XPATH, '//label[text()="Salary Component"]//following::div[1]/input').send_keys(
          "500000")
      driver.find_element(By.XPATH, '//label[text()="Pay Grade"]//following::div[4]').click()
      Grade = driver.find_element(By.XPATH, '//span[text()="Grade 4"]').click()
      driver.find_element(By.XPATH, '//label[text()="Pay Frequency"]//following::div[4]').click()
      Frequency = driver.find_element(By.XPATH, '//span[text()="Monthly"]').click()
      driver.find_element(By.XPATH, '//label[text()="Currency"]//following::div[4]').click()
      Currency = driver.find_element(By.XPATH, '//span[text()="United States Dollar"]').click()
      Amount = driver.find_element(By.XPATH, '//label[text()="Amount"]//following::div[1]/input').send_keys("35000")
      Comment = driver.find_element(By.XPATH, '//label[text()="Comments"]//following::textarea').send_keys("Salary account")
      time.sleep(3)
      print("Salary details added sucessfully")

      Deposit = driver.find_element(By.XPATH,'//input[@type="checkbox"]').click()
      Acc_No = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[2]/input').send_keys("12345678912")
      save = driver.find_element(By.XPATH,'//button[@type="submit"]').click()
      




ab= OrangeHRM_Update_salary_deatils()
ab.test()