import time

import pytest

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):

        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("Entering form data")
        log.info("First name is: " + getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEMail().send_keys(getData["email"])
        homePage.getPassword().send_keys(getData["password"])
        homePage.getCheckbox().click()
        self.selectDropdownOptionsByText(homePage.getGender(), getData["gender"])
        homePage.getEmploymentStatus().click()
        homePage.getSubmitButton().click()
        alertText = homePage.getSuccessMessage().text
        log.info("Text received from application after submitting the form is: " + alertText)
        assert "Success!" in alertText
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getData(self, request):
        return request.param
