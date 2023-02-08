from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class OrangeHRM_updating_personal_deatils():

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
                        2.Fill out all fields in  Personal details page
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
      time.sleep(3)
      Record = driver.find_element(By.XPATH, "//div[text()='Pradeepa Naganathan']").click()

      Ot_Id = driver.find_element(By.XPATH, '//label[text()="Other Id"]/following::div[1]/input').send_keys("008")
      time.sleep(3)
      driversliscenceno = driver.find_element(By.XPATH, '//label[text()="Other Id"]/following::input[2]').send_keys(
          "LNC123")
      time.sleep(3)
      driver_liscence_date = driver.find_element(By.XPATH,
                                                 '//label[text()="License Expiry Date"]/following::div[1]//input').send_keys(
          "2026-10-05")
      time.sleep(5)
      SSNnumber = driver.find_element(By.XPATH, '//label[text()="SSN Number"]/following::div[1]/input').send_keys("510")
      time.sleep(5)
      sinnumber = driver.find_element(By.XPATH, '//label[text()="SIN Number"]/following::div[1]/input').send_keys("2000")
      time.sleep(3)
      nationality = driver.find_element(By.XPATH,
                                        '//label[text()="Nationality"]/following::div[1]//div[text()="-- Select --"]').click()
      time.sleep(3)
      selectcounty = driver.find_element(By.XPATH, '//span[text()="Angolan"]').click()
      time.sleep(3)
      marital_status = driver.find_element(By.XPATH,
                                           '//label[text()="Marital Status"]/following::div[text()="-- Select --"][1]').click()
      time.sleep(5)
      click_single = driver.find_element(By.XPATH, '//span[text()="Single"]').click()
      time.sleep(5)
      DOB = driver.find_element(By.XPATH,
                                '//label[text()="Date of Birth"]/following::div[3]/input[@placeholder="yyyy-mm-dd"]').send_keys(
          "1994-10-05")
      time.sleep(5)
      selectgender = driver.find_element(By.XPATH, '//input[@value="1"]/following::span[1]').click()
      time.sleep(5)
      military = driver.find_element(By.XPATH, '//label[text()="Military Service"]/following::div[1]//input').send_keys(
          "yes")
      time.sleep(5)

      save_2 = driver.find_element(By.XPATH, '//div/p[text()=" * Required"]/following::button[@type="submit"][1]').click()
      time.sleep(5)
      blood = driver.find_element(By.XPATH, '//label[text()="Blood Type"]/following::div[4]').click()
      time.sleep(5)
      select_blood = driver.find_element(By.XPATH, '//span[text()="B+"]').click()
      time.sleep(5)
      save_3 = driver.find_element(By.XPATH, '//div/p[text()=" * Required"]/following::button[@type="submit"][2]').click()
      print("Testcase5:", "Personal details added sucessfully")


      #Validation:
      Ot_Id_1= driver.find_element(By.XPATH, '//label[text()="Other Id"]/following::div[1]/input')
      print("Ot_Id is displayed:",Ot_Id_1.is_displayed(),"Ot_Id:",Ot_Id_1.text)
      driversliscenceno_1 = driver.find_element(By.XPATH, '//label[text()="Other Id"]/following::input[2]')
      print("driver liscenceno is displayed:",driversliscenceno_1.is_displayed(),"driversliscenceno_1:",driversliscenceno_1.text)
      SSNnumber_1 = driver.find_element(By.XPATH, '//label[text()="SSN Number"]/following::div[1]/input')
      print("SSN is displayed:", SSNnumber_1.is_displayed(), "SSN:", SSNnumber_1.text)
      sinnumber = driver.find_element(By.XPATH, '//label[text()="SIN Number"]/following::div[1]/input')
      print(" sinnumber is displayed:",  sinnumber.is_displayed(), " sinnumber:",  sinnumber.text)
      nationality = driver.find_element(By.XPATH,'//label[text()="Nationality"]/following::div[1]//div[text()="-- Select --"]')
      print(" nationality is displayed:", nationality.is_displayed(), " nationality:", nationality.text)
      selectcounty = driver.find_element(By.XPATH, '//span[text()="Angolan"]')
      print(" selectcounty is displayed:", selectcounty.is_displayed(), " selectcounty:", selectcounty.text)
      marital_status = click_single = driver.find_element(By.XPATH, '//span[text()="Single"]')
      print(" marital_status is displayed:", marital_status.is_displayed(), " marital_status:", marital_status.text)
      DOB = driver.find_element(By.XPATH,'//label[text()="Date of Birth"]/following::div[3]/input[@placeholder="yyyy-mm-dd"]')
      print(" DOB is displayed:", DOB.is_displayed(), " DOB:", DOB.text)
      selectgender = driver.find_element(By.XPATH, '//input[@value="1"]/following::span[1]')
      print(" selectgender is displayed:", selectgender.is_displayed(), " selectgender:", selectgender.text)
      military = driver.find_element(By.XPATH, '//label[text()="Military Service"]/following::div[1]//input')
      print(" military is displayed:", military.is_displayed(), " military:", military.text)
      select_blood = driver.find_element(By.XPATH, '//span[text()="B+"]')
      print(" select_blood is displayed:", select_blood.is_displayed(), " select_blood:", select_blood.text)
      time.sleep(5



ab= OrangeHRM_updating_personal_deatils()
ab.test()




