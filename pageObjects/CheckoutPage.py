from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    # productElements = self.driver.find_elements(By.CSS_SELECTOR, ".card")
    cardTitle = (By.CSS_SELECTOR, ".card")
    # productName = product.find_element(By.CSS_SELECTOR, ".card-body h4 a").text
    productName = (By.CSS_SELECTOR, ".card-body h4 a")
    # product.find_element(By.CSS_SELECTOR, ".card-footer button")
    addProductButton = (By.CSS_SELECTOR, ".card-footer button")
    # self.driver.find_element(By.CSS_SELECTOR, "a.btn-primary").click()
    checkoutButton = (By.CSS_SELECTOR, "a.btn-primary")


    def __init__(self, driver):
        self.driver = driver

    def getProductTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def clickCheckoutButton(self):
        self.driver.find_element(*CheckoutPage.checkoutButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage