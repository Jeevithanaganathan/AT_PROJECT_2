from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class OrangeHRM_Drop_Down():

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
         2.Validate the below MENU options (On side pane) are displaying on Admin page
         3.Click user under user management in header
         4.Validate below field are available under system users:
                a) User Role - Drop Down
                b) Status - Drop Down
      """

    xpath_of_username = "//input[@name='username']"

    xpath_of_password = "//input[@name='password']"

    xpath_of_login = "//button[@type='submit']"

    driver.find_element(By.XPATH, xpath_of_username).send_keys("Admin")
    driver.find_element(By.XPATH, xpath_of_password).send_keys("admin123")
    driver.find_element(By.XPATH, xpath_of_login).click()

    # validate menu are displaying on admin page

    menu = driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul")
    print("menu display status:", menu.is_displayed())
    print("menu enable status:", menu.is_enabled())
    time.sleep(2)

    # Click user under user management in header
    Xpath_of_admin = "//a[@href ='/web/index.php/admin/viewAdminModule']"

    driver.find_element(By.XPATH, Xpath_of_admin).click()

    Xpath_of_usermanagement = "li[class='oxd-topbar-body-nav-tab --parent --visited'] span[class='oxd-topbar-body-nav-tab-item']"
    driver.find_element(By.CSS_SELECTOR, Xpath_of_usermanagement).click()

    Xpath_of_user = "//ul[@class='oxd-dropdown-menu']"
    user = driver.find_element(By.XPATH, Xpath_of_user)
    actions = ActionChains(driver)
    actions.move_to_element(user).click().perform()
    # select admin and Status Enable
    userRole = driver.find_element(By.XPATH, "//label[text()='User Role']")
    actions = ActionChains(driver)
    userRole_select = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]")
    actions.move_to_element(userRole_select).click().perform()
    admin = driver.find_element(By.XPATH, "//label[text()='User Role']/following::span[text()='Admin']")
    actions.move_to_element(admin).click().perform()
    status = driver.find_element(By.XPATH, '//label[text()="Status"]//following::div[4][text()="-- Select --"]')
    actions.move_to_element(status).click().perform()
    enable = driver.find_element(By.XPATH, '//label[text()="Status"]/following::span[text()="Enabled"]')
    actions.move_to_element(enable).click().perform()
    print("Role:", "Admin", "Status:", "Enabled")
    # select ESS and Status Disable
    userRole_1 = driver.find_element(By.XPATH, "//label[text()='User Role']")
    actions = ActionChains(driver)
    userRole_select_1 = driver.find_element(By.XPATH, '//label[text()="User Role"]//following::div[4][text()="Admin"]')
    actions.move_to_element(userRole_select_1).click().perform()
    ESS = driver.find_element(By.XPATH,"//label[text()='User Role'] //following::span[text()='ESS']")
    actions.move_to_element(ESS).click().perform()
    status_1= driver.find_element(By.XPATH, '//label[text()="Status"]//following::div[4][text()="Enabled"]')
    actions.move_to_element(status_1).click().perform()
    Disable = driver.find_element(By.XPATH, '//label[text()="Status"]/following::span[text()="Disabled"]')
    actions.move_to_element(Disable).click().perform()
    print("Role:", "ESS", "Status:", "is Disabled ")






ab = OrangeHRM_Drop_Down()
ab.test()



