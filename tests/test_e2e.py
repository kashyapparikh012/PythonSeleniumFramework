import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        checkoutProduct = "Nokia Edge"

        homePage = HomePage(self.driver)
        checkoutPage = homePage.clickShopButton()
        log.info("Getting all the card titles")
        productElements = checkoutPage.getProductTitles()
        for product in productElements:
            product_name = product.find_element(*checkoutPage.productName).text
            if product_name == checkoutProduct:
                log.info(product_name)
                product.find_element(*checkoutPage.addProductButton).click()
                log.info("Product has been added to cart")
                break

        self.scrollWebpageToTop()
        confirmPage = checkoutPage.clickCheckoutButton()

        selectedProduct = confirmPage.getProductName().text
        assert selectedProduct == checkoutProduct
        confirmPage.getCheckOutButton().click()
        log.info("Entering country name as ind")
        confirmPage.getCountryField().send_keys("ind")
        self.verifyLinkPresence("India")
        confirmPage.getSelectedCountry().click()
        confirmPage.getCheckbox().click()
        confirmPage.getPurchaseButton().click()

        successMessage = confirmPage.getSuccessMessage().text
        log.info("Success message received from application is: " + successMessage)
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in successMessage
