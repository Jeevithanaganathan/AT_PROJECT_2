from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class OrangeHRM_updating_Contact_deatils():

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
                        1.Go to Employee  List page(Post creation in PIM module).
                        2.Fill out all fields in Contact details page
                        3.Click save and validate filled details are present

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
      time.sleep(2)
      Employee_name = driver.find_element(By.XPATH, "//label[text()='Employee Name']//following::input[1]").send_keys(
          "Pradeepa")
      time.sleep(2)
      search = driver.find_element(By.XPATH, "//button[@type='submit']").click()
      time.sleep(2)
      Record = driver.find_element(By.XPATH, "//div[text()='Pradeepa Naganathan']").click()
      time.sleep(3)

      Contact_Details = driver.find_element(By.XPATH, '//a[text()="Contact Details"]').click()
      time.sleep(3)
      Street_1 = driver.find_element(By.XPATH, '//label[text()="Street 1"]//following::div[1]/input').send_keys("WzO/87 OuterRing Road")
      time.sleep(3)
      Street_2 = driver.find_element(By.XPATH, '//label[text()="Street 2"]//following::div[1]/input').send_keys("Vijayanagar")
      time.sleep(3)
      City = driver.find_element(By.XPATH, '//label[text()="City"]//following::div[1]/input').send_keys("banglore")
      time.sleep(3)
      State = driver.find_element(By.XPATH, '//label[text()="State/Province"]//following::div[1]/input').send_keys("karnataka")
      time.sleep(3)
      code = driver.find_element(By.XPATH, '//label[text()="Zip/Postal Code"]//following::div[1]/input').send_keys("603401")
      time.sleep(3)
      country = driver.find_element(By.XPATH, '//label[text()="Country"]/following::div[text()="-- Select --"]').click()
      time.sleep(3)
      driver.find_element(By.XPATH, '//span[text()="Albania"]').click()
      time.sleep(3)
      print("Testcase6:","Contact Details are added sucessfully")
      time.sleep(3)

      #Validation:
      Street_1 = driver.find_element(By.XPATH, '//label[text()="Street 1"]//following::div[1]/input')
      print("Street_1 is displayed:", Street_1.is_displayed(), "Street_1:", Street_1.text)
      Street_2 = driver.find_element(By.XPATH, '//label[text()="Street 2"]//following::div[1]/input')
      print("Street_2 is displayed:", Street_2.is_displayed(), "Street_2:", Street_2.text)
      City = driver.find_element(By.XPATH, '//label[text()="City"]//following::div[1]/input')
      print("City  is displayed:", City .is_displayed(), "City :", City .text)
      State = driver.find_element(By.XPATH, '//label[text()="State/Province"]//following::div[1]/input')
      print("State is displayed:", State.is_displayed(), "State:", State.text)
      code = driver.find_element(By.XPATH, '//label[text()="Zip/Postal Code"]//following::div[1]/input')
      print("code is displayed:", code.is_displayed(), "code:", code.text)
      country = driver.find_element(By.XPATH, '//span[text()="Albania"]')
      print("country is displayed:", country.is_displayed(), "country:", country.text)


ab= OrangeHRM_updating_Contact_deatils()
ab.test()