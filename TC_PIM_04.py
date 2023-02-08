from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class OrangeHRM_Validate_personal_deatils():

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
                        1.Go to Employee List page(Post creation in PIM module).
                        2.Validate below tabs are present in PIM page
                            a.Personal Details
                            b.Contact Details
                            c.Emergency Contacts
                            d.Dependents
                            e.Immigration
                            f.Job
                            g.Salary
                            h.Tax Exemptions
                            i.Report-to
                            j.Qualifications
                            k.Memberships
                     """
      xpath_of_username = "//input[@name='username']"

      xpath_of_password = "//input[@name='password']"

      xpath_of_login = "//button[@type='submit']"

      driver.find_element(By.XPATH, xpath_of_username).send_keys("Admin")
      driver.find_element(By.XPATH, xpath_of_password).send_keys("admin123")
      driver.find_element(By.XPATH, xpath_of_login).click()
      time.sleep(2)

      #Go to Employee List page(Post creation in PIM module)

      # Click (+Add)button on PIM

      xpath_of_PIM = "//a[contains(@href,'viewPimModule')]"
      xpath_of_add_button = "//button[@type='button']/following::button[4]"
      xpath_of_firstName = "//input[@name='firstName']"
      xpath_of_middleName = "//input[@name='middleName']"
      xpath_of_lastName = "//input[@name='lastName']"

      PIM = driver.find_element(By.XPATH, xpath_of_PIM)
      PIM.click()
      time.sleep(2)
      Add = driver.find_element(By.XPATH, xpath_of_add_button).click()
      time.sleep(2)

      firstName = driver.find_element(By.XPATH, xpath_of_firstName)
      firstName.send_keys("Pradeepa")
      time.sleep(2)
      middleName = driver.find_element(By.XPATH, xpath_of_middleName)
      middleName.send_keys("Naganathan")
      time.sleep(2)
      lastName = driver.find_element(By.XPATH, xpath_of_lastName)
      lastName.send_keys("P")
      time.sleep(2)

      Employee_id = driver.find_element(By.XPATH, '//label[text()="Employee Id"]//following::input[1]')
      Employee_id.send_keys(Keys.CONTROL + "a")
      time.sleep(2)
      Employee_id.send_keys(Keys.BACK_SPACE)
      Employee_id.send_keys("51094")
      time.sleep(2)
      driver.find_element(By.XPATH, '//button[@type="submit"]').click()
      time.sleep(5)

      Employee_list = driver.find_element(By.XPATH,"//a[normalize-space()='Employee List']").click()
      time.sleep(2)
      Employee_name = driver.find_element(By.XPATH, "//label[text()='Employee Name']//following::input[1]").send_keys("Pradeepa")
      time.sleep(2)
      search = driver.find_element(By.XPATH, "//button[@type='submit']").click()
      time.sleep(3)
      Record = driver.find_element(By.XPATH, "//div[text()='Pradeepa Naganathan']").click()
      #verify = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]")
      #print(verify.text)
      time.sleep(3)

      # Validate below tabs are present in PIM page

      personal_details = driver.find_element(By.XPATH, "//a[@href='/web/index.php/pim/viewPersonalDetails/empNumber/275']")
      print("personal_details is present:",personal_details.is_displayed(),personal_details.text)

      contact_details = driver.find_element(By.XPATH,"//a[text()='Contact Details']")
      print("contact_details is present:",contact_details.is_displayed(),contact_details.text)

      Emergency_contacts = driver.find_element(By.XPATH, "//a[@href='/web/index.php/pim/viewEmergencyContacts/empNumber/275']")
      print("Emergency_contacts is present:", Emergency_contacts.is_displayed(),Emergency_contacts.text)

      Dependens = driver.find_element((By.XPATH, "//a[@href='/web/index.php/pim/viewDependents/empNumber/275']"))
      print("Dependens is present:", Dependens.is_displayed(),Dependens.text)

      immigration = driver.find_element(By.XPATH, "//a[@href='/web/index.php/pim/viewImmigration/empNumber/275']")
      print("immigration is present:", immigration.is_displayed(),immigration.text)

      job = driver.find_element(By.XPATH, "//a[@href='/web/index.php/pim/viewJobDetails/empNumber/275']")
      print("job is present:", job.is_displayed(),job.text)

      Salary = driver.find_element(By.XPATH, "//a[@href='/web/index.php/pim/viewSalaryList/empNumber/275']")
      print("Salary is present:", Salary.is_displayed(),Salary.text)

      Tax = driver.find_element(By.XPATH,"//a[@href='/web/index.php/pim/viewUsTaxExemptions/empNumber/275']")
      print("Tax is present:", Tax.is_displayed(),Tax.text)

      Report = driver.find_element(By.XPATH, "//a[@href='/web/index.php/pim/viewReportToDetails/empNumber/275']")
      print("Report is present:", Report.is_displayed(), Report.text)

      Membership = driver.find_element(By.XPATH, "href='/web/index.php/pim/viewMemberships/empNumber/275'")
      print("Membership is present:", Membership.is_displayed(), Report.text)
      time.sleep(3)


ab= OrangeHRM_Validate_personal_deatils()
ab.test()





