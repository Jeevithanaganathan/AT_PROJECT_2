from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class OrangeHRM_updating_Job_deatils():

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
                        1.Go to Emergency Contact details and click(Add+).
                        2.Fill out all fields in Emergency Contacts details page
                        3.Click save and validate filled details are present under Assigned Emergency Contact

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

      job = driver.find_element(By.XPATH, '//a[text()="Job"]').click()
      date = driver.find_element(By.XPATH, '//label[text()="Joined Date"]//following::div[3]/input').send_keys(
          "2016-09-15")

      Title = driver.find_element(By.XPATH, '//label[text()="Job Title"]//following::div[text()="-- Select --"][1]').click()
      Specification = driver.find_element(By.XPATH, '//span[text()="Chief Executive Officer"]').click()
      Category = driver.find_element(By.XPATH,'//label[text()="Job Category"]//following::div[text()="-- Select --"][1]').click()
      job_category = driver.find_element(By.XPATH, '//span[text()="Professionals"]').click()
      subunit = driver.find_element(By.XPATH, '//label[text()="Sub Unit"]//following::div[text()="-- Select --"][1]').click()
      unit= driver.find_element(By.XPATH, '//span[text()="Engineering"]').click()
      driver.find_element(By.XPATH, '//label[text()="Location"]//following::div[text()="-- Select --"][1]').click()
      location = driver.find_element(By.XPATH, '//span[text()="Texas R&D"]').click()
      driver.find_element(By.XPATH,'//div[@class="oxd-select-text oxd-select-text--active"]//following::div[text()="-- Select --"][4]').click()
      status = driver.find_element(By.XPATH,'//div[text()="Full-Time Permanent"]').click()
      time.sleep(3)

      Contract_details = driver.find_element(By.XPATH,'//input[@type="checkbox"]').click()
      contract_startdate= driver.find_element(By.XPATH, '//input[@placeholder="yyyy-mm-dd"]//following::i[@class="oxd-icon bi-calendar oxd-date-input-icon"][2]').send_keys("2023-02-02")
      Contract_enddate = driver.find_element(By.XPATH, '//input[@placeholder="yyyy-mm-dd"]//following::i[@class="oxd-icon bi-calendar oxd-date-input-icon"][3]').send_keys("2025-02-03")
      save = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
      print("Testcase9:", "Job details are present in job details page")

      #validate filled details:
      date = driver.find_element(By.XPATH, '//label[text()="Joined Date"]//following::div[3]/input')
      print("date is displayed:", date.is_displayed(), "date:", date.text)
      Title = driver.find_element(By.XPATH,'//label[text()="Job Title"]//following::div[text()="-- Select --"][1]')
      print("Title is displayed:", Title.is_displayed(), "Title:", Title.text)
      Specification = driver.find_element(By.XPATH, '//span[text()="Chief Executive Officer"]')
      print("Specification is displayed:", Specification.is_displayed(), "Specification:", Specification.text)
      job_category = driver.find_element(By.XPATH, '//span[text()="Professionals"]')
      print("job_category is displayed:", job_category.is_displayed(), "job_category:", job_category.text)
      unit = driver.find_element(By.XPATH, '//span[text()="Engineering"]')
      print("unit is displayed:", unit.is_displayed(), "unit:", unit.text)
      location = driver.find_element(By.XPATH, '//span[text()="Texas R&D"]')
      print("location is displayed:", location.is_displayed(), "location:", location.text)
      status = driver.find_element(By.XPATH, '//div[text()="Full-Time Permanent"]')
      print("status  is displayed:", status .is_displayed(), "status :", status .text)



ab= OrangeHRM_updating_Job_deatils()
ab.test()
