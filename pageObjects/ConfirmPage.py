from selenium.webdriver.common.by import By


class ConfirmPage:

    # selectedProduct = self.driver.find_element(By.CSS_SELECTOR, "h4").text
    productName = (By.CSS_SELECTOR, "h4")
    # self.driver.find_element(By.XPATH, "//button[normalize-space()='Checkout']")
    checkoutButton = (By.XPATH, "//button[normalize-space()='Checkout']")
    # self.driver.find_element(By.ID, "country")
    country = (By.ID, "country")
    # self.driver.find_element(By.LINK_TEXT, "India")
    selectedCountry = (By.LINK_TEXT, "India")
    # self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
    checkbox = (By.XPATH, "//label[@for='checkbox2']")
    # self.driver.find_element(By.XPATH, "//input[@value='Purchase']")
    purchaseButton = (By.XPATH, "//input[@value='Purchase']")
    # self.driver.find_element(By.CSS_SELECTOR, ".alert-success")
    successMessage = (By.CSS_SELECTOR, ".alert-success")

    def __init__(self, driver):
        self.driver = driver

    def getProductName(self):
        return self.driver.find_element(*ConfirmPage.productName)

    def getCheckOutButton(self):
        return self.driver.find_element(*ConfirmPage.checkoutButton)

    def getCountryField(self):
        return self.driver.find_element(*ConfirmPage.country)

    def getSelectedCountry(self):
        return self.driver.find_element(*ConfirmPage.selectedCountry)

    def getCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.successMessage)