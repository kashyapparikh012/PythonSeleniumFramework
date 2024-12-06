from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    shop = (By.LINK_TEXT, "Shop")
    name = (By.CSS_SELECTOR, ".form-group input[name='name']")
    email = (By.CSS_SELECTOR, ".form-group input[name='email']")
    password = (By.CSS_SELECTOR, "#exampleInputPassword1")
    checkbox = (By.CSS_SELECTOR, "#exampleCheck1")
    gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    employmentStatus = (By.CSS_SELECTOR, "#inlineRadio2")
    submitButton = (By.CSS_SELECTOR, "input[value='Submit']")
    alertText = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver):
        self.driver = driver

    def clickShopButton(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEMail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getEmploymentStatus(self):
        return self.driver.find_element(*HomePage.employmentStatus)

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submitButton)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.alertText)

